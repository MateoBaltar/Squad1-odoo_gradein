{
    "name": "Odoo Gradein",
    "version": "1.0",
    "author": "Alkemy",
    "depends": ["base"],
    "installable": True,
    "application": True,
    "data": [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/gradein_answer_view.xml',
        'views/menu_services.xml',
        'views/gradein_question_view.xml',
    ]
}