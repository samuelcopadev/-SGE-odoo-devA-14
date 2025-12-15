# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ScfIncidenciasIntervencion(models.Model):
    _name = 'scf_incidencias.intervenciones'
    _description = 'Parte de Trabajo'
    _order = 'date desc'

    name = fields.Char(string='Título del trabajo', required=True, help="Introduce el título")
    description = fields.Text(string='Detalles')
    date = fields.Datetime(string='Fecha', default=fields.Datetime.now)
    time_spent = fields.Float(string='Horas', help="Ej: 1.5")