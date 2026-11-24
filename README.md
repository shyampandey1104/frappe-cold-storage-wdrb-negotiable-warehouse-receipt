# Frappe WDRA Electronic Negotiable Warehouse Receipt (e-NWR) & Commodity Lien Engine

[![Frappe Framework](https://img.shields.io/badge/Frappe-v15.x-blue.svg)](https://frappeframework.com/)
[![WDRA Certified](https://img.shields.io/badge/WDRA-e--NWR%20Accredited-gold.svg)]()
[![Agri Commodity](https://img.shields.io/badge/Commodity-Pledge%20Financing-emerald.svg)]()
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 📌 Executive Overview & Real-World Client Problem

Agri-commodity warehouse operators accredited by the **Warehousing Development and Regulatory Authority (WDRA)** handle millions of metric tons of agricultural commodities (grains, pulses, oilseeds, spices).

Key operational pain points:
1. **Pledge Financing Lien Disputes:** Farmers and commodity traders require accredited **Electronic Negotiable Warehouse Receipts (e-NWR)** through repositories (CCRL/NERL) to obtain low-interest post-harvest bank loans. Managing bank lien marks and release holds without digital verification risks double-pledging fraud.
2. **Moisture & Storage Shrinkage Norms:** Commodities lose weight over months of storage due to moisture loss. Failure to apply standard WDRA permissible shrinkage allowances leads to delivery shortfalls during stock release.
3. **Assaying & Quality Grade Drift:** Stored stock quality parameters (foreign matter, damaged grains, insect infestation) must be audited periodically to adjust delivery valuations.

This Frappe application implements an enterprise e-NWR warehouse receipt manager with automated shrinkage computation and bank lien workflows.

---

## 🏛️ System Architecture Flow

```mermaid
flowchart TD
    A["Farmer / Trader Commodity Inward at Warehouse"] -->|Lab Assaying (Moisture%, Impurities)| B["WDRA Inward Quality Gate"]
    B -->|Calculate Standard Moisture Shrinkage Allowance| C["Net Deliverable Weight Calculator"]
    C -->|Issue Certified Digital Receipt| D["Electronic Negotiable Warehouse Receipt (e-NWR)"]
    D -->|Depositor Requests Bank Loan| E{"Bank Lien Marking Workflow"}
    E -->|Lien Marked to Scheduled Commercial Bank| F["Stock Locked: Transfer / Delivery Prohibited"]
    E -->|Unencumbered| G["Free Trading / Physical Delivery Authorized"]
    F -->|Bank Issues Loan Repayment NOC| H["Release Lien: e-NWR Unencumbered"]
    H -->|Issue Delivery Order| I["Physical Commodity Outward Dispatch"]
```

---

## 🚀 Key Engineering Capabilities

- **Automated WDRA Shrinkage Calculator:** Applies statutory moisture loss allowances ensuring deliverable stocks match warehouse physical inventory.
- **Bank Lien Pledge Management:** Marks, tracks, and releases bank pledge encumbrances preventing fraudulent stock withdrawals.
- **Assaying Quality Parameter Matrix:** Records foreign matter, broken grains, moisture, and grading certificates.
- **CCRL / NERL Repository Formatter:** Prepares standardized XML/JSON payloads for statutory electronic warehouse repositories.

---

## 📂 Frappe DocType Schema & Data Structure

```text
wdra_enwr_warehouse/
├── wdra_enwr_warehouse_core/
│   ├── doctype/
│   │   ├── stored_commodity_lot/
│   │   │   ├── stored_commodity_lot.json
│   │   │   ├── stored_commodity_lot.py
│   │   │   └── stored_commodity_lot.js
│   │   └── enwr_pledge_record/
│   │       └── enwr_pledge_record.json
│   └── workspace/
│       └── wdra_enwr_warehouse_workspace/
│           └── wdra_enwr_warehouse_workspace.json
```

---

## ⚡ Frappe Hooks & Whitelisted APIs

- **REST Endpoint:** `POST /api/method/wdra_enwr_warehouse.api.issue_enwr_receipt`
- **Whitelisted Method:** `@frappe.whitelist() def pledge_receipt_for_bank_loan(receipt_id, bank_name)`
- **Hooks Event:** `on_submit` of `Stock Entry` (Material Receipt) auto-generates commodity lots.

---

## 🛠️ Installation & Bench Setup

```bash
bench get-app https://github.com/shyampandey1104/frappe-cold-storage-wdrb-negotiable-warehouse-receipt
bench --site erp.yourdomain.com install-app wdra_enwr_warehouse
bench --site erp.yourdomain.com migrate
python3 -m unittest discover tests
```

---

## 📄 License
MIT License. Built for Cold Storage Chains, WDRA Accredited Warehouses, and Agri-Fintech Pledging Lenders.
