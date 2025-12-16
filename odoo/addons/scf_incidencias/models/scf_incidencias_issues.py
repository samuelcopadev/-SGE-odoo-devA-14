# models/scf_incidencias_issues.py
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ScfIncidenciasIssues(models.Model):
    _name = 'scf_incidencias.issues'
    _description = 'Incidencias'
    # Heredamos de mail.thread para activar el Chatter (historial de mensajes)
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Título', required=True)
    description = fields.Text(string='Descripción', help="Descripción detallada")
    
    activo_id = fields.Many2one('scf_incidencias.activos', string='Activo Afectado', required=True)
    # Campo related: muestra la imagen del activo sin duplicar datos en BDD
    activo_image = fields.Binary(related='activo_id.image', string="Imagen del Activo", readonly=True)
    
    # Asigna por defecto al usuario que crea el registro
    users_id = fields.Many2one('res.users', string='Técnico', default=lambda self: self.env.user)
    date_reported = fields.Date(string='Fecha de Reporte', default=fields.Date.context_today)
    
    # tracking=True registra los cambios de valor en el historial (Chatter)
    priority = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta')
    ], string='Prioridad', default='1', tracking=True)
    
    state = fields.Selection([
        ('draft', 'Nueva'),
        ('process', 'En Proceso'),
        ('done', 'Resuelta')
    ], string='Estado', default='draft', tracking=True)
    
    tag_ids = fields.Many2many('scf_incidencias.etiquetas', string='Etiquetas')
    intervencion_ids = fields.One2many('scf_incidencias.intervenciones', 'issue_id', string='Intervenciones')

    # store=True guarda el cálculo en base de datos para permitir búsquedas y filtros
    total_hours = fields.Float(string='Total Horas', compute='_compute_total_hours', store=True)

    @api.depends('intervencion_ids.time_spent')
    def _compute_total_hours(self):
        # Recalcula el total sumando el tiempo de las líneas de intervención
        for record in self:
            record.total_hours = sum(line.time_spent for line in record.intervencion_ids)

    @api.onchange('activo_id')
    def _onchange_activo_id(self):
        # Automatización: ajusta prioridad según la categoría del activo seleccionado
        if self.activo_id:
            if self.activo_id.category == 'network':
                self.priority = '2'
            elif self.activo_id.category == 'printer':
                self.priority = '0'

    @api.constrains('state', 'total_hours')
    def _check_closing_hours(self):
        # Validación de integridad: impide cerrar la incidencia si no se han imputado horas
        for record in self:
            if record.state == 'done' and record.total_hours == 0:
                raise ValidationError(_("No puedes marcar la incidencia como 'Resuelta' sin haber imputado horas de trabajo."))