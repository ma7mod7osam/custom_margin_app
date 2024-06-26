# custom_margin_app/hooks.py

app_name = "custom_margin_app"
app_title = "Custom Margin App"
app_publisher = "ma7mod7osam"
app_description = "An app to apply custom margin rate on items"
app_email = "ma7mod7osam@gmail.com"
app_license = "MIT"

# No frontend assets included, so no need to specify app_include_js or app_include_css


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