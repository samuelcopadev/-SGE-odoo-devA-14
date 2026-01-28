# -*- coding: utf-8 -*-
from odoo import models, fields

class ScfIncidenciasActivo(models.Model):
    _name = 'scf_incidencias.activos'
    _description = 'Activo Informático'
    # Define la ordenación por defecto en las vistas (Listas, búsquedas...)
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

    image = fields.Binary(string="Imagen")
    purchase_date = fields.Date(string="Fecha de Compra")
    notes = fields.Text(string="Notas")

    # Garantizar unicidad física del activo
    _sql_constraints = [
        (
            'serial_no_unique', 
            'UNIQUE(serial_no)', 
            'El número de serie debe ser único. Ya existe un activo registrado con este serial.'
        )
    ]