/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PosPayment } from "@point_of_sale/app/models/pos_payment";

patch(PosPayment.prototype, {
    get smForeignLabel() {
        if (!this.sm_currency_id || !this.sm_amount_currency) {
            return "";
        }
        const cur = this.sm_currency_id;
        const amount = Number(this.sm_amount_currency).toLocaleString(undefined, {
            minimumFractionDigits: 0,
            maximumFractionDigits: cur.decimal_places,
        });
        return cur.position === "before" ? `${cur.symbol} ${amount}` : `${amount} ${cur.symbol}`;
    },

    export_for_printing() {
        const result = super.export_for_printing(...arguments);
        if (this.smForeignLabel) {
            result.name += ` (${this.smForeignLabel})`;
        }
        return result;
    },
});
