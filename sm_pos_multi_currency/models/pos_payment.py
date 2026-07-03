# -*- coding: utf-8 -*-
from odoo import fields, models


class PosPayment(models.Model):
    _inherit = "pos.payment"

    sm_currency_id = fields.Many2one(
        "res.currency", string="Paid Currency",
        help="Foreign currency the customer actually paid in.")
    sm_amount_currency = fields.Float(
        string="Amount in Currency",
        help="Amount received in the foreign currency.")
