# -*- coding: utf-8 -*-
from odoo import models, fields

class ScfIncidenciasEtiquetas(models.Model):
    _name = 'scf_incidencias.etiquetas'
    _description = 'Etiquetas de clasificación'
    _order = 'name asc'

    name = fields.Char(string='Nombre de la Etiqueta', required=True, help="Ej: Urgente, Wifi, Impresora...")
    description = fields.Text(string='Descripción')
    
    #Permite elegir un color de una paleta (0-9)
    color = fields.Integer(string='Color') 

    # issue_ids = fields.Many2many('scf_incidencias.issues', string='Incidencias')