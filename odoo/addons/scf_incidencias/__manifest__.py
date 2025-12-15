# -*- coding: utf-8 -*-
{
    'name': "scf_incidencias",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/scf_incidencias_issues.xml',
        'views/menus.xml',
        'views/scf_incidencias_activos.xml',
        'views/scf_incidencias_intervenciones.xml',
        'views/scf_incidencias_etiquetas.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/scf_incidencias_demo.xml',
    ],
    'application': True,
}

