"""WDRA Electronic Negotiable Warehouse Receipt (e-NWR) & Commodity Lien Engine."""
from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List, Dict, Any, Optional

@dataclass
class StoredCommodityLot:
    receipt_id: str
    depositor_pan: str
    commodity_name: str         # SOYBEAN, CHANA, MUSTARD, WHEAT
    inward_gross_weight_mt: float
    moisture_pct_at_inward: float
    standard_shrinkage_allowance_pct: float = 1.5
    net_deliverable_weight_mt: float = 0.0
    pledge_bank_lien: str = ""  # Bank name if pledged
    status: str = "ISSUED_UNENCUMBERED"

class WDRAWarehouseReceiptEngine:
    def __init__(self, wdra_accreditation_no: str):
        self.wdra_accreditation_no = wdra_accreditation_no
        self.receipts: Dict[str, StoredCommodityLot] = {}

    def issue_enwr_receipt(self, lot: StoredCommodityLot) -> Dict[str, Any]:
        # Net deliverable after permissible moisture loss
        shrinkage_loss = round(lot.inward_gross_weight_mt * (lot.standard_shrinkage_allowance_pct / 100.0), 3)
        lot.net_deliverable_weight_mt = round(lot.inward_gross_weight_mt - shrinkage_loss, 3)
        self.receipts[lot.receipt_id] = lot

        return {
            "receipt_id": lot.receipt_id,
            "wdra_accreditation_no": self.wdra_accreditation_no,
            "inward_mt": lot.inward_gross_weight_mt,
            "net_deliverable_mt": lot.net_deliverable_weight_mt,
            "status": lot.status
        }

    def pledge_receipt_for_bank_loan(self, receipt_id: str, bank_name: str) -> Dict[str, Any]:
        if receipt_id not in self.receipts:
            raise ValueError(f"Receipt {receipt_id} not found.")
        lot = self.receipts[receipt_id]
        if lot.status != "ISSUED_UNENCUMBERED":
            raise ValueError(f"Receipt {receipt_id} cannot be pledged. Current status: {lot.status}")

        lot.pledge_bank_lien = bank_name
        lot.status = "PLEDGED_LIEN_MARKED"
        return {"receipt_id": receipt_id, "lien_marked_to": bank_name, "status": lot.status}
