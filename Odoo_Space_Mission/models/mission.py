# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Mission(models.Model):
    
    _name = 'mission.mission'
    _description = 'Missions informations'
    
    spaceship_id = fields.Many2one(comodel_name='spaceship.mission',
                                   string="Mission",
                                   ondelete='cascade',
                                   required =True)
    
    launch_date = fields.Date(string='Launch Date', required=False)
    return_date = fields.Date(string='Return Date', required=True)
    
    name = fields.Char(string='Title', related='spaceship_id.name')
    
    assigned_spaceship_id = fields.Many2one(comodel_name='res.partner', string="Assigned Spaceship")
    
    crew_members_ids = fields.Many2many(comodel_name='res.partner', string='Crew Members')