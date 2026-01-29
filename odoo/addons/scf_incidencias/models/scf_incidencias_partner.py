# -*- coding: utf-8 -*-
from odoo import models, fields

class Especialista(models.Model):
    _name = 'scf_incidencias.especialista'
    _inherit = 'res.partner'
    _description = 'Especialista Técnico Externo'

    nivel = fields.Selection([
        ('junior', 'Junior'),
        ('senior', 'Senior'),
        ('master', 'Master')
    ], string="Nivel de Experiencia", default='junior')
    
    certificaciones = fields.Char(string="Certificaciones Técnicas", help="Ej: CCNA, AWS Certified, Odoo Functional")
