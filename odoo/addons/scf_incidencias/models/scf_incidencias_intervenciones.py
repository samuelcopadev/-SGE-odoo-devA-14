# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ScfIncidenciasIntervencion(models.Model):
    _name = 'scf_incidencias.intervenciones'
    _description = 'Parte de Trabajo'
    _order = 'date desc' # Ordena por defecto las más recientes primero

    name = fields.Char(string='Título del trabajo', required=True)
    description = fields.Text(string='Detalles')
    
    # Datetime.now: Guarda fecha y hora exacta del sistema.
    date = fields.Datetime(string='Fecha', default=fields.Datetime.now)
    
    # Campo Float: Necesario para poder realizar operaciones matemáticas (sumas) en la vista Tree.
    time_spent = fields.Float(string='Horas', help="Ej: 1.5")
   
    # Asignación automática al técnico que crea el registro.
    user_id = fields.Many2one('res.users', string='Técnico', default=lambda self: self.env.user)

    # ondelete='cascade': Integridad Referencial.
    # Si se borra la Incidencia Padre, Odoo borrará automáticamente todas sus intervenciones hijas
    # para evitar registros huérfanos en la base de datos.
    issue_id = fields.Many2one('scf_incidencias.issues', string='Incidencia', required=True, ondelete='cascade')