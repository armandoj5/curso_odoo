# -*- coding: utf-8 -*-
{
    'name': "Modulo de desarrollo",

    'summary': """
        """,

    'description': """
        Aprendizaje de Odoo 12 por la empresa Quadit
        Para poder facturar es necesario tener la categoria de producto Facturacion Colegiatura.
    """,

    'author': "Quadit",
    'website': "https://www.quadit.mx/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Desarrollo',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/academy.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}