# -*- coding: utf-8 -*-
from odoo import models, fields

class ScfIncidenciasActivo(models.Model):
    _name = 'scf_incidencias.activos'
    _description = 'Activo Informático'
    _order = 'name asc'

    name = fields.Char(string='Código/Nombre', required=True, help="Codigo/Nombre del producto")
    model = fields.Char(string='Modelo', help="Modelo del producto")
    serial_no = fields.Char(string='Nº Serie')
    
    category = fields.Selection([
        ('pc', 'Ordenador / Portátil'),
        ('printer', 'Impresora'),
        ('monitor', 'Monitor'),
        ('network', 'Redes'),
        ('other', 'Otro')
    ], string='Categoría', required=True, default='pc')
    
    purchase_date = fields.Date(string='Fecha de Compra')
    image = fields.Binary(string="Imagen")
    notes = fields.Text(string="Notas")