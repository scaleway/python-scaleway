#!/usr/bin/env python

from client import ApiClient


def main():
    client = ApiClient('access_key', 'secret_key')
    data = {
        'name': 'my name isss',
        'technical_contacts': ('2', '3', '4'),
        'administrative_contacts': ('11', '12', '13'),
        'billing_contacts': ('11', '12', '13'),
    }
    print client.request('/organizations/', method='POST', data=data)

if __name__ == '__main__':
    main()
