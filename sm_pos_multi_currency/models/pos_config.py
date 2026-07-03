# -*- coding: utf-8 -*-
from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    sm_enable_multi_currency = fields.Boolean(
        string="Enable Multi Currency",
        help="Show a currency selector on the POS payment screen to accept "
             "payments in foreign currencies.")
    sm_currency_ids = fields.Many2many(
        "res.currency", string="Allowed Currencies",
        help="Currencies the cashier can accept on the payment screen.")
