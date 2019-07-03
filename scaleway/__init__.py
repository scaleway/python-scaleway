# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2016 Online SAS and Contributors. All Rights Reserved.
#                         Julien Castets <jcastets@scaleway.com>
#
# Licensed under the BSD 2-Clause License (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the
# License at https://opensource.org/licenses/BSD-2-Clause

import logging

# To enable logging, the client application needs to configure the logging std
# module, by calling for instance logging.basicConfig(level=logging.INFO) or
# preferably logging.config.dictConfig.

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:  # pragma no cover
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

# Prevent message "No handlers could be found for logger "scaleway"" to be
# displayed.
logging.getLogger(__name__).addHandler(NullHandler())


__version__ = '1.9.0'
