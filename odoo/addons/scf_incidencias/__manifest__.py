# -*- coding: utf-8 -*-
{
    'name': "scf_incidencias",

    'summary': "Gestor de incidencias completo y funcional",

    'description': """
Long description of module's purpose
    """,

    'author': "Samuel Copa",
    'website': "https://github.com/samuelcopadev/-SGE-odoo-devA-14",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/scf_incidencias_security.xml',
        'security/ir.model.access.csv',
        'views/scf_incidencias_issues.xml',
        'views/menus.xml',
        'views/scf_incidencias_activos.xml',
        'views/scf_incidencias_intervenciones.xml',
        'views/scf_incidencias_etiquetas.xml',
        'views/res_users.xml',
        'reports/scf_incidencias_report.xml',
        'reports/scf_incidendcias_report_tempate.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/scf_incidencias_demo.xml',
    ],
    'application': True,
}

