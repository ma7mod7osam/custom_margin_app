import frappe
from frappe.model.document import Document

def apply_custom_margin(doc, method):
    for item in doc.items:
        item_valuation_rate = get_item_valuation_rate(item.item_code, item.warehouse)
        if item_valuation_rate and 'custom_client_margin_rate' in item:
            margin_rate = item.custom_client_margin_rate
            item.rate = item_valuation_rate + (item_valuation_rate * margin_rate / 100)
            frappe.msgprint(f"Item {item.item_code} rate updated to {item.rate}")

def get_item_valuation_rate(item_code, warehouse):
    valuation_rate = frappe.db.get_value("Bin", {"item_code": item_code, "warehouse": warehouse}, "valuation_rate")
    if valuation_rate:
        return valuation_rate
    else:
        frappe.throw(f"Could not find valuation rate for item {item_code} in warehouse {warehouse}")
