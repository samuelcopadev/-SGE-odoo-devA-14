# -*- coding: utf-8 -*-
{
    'name': "scf_incidencias",

    'summary': "Gestor de incidencias completo y funcional",

    'description': """
    Módulo para la gestión de incidencias del parque informático.
    Incluye gestión de activos, tickets de soporte y partes de trabajo.
    """,

    'author': "Samuel Copa",
    'website': "https://github.com/samuelcopadev/-SGE-odoo-devA-14",

    'category': 'Technical Support',
    'version': '0.1',
    'license': 'LGPL-3',

    'depends': ['base', 'mail'],

    'data': [
        'security/scf_incidencias_security.xml',
        'security/ir.model.access.csv',
        'views/scf_incidencias_issues.xml',
        'views/menus.xml',
        'views/scf_incidencias_activos.xml',
        'views/scf_incidencias_intervenciones.xml',
        'views/scf_incidencias_etiquetas.xml',
        'views/res_users.xml',
        'reports/scf_incidendcias_report_tempate.xml',
        'reports/scf_incidencias_report.xml',
    ],
    'demo': [
        'demo/scf_incidencias_demo.xml',
    ],
    'application': True,
}

