# -*- coding: utf-8 -*-
{
    'name': 'Auth0',
    'version': '1.0',
    'author': 'Odoo Community',
    'summary': 'Auth0 module for Odoo',
    'website': 'https://github.com/idazco/odoo_auth0',
    'description': 'Enables OAuth authentication through Auth0',
    'category': 'Authentication',
    'depends': [
        'auth_oauth','website'
    ],
    'data': [
        'data/data_auth0.xml',
        'data/auto_signup_data.xml',
        'views/signup.xml',
        'views/auth0_views.xml',
        'views/templates.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
