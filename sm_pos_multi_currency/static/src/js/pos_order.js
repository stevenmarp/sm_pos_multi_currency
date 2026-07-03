/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PosOrder } from "@point_of_sale/app/models/pos_order";

patch(PosOrder.prototype, {
    export_for_printing(baseUrl, headerData) {
        const result = super.export_for_printing(...arguments);
        this.payment_ids.forEach((pl, i) => {
            if (pl.sm_currency_id && pl.sm_amount_currency && result.paymentLines[i]) {
                result.paymentLines[i].name += ` (${pl.sm_amount_currency}${pl.sm_currency_id.symbol})`;
            }
        });
        return result;
    },
});
