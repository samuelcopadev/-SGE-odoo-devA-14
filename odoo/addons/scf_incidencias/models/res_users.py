# -*- coding: utf-8 -*-
from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    # Campo nuevo añadido por herencia 
    x_is_technician = fields.Boolean(string="Es Técnico de Soporte", default=False)
