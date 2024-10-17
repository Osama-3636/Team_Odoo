# -*- coding: utf-8 -*-
from email.policy import default

from odoo import models,fields
from unicodedata import digit


class academy(models.Model):
     _name = 'academy.academy'
     _description='Osama Academy'

     name = fields.Char(string='course name', required=True, help='name',index=True)
     #index help search faster

     active = fields.Boolean(default=True)
     completed = fields.Boolean()

     text=fields.Text()

     price = fields.Float(digits=(5,9))

     days = fields.Integer()

     icon = fields.Binary(attachment=True)

     image = fields.Image()

     description = fields.Text()

     date = fields.Date()

     start_time = fields.Datetime()

     end_time = fields.Datetime()

     instructors = fields.Many2one(comodel_name='academy.instructor1')

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

