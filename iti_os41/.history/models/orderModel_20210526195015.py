from odoo import models, fields, api
# -*- coding: utf-8 - *-


class orderModel(models.Model):
    # _name = 'order'
    _name = 'order'

    # one to many
    # inverse field order id
    relationorderid = fields.One2many('orderlines', inverse_name='order_id')
    # order_Lines = fields.One2many('orderLines', related_field)
    name = fields.Char()
    total = fields.Float()
    # total = fields.Float(compute="_value_pc", store=True)
    date = fields.Date()

    # asm al field 2li bysm3 lma aktb feh hya al subtotal
    @api.depends('sub_total')
    def _value_pc(self):
        for record in self:
            record.total = float(record.sub_total)  # from model Order


# kda na2s y7sb al total mn al subtotal
# a3ml al custmor bta3t al res.partner
#
