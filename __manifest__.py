{
    'name': "mrp_bom_check",
    'author': "mrp_bom_check",
    'category': 'stock',
    'summary': """mrp_bom_check""",
    'website': 'http://www.asceticbs.com',
    'license': 'AGPL-3',
    'description': """mrp_bom_check""",
    'version': '14.0.1.0',
    'depends': ['mrp','stock'],
    "data": [
        "views/stock_pickings.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
