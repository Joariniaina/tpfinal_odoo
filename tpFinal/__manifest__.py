{
    'name': 'Gestion des Ventes Personnalisée',
    'version': '1.0',
    'category': 'Sales',
    'author': 'Votre nom',
    'depends': ['sale', 'hr', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'security/security_group.xml',
        'views/sale_order_views.xml',
        'views/employee_form.xml',
        'report/invoice_report.xml',
        'menu/sale_order_actions.xml',
        'menu/sale_order_menu.xml',
    ],
    'installable': True,
    'application': True,
}
