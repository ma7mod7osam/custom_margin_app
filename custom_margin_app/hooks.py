# custom_margin_app/hooks.py

doc_events = {
    "Quotation": {
        "before_save": "custom_margin_app.custom_margin_app.doctype.custom_margin_app.custom_margin_app.apply_custom_margin"
    },
    "Sales Order": {
        "before_save": "custom_margin_app.custom_margin_app.doctype.custom_margin_app.custom_margin_app.apply_custom_margin"
    },
    "Sales Invoice": {
        "before_save": "custom_margin_app.custom_margin_app.doctype.custom_margin_app.custom_margin_app.apply_custom_margin"
    }
}
