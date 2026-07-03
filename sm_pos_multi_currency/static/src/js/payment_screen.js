/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { useState } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";

patch(PaymentScreen.prototype, {
    setup() {
        super.setup(...arguments);
        this.smState = useState({
            currencyId: false,
            amountIn: "",
        });
    },

    get smEnabled() {
        return this.pos.config.sm_enable_multi_currency && this.smCurrencies.length > 0;
    },

    get smCurrencies() {
        const companyCurrencyId = this.pos.currency.id;
        const allowed = (this.pos.config.sm_currency_ids || []).map((c) => c.id);
        return this.pos.models["res.currency"]
            .getAll()
            .filter((c) => c.id !== companyCurrencyId && allowed.includes(c.id));
    },

    get smSelectedCurrency() {
        return this.smState.currencyId
            ? this.pos.models["res.currency"].get(this.smState.currencyId)
            : null;
    },

    // res.currency.rate = units of this currency per 1 company currency unit
    get smRate() {
        const cur = this.smSelectedCurrency;
        return cur ? cur.rate : 0;
    },

    get smTotalInCurrency() {
        if (!this.smSelectedCurrency) {
            return 0;
        }
        return this.currentOrder.get_total_with_tax() * this.smRate;
    },

    smSelectCurrency(ev) {
        this.smState.currencyId = parseInt(ev.target.value) || false;
    },

    smUpdateAmount() {
        const cur = this.smSelectedCurrency;
        const amountIn = parseFloat(this.smState.amountIn);
        if (!cur || !amountIn) {
            this.dialog.add(AlertDialog, {
                title: _t("Multi Currency"),
                body: _t("Please add amount first or select currency."),
            });
            return;
        }
        let line = this.selectedPaymentLine;
        if (!line) {
            this.addNewPaymentLine(this.payment_methods_from_config[0]);
            line = this.selectedPaymentLine;
        }
        if (!line) {
            return;
        }
        const converted = amountIn / this.smRate;
        line.set_amount(converted);
        line.sm_currency_id = cur;
        line.sm_amount_currency = amountIn;
        this.smState.amountIn = "";
    },
});
