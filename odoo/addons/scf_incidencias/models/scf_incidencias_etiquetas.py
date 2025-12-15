# -*- coding: utf-8 -*-
from odoo import models, fields

class ScfIncidenciasEtiquetas(models.Model):
    _name = 'scf_incidencias.etiquetas'
    _description = 'Etiquetas de clasificación'
    
    name = fields.Char(string='Nombre de la Etiqueta', required=True)
    description = fields.Text(string='Descripción')
    
    # Este entero es usado por el widget 'many2many_tags' en el XML.
    # Odoo mapea el número (0-11) a una paleta de colores predefinida en CSS.
    color = fields.Integer(string='Color')