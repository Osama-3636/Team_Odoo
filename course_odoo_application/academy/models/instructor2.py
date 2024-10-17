# -*- coding: utf-8 -*-

from odoo import models,fields

# from academy.models.course import get_cities
import os

def get_cities():
    result = []
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'cities.csv')
    with open(csv_path, mode='r') as f:
        for line in f.readlines():
            result.append((line.strip(), line.strip()))
            print(result)

    return result


class academy_instructor(models.Model):
     _name = 'academy.instructor1'
     _description='THe Instructor Osama '

     name = fields.Char(string='course name', required=True, help='name',index=True)
     #index help search faster


     notes=fields.Text()

     payed = fields.Boolean()

     age = fields.Integer()

     icon = fields.Binary()

     expereience=fields.Selection(
         selection=get_cities(),
         required=False, )

     gender= fields.Selection(
         string='gender type',
         selection=[('M', 'Male'),
                    #database,#views
                    ('F', 'Female'), ],
         required=False, )


    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()
    #
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

