# -*- coding: utf-8 -*-
from odoo import models, fields

class ScfIncidenciasEtiquetas(models.Model):
    _name = 'scf_incidencias.etiquetas'
    _description = 'Etiquetas de clasificación'
    _order = 'name asc'

    name = fields.Char(string='Nombre de la Etiqueta', required=True, help="Ej: Urgente, Wifi, Impresora...")
    description = fields.Text(string='Descripción')
    
    color = fields.Integer(string='Color') 
