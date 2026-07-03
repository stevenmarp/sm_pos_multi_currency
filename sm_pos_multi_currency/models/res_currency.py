# -*- coding: utf-8 -*-
from odoo import api, models


class ResCurrency(models.Model):
    _inherit = "res.currency"

    @api.model
    def _load_pos_data_domain(self, data, config):
        domain = super()._load_pos_data_domain(data, config)
        if config.sm_enable_multi_currency and config.sm_currency_ids:
            loaded = {config.currency_id.id, config.company_id.currency_id.id}
            for leaf in domain:
                value = leaf[2]
                loaded.update(value if isinstance(value, (list, tuple)) else [value])
            return [("id", "in", list(loaded | set(config.sm_currency_ids.ids)))]
        return domain
