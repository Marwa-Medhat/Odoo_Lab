from odoo import models, fields, api
# -*- coding: utf-8 - *-


class orderModel(models.Model):
    # _name = 'order'
    _name = 'order'

    # _inherit = 'res.partner'

    partner_id = fields.Many2one('res.partner', string="Customer")
    # one to many
    # inverse field order id
    relationorderid = fields.One2many('orderlines', inverse_name='order_id')
    # order_Lines = fields.One2many('orderLines', related_field)
    name = fields.Char()
    # total = fields.Float()
    total = fields.Float(compute="_value_pc")
    date = fields.Date()

    # asm al field 2li bysm3 lma aktb feh hya al subtotal
    @api.onchange('value')
    def _value_pc(self):
        for record in self:
            record.total = 0
            for orderline in record.relationorderid:
                record.total = record.total + orderline.sub_total  # from model Order
