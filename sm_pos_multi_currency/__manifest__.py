# -*- coding: utf-8 -*-
{
    "name": "POS Multi Currency",
    "version": "19.0.1.1.0",
    "category": "Point of Sale",
    "summary": "Accept POS payments in multiple currencies: live conversion on the payment screen, change in foreign currency, foreign amount on receipt and backend order",
    "description": """
POS Multi Currency
==================

Accept Point of Sale payments in any active currency.

* Enable multi currency per POS and pick the allowed currencies
* Currency selector on the payment screen with live conversion rate
  (rates come from Accounting > Currencies)
* Enter the amount received in the foreign currency, the payment line is
  converted to the company currency automatically
* Change shown in both currencies so the cashier knows exactly how much
  foreign cash to hand back
* Amounts respect the currency symbol position and thousands separator
  (Rp 2,555,555 / 92 EUR)
* Payment lines show the original foreign amount next to the converted one
* Split one order across several currencies
* Receipt prints the foreign amount per payment line
* Foreign amount and currency stored on the payment in the backend order
  (Payments tab: Amount in Currency, Paid Currency)
* Accounting stays clean: journals and invoices remain in your company
  currency
    """,
    "author": "Steven Marp",
    "website": "https://apps.odoo.com/apps/modules/browse?author=Steven Marp",
    "license": "OPL-1",
    "images": ["static/description/banner.gif"],
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
    "price": 48.00,
    "currency": "USD",
}
