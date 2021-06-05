# -*- coding: utf-8 -*-
from odoo import http


# class ItiOs41(http.Controller):
#     @http.route('/iti_os41/iti_os41/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iti_os41/iti_os41/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iti_os41.listing', {
#             'root': '/iti_os41/iti_os41',
#             'objects': http.request.env['iti_os41.iti_os41'].search([]),
#         })

#     @http.route('/iti_os41/iti_os41/objects/<model("iti_os41.iti_os41"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iti_os41.object', {
#             'object': obj
#         })


import json
import logging

logger = logging.getLogger(__name__)


class ItiOs41(http.Controller):
    # @http.route('/iti_os41/iti_os41/', auth='public')
    # def index(self, **kw):
    #     return "Hello, world"

    @http.route('/iti_os41/objects/', auth='public', type='json')
    def list(self, **kw):
        result = http.request.env['medicine'].search_read(
            [], fields=['name', 'price', 'description', 'manufacturer'])
        logger.info(result)
        return json.dumps(result)
        # return http.request.render('iti_os41.listing', {
        #     'root': '/iti_os41/iti_os41',
        #     'objects': http.request.env['order'].search([]),
        # })
