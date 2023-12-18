{
    "name": "Odoo Gradein",
    "version": "1.0",
    "author": "Alkemy",
    "depends": ["base", "web"],
    "installable": True,
    "application": True,
    "data": [
        'security/groups.xml',
        'reports/gradein_order_reports_view.xml',
        'security/ir.model.access.csv',
        'views/gradein_answer_view.xml',
        'views/gradein_question_view.xml',
        'views/equipment_type_view.xml',
        'views/gradein_equipment_view.xml',
        'views/gradein_reject_motive_view.xml',
        'views/gradein_order_view.xml',
        'views/gradein_orders_image_views.xml',
        'views/menu_services.xml',  
    ],
    "assets": {
        "web.assets_backend": [
            "gradein_services/static/src/css/gradein_services.css",
        ],
    },
}
