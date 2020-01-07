{
    'name': 'KIJABE-PURCHASE-EXT',
    'description': 'Extend purchase module to add custom modifications for Kijabe odoo implementation',
    'author': 'Mupagasi Jean Paul',
    'depends': ['purchase','stock'],
    'summary':'Extension of Purchase module',
    'website':'https://cure.org/',
    'data': 
        [
            'security/purchase_groups.xml',
            'security/ir.model.access.csv',
            'views/kijabe_purchase_ext_view.xml',
            'views/internal_requisition_view.xml',
            'views/external_requisition_view.xml',
            'report/report.xml'

        ],
}
