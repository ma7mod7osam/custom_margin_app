import frappe
from frappe.model.document import Document

def apply_custom_margin(doc, method):
    customer_margin_rate = frappe.db.get_value("Customer", doc.customer, "custom_client_margin_rate")
    if not customer_margin_rate:
        frappe.throw(f"Customer {doc.customer} does not have a custom margin rate set.")
    
    for item in doc.items:
        item_valuation_rate = get_item_valuation_rate(item.item_code, item.warehouse)
        if item_valuation_rate:
            item.rate = item_valuation_rate + (item_valuation_rate * customer_margin_rate / 100)
            frappe.msgprint(f"Item {item.item_code} rate updated to {item.rate} based on customer margin rate of {customer_margin_rate}%")

def get_item_valuation_rate(item_code, warehouse):
    valuation_rate = frappe.db.get_value("Bin", {"item_code": item_code, "warehouse": warehouse}, "valuation_rate")
    if valuation_rate:
        return valuation_rate
    else:
        frappe.throw(f"Could not find valuation rate for item {item_code} in warehouse {warehouse}")
