# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class Mission(models.Model):
    
    _name = 'mission.mission'
    _description = 'Missions informations'
    
    spaceship_id = fields.Many2one(comodel_name='spaceship.mission',
                                   string="Mission",
                                   ondelete='cascade',
                                   required =True)
    
    name = fields.Char(string='Title', related='spaceship_id.name')
    
    assigned_spaceship_id = fields.Many2one(comodel_name='res.partner', string='assigned spaceship to')
    
    crew_members_ids = fields.Many2one(comodel_name='res.partner', string='Crew members')
    
    launch_date = fields.Date(string='Launch Date',
                              required=False)
    
    duration = fields.Integer(string='Duration',
                              default=365,
                              readonly=True)
    
    return_date = fields.Date(string='Return Date',
                              compute='_compute_return_date',
                              store=True)
    
    @api.depends('launch_date', 'duration')
    def _compute_return_date(self):
        for record in self:
            if not (record.launch_date and record.duration):
                record.return_date = record.launch_date
            else:
                duration = timedelta(days=record.duration)
                record.return_date = record.launch_date + duration