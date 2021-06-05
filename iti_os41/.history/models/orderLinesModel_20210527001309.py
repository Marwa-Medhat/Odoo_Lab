from odoo import models, fields, api
# -*- coding: utf-8 - *-


class orderLinesModel(models.Model):
    _name = 'orderlines'
    _description = 'orderlines'

    orderlinename = fields.Many2one('medicine')
    unit_price = fields.Float(compute="_value_pc", store=True)
    # unit_price = fields.Float()
    quantity = fields.Float()
    sub_total = fields.Float()
    order_id = fields.Many2one('order')

    @api.depends('price')
    # @api.onchange('price')
    def _value_pc(self):
        for record in self:
            # price in Medicine Model
            record.unit_price = float(record.orderlinename.price)
