# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ScfIncidenciasIssues(models.Model):
    _name = 'scf_incidencias.issues'
    _description = 'Incidencias'

    @api.model
    def _expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]

    name = fields.Char(string='Título', required=True, help="Introduce el título de la incidencia")
    description = fields.Text(string='Descripción', help="Descripción detallada")
    
    priority = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta')
    ], string='Prioridad', default='0')
    
    date_reported = fields.Date(
        string='Fecha de Reporte',
        default=fields.Date.context_today
    )

    state = fields.Selection([
        ('draft', 'Nueva'),
        ('process', 'En Proceso'),
        ('done', 'Resuelta')
    ], string='Estado', default='draft', group_expand='_expand_states')

    activo_id = fields.Many2one('scf_incidencias.activos',  string='Activo Afectado', help="Selecciona el equipo que tiene el problema")

    activo_image = fields.Binary(related='activo_id.image', string="Imagen del Activo", readonly=True)

    users_id = fields.Many2one( 'res.users', default=lambda self: self.env.user)