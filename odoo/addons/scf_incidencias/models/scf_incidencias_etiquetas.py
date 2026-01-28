# -*- coding: utf-8 -*-
from odoo import models, fields

class ScfIncidenciasEtiquetas(models.Model):
    _name = 'scf_incidencias.etiquetas'
    _description = 'Etiquetas de clasificación'
    
    name = fields.Char(string='Nombre de la Etiqueta', required=True)
    description = fields.Text(string='Descripción')
    
    # Índice de color (0-11) para el widget many2many_tags_avatar
    color = fields.Integer(string='Color')