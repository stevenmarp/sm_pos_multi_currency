/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PosPayment } from "@point_of_sale/app/models/pos_payment";

patch(PosPayment.prototype, {
    export_for_printing() {
        const result = super.export_for_printing(...arguments);
        if (this.sm_currency_id && this.sm_amount_currency) {
            result.name += ` (${this.sm_amount_currency}${this.sm_currency_id.symbol})`;
        }
        return result;
    },
});
