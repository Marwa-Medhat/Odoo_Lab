from odoo import models, fields, api
# -*- coding: utf-8 - *-


class orderLinesModel(models.Model):
    _name = 'orderlines'
    _description = 'orderlines'

    orderlinename = fields.Many2one('medicine')
    unit_price = fields.Float(compute="_value_pc", store=True)
    # unit_price = fields.Float()
    quantity = fields.Float()
    sub_total = fields.Float(compute="_value_pc_2", store=True)
    order_id = fields.Many2one('order')

    # @api.depends('price')
    @api.onchange('value')
    def _value_pc(self):
        for record in self:
            # price in Medicine Model
            record.unit_price = float(record.orderlinename.price)
    # @api.onchange('orderlinename')

    def _value_pc_2(self):
        for record in self:
            record.sub_total = (float(record.quantity)) * \
                (float(record.unit_price))  # from model Order
