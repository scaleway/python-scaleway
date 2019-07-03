# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2016 Online SAS and Contributors. All Rights Reserved.
#                         Julien Castets <jcastets@scaleway.com>
#                         Romain Gay <rgay@scaleway.com>
#                         Kevin Deldycke <kdeldycke@scaleway.com>
#
# Licensed under the BSD 2-Clause License (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at https://opensource.org/licenses/BSD-2-Clause

import slumber
from six.moves import zip_longest

from . import API


class InvalidToken(Exception):
    pass


class ExpiredToken(InvalidToken):
    pass


class BadToken(InvalidToken):
    pass


class AccountAPI(API):
    """ Interacts with Scaleway Account API.
    """
    base_url = 'https://account.scaleway.com/'

    def perm_matches(self, request_perm, effective_perm):
        """ Evaluates whether `request_perm` is granted by `effective_perm`.

        Permissions are string separated by semi-colon characters.
        Checking of permissions is performed from left to right and stops at
        the first mismatch between `effective_perm` and `request_perm`.

        The `*` character is used to match all permissions at a given step in
        the permission validation process.

        Examples:
        >>> perm_matches('request:auth:read', 'request:auth:*')
        True
        >>> perm_matches('request:auth:read', 'request:*')
        True
        >>> perm_matches('request:auth:read', 'request:log:*')
        False
        >>> perm_matches('request:log:write', 'request:log:read')
        False

        :param request_perm: Currently granted permissions
        :param effective_perm: Actual permission granted to the token
        """
        if request_perm is None:
            return True

        request_perm_parts = request_perm.split(':')
        effective_perm_parts = effective_perm.split(':')

        for (request_perm_part,
             effective_perm_part) in zip_longest(request_perm_parts,
                                                 effective_perm_parts):

            if (
                request_perm_part != effective_perm_part and
                effective_perm_part != '*' and
                effective_perm_part is not None
            ):
                return False

        return True

    def get_resources(self, service=None, name=None, resource=None,
                      include_locked=False):
        """ Gets a list of resources for which the auth token is granted.

        The permissions of a token is the sum of:

        - token's permissions
        - user's permissions
        - user's roles permissions
        - token's roles permissions

        Roles are linked to organizations.

        This function doesn't return the permissions retrieved from locked
        organizations unless `include_locked` is True. Setting `include_lock`
        to True is useful when you need to check the permissions of a token,
        but don't care if the owner's organization is locked or not.

        Note: If you - the reader - are not a staff member, this pydoc might be
        a little confusing. Roles and permissions are not yet fully exposed by
        our APIs, but I promise we will try to expose and document them very
        soon. Anyway, if you have questions, we'll be glad to answer you guys!
        """
        assert isinstance(include_locked, bool)

        if self.auth_token:
            # GET /tokens/:id/permissions on account-api
            query = self.query().tokens(self.auth_token).permissions
        elif self.auth_jwt:
            # GET /jwt/permissions on account-api
            query = self.query().jwt.permissions
        else:
            return []

        query_params = {
            "include_locked": include_locked,
        }

        if resource:
            resources = resource.split(":")
            query_params["organization_key"] = resources[0]

            if len(resources) == 2:
                query_params["resource_key"] = resources[1]

        if name:
            permissions = name.split(":")
            query_params["name"] = permissions[0]

            if len(permissions) == 2:
                query_params["permission"] = permissions[1]

        try:
            response = query.get(**query_params)
        except slumber.exceptions.HttpClientError as exc:
            if exc.response.status_code in (400, 404):
                raise BadToken()

            if exc.response.status_code == 410:
                raise ExpiredToken()

            raise

        # Apply filters on effective permissions
        #
        # >>> print response.get('permissions')
        # {
        #   'service_name': {
        #      'perm_name': ['resource1', 'resource2', ...],
        #      ...
        #   },
        #   ...
        # }
        ret = []

        for (eff_service_name,
             eff_service_perms) in response.get('permissions', {}).items():

            # Filter on service
            if eff_service_name == service or service is None:

                # Filter on perms
                for (eff_perm_name,
                     eff_perm_resources) in eff_service_perms.items():

                    if self.perm_matches(name, eff_perm_name):

                        # Filter on resources
                        ret.extend([
                            eff_perm_resource
                            for eff_perm_resource in eff_perm_resources
                            if self.perm_matches(resource, eff_perm_resource)
                        ])

        return list(set(ret))

    def has_perm(self, service=None, name=None, resource=None,
                 include_locked=False):
        """ Checks if the token has a permission.
        """
        return bool(
            self.get_resources(service=service, name=name, resource=resource,
                               include_locked=include_locked)
        )

    def get_quotas(self, organization):
        """ Gets a list of quotas for the given organization.
        """
        # For now, request more than the default 50 lines
        # TODO: improve this, cf: CP-1660
        response = self.query().organizations(organization).quotas.get(
            per_page=100)
        return response['quotas']

    def get_quota(self, organization, resource):
        """ Gets one quota for the given organization.
        """
        quotas = self.get_quotas(organization)
        return quotas.get(resource)

    def has_quota(self, organization, resource, used=None):
        """ Checks if `organization` has the quota set for `resource`, and if
        `used` is not None, also checks if the quota value is higher than
        `used`.
        """
        quotas = self.get_quotas(organization=organization)

        # Check if the quota is set
        quota_value = quotas.get(resource)
        if quota_value is None:
            return False

        # Check if quota is unlimited
        if quota_value == -1:
            return True
        # If `used` is not None, check it is lower than `quota_value`
        if used is not None and used >= quota_value:
            return False

        return True
