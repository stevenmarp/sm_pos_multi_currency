# -*- coding: utf-8 -*-
{
    "name": "POS Multi Currency",
    "version": "19.0.1.0.0",
    "category": "Point of Sale",
    "summary": "Accept POS payments in multiple currencies with live conversion on the payment screen",
    "description": """
POS Multi Currency
==================

Accept Point of Sale payments in any active currency.

* Enable multi currency per POS and pick the allowed currencies
* Currency selector on the payment screen with live conversion rate
* Enter the amount received in the foreign currency, the payment line is
  converted to the company currency automatically
* Payment lines show the original foreign amount next to the converted one
* Receipt prints the foreign amount per payment line
* Foreign amount and currency stored on the payment in the backend order
    """,
    "author": "Steven Marp",
    "website": "https://apps.odoo.com/apps/modules/browse?author=Steven Marp",
    "license": "OPL-1",
    "depends": ["point_of_sale"],
    "data": [
        "views/res_config_settings_views.xml",
        "views/pos_order_views.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "sm_pos_multi_currency/static/src/js/*",
            "sm_pos_multi_currency/static/src/xml/*",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
    "price": 49.90,
    "currency": "USD",
}
