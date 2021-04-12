# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class Spaceship(models.Model):
    
    _name = 'spaceship.mission'
    _description = 'Spaceship informations'
    
    name = fields.Char(string='Internal Reference', required=True)
    description = fields.Char(string='Dimensions', required=True)
    
    fuel_type = fields.Selection(string='Fuel Type',
                                 selection=[('gasole', 'Gasole'),
                                            ('atomic fusion', 'Atomic Fusion'),
                                            ('electric', 'Electric')],
                                 copy=False)
    
    active = fields.Boolean(string='Active', default=True)
    
    ship_type = fields.Selection(string='Type of ship',
                                 selection=[('rocket', 'Rocket'),
                                            ('scientist missions', 'Scientist Missions'),
                                            ('biologist missions', 'Biologist Missions')],
                                 copy=False)
    
    number_of_passengers= fields.Integer(string='Number of Passengers', required=True)
    
    largeur = fields.Float(string='Largeur', default=0.00)
    
    longueur = fields.Float(string='Longueur', default=0.00)
    
    mission_ids = fields.One2many(comodel_name='mission.mission',
                                  inverse_name='spaceship_id',
                                  string='Missions')
    
    @api.constrains('largeur', 'longueur')
    def _onchange_longueur(self):
        for record in self:
            if record.longueur < record.largeur:
                raise UserError('La longueur ne peut pas être plus petite que la largeur')