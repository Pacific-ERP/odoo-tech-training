# -*- coding: utf-8 -*-

from odoo import models, fields, api

class books(models.Model):
    
    _name = 'library.books'
    _description = 'Informations about books'
    
    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    editor = fields.Char(string='Editor', required=True)
    publisher = fields.Char(string='Publisher', required=True)
    year_of_edition = fields.Date(string='Year of Edition', required=False)
    isbn_number = fields.Integer(string='ISBN Number', required=False)
    description = fields.Char(string='Notes', required=False)
    
    genre = fields.Selection(string='Genre',
                             selection=[('thriller', 'Thriller'),
                                        ('romance', 'Romance'),
                                        ('kids', 'Kids'),
                                        ('suspense', 'Suspense')],
                             required=False)