# -*- coding: utf-8 -*-
from odoo import models, fields, api

# This class inherit purchase.order model by
# 1) Adding new fields and modifying fields display name
# 2) Send email notification to managers of purchase order need to be approved


class purchase(models.Model):
    _inherit = 'purchase.order'
    # Add new field
    x_division = fields.Selection(
        [
            ('MED', 'MED'),
            ('NUR', 'NUR'),
            ('CCK', 'CCK'),
            ('SSD', 'SSD'),
            ('HRD', 'HRD'),
            ('FIN', 'FIN'),
            ('OPS', 'OPS')
        ],
        string=u'Division')
    # Modify existing fields display name
    partner_id = fields.Many2one(string=u'Supplier')
    partner_ref = fields.Char(string=u'Supplier Code')

    # Confirm order and send notification to managers
    @api.multi
    def button_confirm(self):
        super(purchase, self).button_confirm()  # confirm order
        # get current url
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        if self.state == 'to approve':
            # get groups of 'Manager' in res.groups
            groups = self.env['res.groups'].search([['name', '=', "Manager"]])
            for group in groups:
                users = self.env["res.users"].search([['groups_id', '=', group.id], [
                    'active', '=', True]])  # get active users who belong in the group ids

            for user in users:
                # call the method to send emails
                self._send_mail(user.login, self[0].name, user.name,base_url)
        return True

    # Send email
    def _send_mail(self, recipient, po, name,url):
        mail_pool = self.env['mail.mail']
        values = {}
        values.update({'subject': 'Purchase Order #' +
                       po + ' waiting your approval'})
        values.update({'email_from': "odoomail.service@gmail.com"})
        values.update({'email_to': recipient})
        values.update({'body_html':
                       'To Manager ' + name + ',<br>'
                       + 'LPO No. ' + po + ' has been created and requires your approval. You can find the details to approve here. '+url})

        msg_id = mail_pool.create(values)
        if msg_id:
            result = msg_id.send()
        return True
