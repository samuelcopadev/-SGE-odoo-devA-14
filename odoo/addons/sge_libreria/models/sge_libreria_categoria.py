# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SgeLibreriaCategoria(models.Model):
    _name = 'sge_libreria.categoria'
    _description = 'Categoría'

    name = fields.Char(string='Nombre', required=True, help="Introduce el nombre de la categoria")
    description = fields.Char(string='Descripción', help="Introduce la descripción")
    