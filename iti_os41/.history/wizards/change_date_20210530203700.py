from odoo import fields,models,api

class ChangeDateWizard(models.TransientModel):
    _name = 'lab2.change.date'
    _description = 'lab2.change.date'

    Date = fields.Date()

    def action_change_date(self):
        # make sure hold only one record
        # self.ensure_one()
        active_id=self.env['lab2.order'].browse(self._context.get('active_ids')).copy()
        # active_id.write({'Date':self.Date})
        # active_id= self.env.context.get('active_id')
        # active_id.copy()