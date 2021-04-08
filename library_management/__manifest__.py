# -*- coding: utf-8 -*-

{
    'name': 'Library Management',
    
    'summary': """App to manage a library""",
    
    'description': """
        Library management module for:
        - manage books
        - manage customers
        - customer checking out books
        - customer checking organizing books and rental
    """,
    
    'author': 'Gaëtan',
    
    'website': 'https://www.pacific-erp.com',
    
    'category': 'customers apps',
    'version': '0.1',
        
    'depends': ['base'],
    
    'data': [
        'views/library_management_views.xml',
        'views/library_management_menuitems.xml',
        'security/library_management_security.xml',
        'security/ir.model.access.csv',
        ],
    
    'demo': [
        'demo/library_management_demo.xml',
    ],
}