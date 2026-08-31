{
    'name': 'AI-powered ERP Dashboard + Workflow Automation Suite',
    'version': '18.0.1.0.0',
    'category': 'Productivity/AI',
    'summary': 'AI-powered ERP dashboard and workflow automation suite',
    'description': """
        AI-powered ERP Dashboard + Workflow Automation Suite
        =====================================================
        Extends AI Operations Dashboard with ERP-focused metrics
        and automation rules for accounting, sales, inventory, and manufacturing.
    """,
    'author': 'SoftaiDev',
    'website': 'https://softaidev.pages.dev',
    'license': 'LGPL-3',
    'price': 649.99,
    'currency': 'USD',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
