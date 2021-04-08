# -*- coding: utf-8 -*-

{
    'name': 'Odoo Space Mission',
    
    'summary': """App to help Odoo going on the Moon""",
    
    'descritpion': """
        Module that will plan and help Odoo get to the Moon
    """,
    
    'author': 'Gaëtan',
    
    'website': 'https://www.pacific-erp.com',
    
    'category': 'Space travel',
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'views/Odoo_Space_Mission_views.xml',
        'views/Odoo_Space_Mission_menuitem.xml',
    ],
    
    'demo': [
        'demo/Odoo_Space_Mission_demo.xml',        
    ],
}
