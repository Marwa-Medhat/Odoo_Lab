from odoo import models, fields, api
-*- coding: utf-8 - *-


class iti_os41(models.Model):
    _name = 'iti_os41.iti_os41'
    _description = 'iti_os41.iti_os41'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
