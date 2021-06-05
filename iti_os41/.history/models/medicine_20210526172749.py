from odoo import models, fields, api
# -*- coding: utf-8 - *-


class MedicineModel(models.Model):
    _name = 'medicine'
    _description = 'medicine'

    name = fields.Char()
    price = fields.Integer()
    description = fields.Text()
    manufacturer = fields.Char()
