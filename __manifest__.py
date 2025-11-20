# -*- coding: utf-8 -*-
{
    'name': "mediterraneo_legal",

    'summary': """
        """,

    'description': """
        Modulo para empresas del area de la contruccion 
    """,

    'author': "Sistecem",
    'website': "http://www.sistecem.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Legal',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'contacts',
        'project',
        'purchase',
        'sale',
        'contract',
        'agreement',
        'agreement_legal',  # OCA
        'dms',  # OCA
        'mgmtsystem',  # OCA
        'mgmtsystem_action',  # OCA
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # Cargar archivo de seguridad
        'security/ir.model.access.csv',


        'views/project_legal.xml',


        'views/mgmtsystem_legal.xml',


        'views/legal_task_type_views.xml',
        'views/legal_action_wizard_views.xml',

       
        'views/agreement_legal.xml',
    ],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
