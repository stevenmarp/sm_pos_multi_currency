# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    pos_sm_enable_multi_currency = fields.Boolean(
        related="pos_config_id.sm_enable_multi_currency", readonly=False)
    pos_sm_currency_ids = fields.Many2many(
        related="pos_config_id.sm_currency_ids", readonly=False)
