# -*- coding: utf-8 -*-
{
    'name': "ITI Intake 41",

    'summary': """
       Demo Module""",

    'description': """
       Long Demo Module
    """,

    'author': "ITI",
    'website': "http://www.iti.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/medicine.xml',
        'views/orderlines.xml',
        'views/order.xml',
        'views/templates.xml',
        'reports/report_view.xml',
        'wizards/change_date_wizard_view',

    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
