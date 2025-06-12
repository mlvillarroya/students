# -*- coding: utf-8 -*-
{
    'name': "Students management",
    'summary': "Allows to manage the students and appointments",
    'description': """
Allows to manage the students and appointments
    """,

    'author': "Mikel López",
    'website': "https://www.iernestlluch.cat",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Learning',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'mail'],  # Dependencias clave
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/students_views.xml',
        'views/meetings_views.xml',
        'views/menus.xml',
        'views/templates.xml',
        'data/schools.xml',
        'data/relatives.xml',
        'data/students.xml',
        'data/meetings.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": True,
}

