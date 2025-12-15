# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ScfIncidenciasIssues(models.Model):
    _name = 'scf_incidencias.issues'
    _description = 'Incidencias'

    # Este método fuerza que todas las columnas del Kanban (Nueva, En Proceso, Resuelta)
    # se muestren siempre, incluso si no hay ninguna incidencia en ese estado.
    # Sin esto, las columnas vacías desaparecerían visualmente.
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
    
    # context_today: Usa la zona horaria del cliente (Navegador) para la fecha.
    # Si usáramos fields.Date.today(), usaría la hora del servidor (UTC).
    date_reported = fields.Date(
        string='Fecha de Reporte',
        default=fields.Date.context_today
    )

    # group_expand: Vincula el campo con el método de arriba para pintar el Kanban completo.
    state = fields.Selection([
        ('draft', 'Nueva'),
        ('process', 'En Proceso'),
        ('done', 'Resuelta')
    ], string='Estado', default='draft', group_expand='_expand_states')

    # RELACIONES
    activo_id = fields.Many2one('scf_incidencias.activos', string='Activo Afectado')

    # Campo Related (Espejo):
    # No ocupa espacio real en BBDD (store=False por defecto).
    # readonly=True: Protege la integridad del activo original para no cambiar su foto desde aquí.
    activo_image = fields.Binary(related='activo_id.image', string="Imagen del Activo", readonly=True)

    # Lambda: Se ejecuta en tiempo de creación (Runtime).
    # Asigna dinámicamente el usuario que está logueado en ese momento (self.env.user).
    users_id = fields.Many2one('res.users', default=lambda self: self.env.user)
    
    tag_ids = fields.Many2many('scf_incidencias.etiquetas', string='Etiquetas')

    # One2many: Relación inversa. Apunta al campo 'issue_id' del modelo hijo.
    intervencion_ids = fields.One2many('scf_incidencias.intervenciones', 'issue_id', string='Partes de Trabajo')