# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "wdra_enwr_warehouse"
app_title = "Frappe Cold Storage Wdrb Negotiable Warehouse Receipt"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Cold Storage Wdrb Negotiable Warehouse Receipt - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/wdra_enwr_warehouse/css/wdra_enwr_warehouse.bundle.css"
app_include_js = "/assets/wdra_enwr_warehouse/js/wdra_enwr_warehouse.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Frappe Cold Storage Wdrb Negotiable Warehouse Receipt Entry": {
        "validate": "wdra_enwr_warehouse.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "wdra_enwr_warehouse.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "wdra_enwr_warehouse.tasks.hourly_sync"
    ],
    "daily": [
        "wdra_enwr_warehouse.tasks.daily_reconciliation"
    ],
    "weekly": [
        "wdra_enwr_warehouse.tasks.weekly_digest"
    ]
}
