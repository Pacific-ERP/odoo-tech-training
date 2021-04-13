# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    spaceship_id = fields.Many2one(comodel_name='mission.mission',
                                   string='Related Mission',
                                   ondelete='set null')
    
    assigned_spaceship_id = fields.Many2one(string= 'Spaceship Assigned to',
                                            related='spaceship_id.assigned_spaceship_id')