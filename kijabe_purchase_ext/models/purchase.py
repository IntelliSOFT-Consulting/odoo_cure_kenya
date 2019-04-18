# -*- coding: utf-8 -*- 
from odoo import models, fields, api

# This class inherit purchase.order model by adding new fields and modifying existing fields
class purchase(models.Model):
    _inherit ='purchase.order'
    # Add new field
    x_division=fields.Selection(
        [
            ('MED', 'MED'), 
            ('NUR', 'NUR'),
            ('CCK', 'CCK'),
            ('SSD', 'SSD'),
            ('HRD', 'HRD'),
            ('FIN', 'FIN'),
            ('OPS', 'OPS')
        ],
        string=u'Division')
    # Modify existing fields
    partner_id = fields.Many2one(string=u'Supplier')
    partner_ref = fields.Char(string=u'Supplier Code')
