import unittest
from wdra_enwr_warehouse.engine import StoredCommodityLot, WDRAWarehouseReceiptEngine

class TestWDRAWarehouseReceiptEngine(unittest.TestCase):
    def setUp(self):
        self.engine = WDRAWarehouseReceiptEngine("WDRA-WH-MP-INDORE-044")

    def test_enwr_shrinkage_and_issuance(self):
        lot = StoredCommodityLot(
            receipt_id="eNWR-CCRL-2026-091", depositor_pan="AAAFK1234Z",
            commodity_name="SOYBEAN", inward_gross_weight_mt=100.0,
            moisture_pct_at_inward=12.5, standard_shrinkage_allowance_pct=1.5
        )
        res = self.engine.issue_enwr_receipt(lot)
        self.assertEqual(res["net_deliverable_mt"], 98.5)
        self.assertEqual(res["status"], "ISSUED_UNENCUMBERED")

    def test_bank_lien_pledge(self):
        lot = StoredCommodityLot("eNWR-CCRL-2026-092", "AAAFK5678M", "WHEAT", 50.0, 11.0)
        self.engine.issue_enwr_receipt(lot)
        res = self.engine.pledge_receipt_for_bank_loan("eNWR-CCRL-2026-092", "State Bank of India")
        self.assertEqual(res["status"], "PLEDGED_LIEN_MARKED")
        self.assertEqual(res["lien_marked_to"], "State Bank of India")

if __name__ == "__main__":
    unittest.main()
