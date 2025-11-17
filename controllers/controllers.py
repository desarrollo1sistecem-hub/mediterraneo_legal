# -*- coding: utf-8 -*-
# from odoo import http


# class MediterraneoLegal(http.Controller):
#     @http.route('/mediterraneo_legal/mediterraneo_legal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mediterraneo_legal/mediterraneo_legal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mediterraneo_legal.listing', {
#             'root': '/mediterraneo_legal/mediterraneo_legal',
#             'objects': http.request.env['mediterraneo_legal.mediterraneo_legal'].search([]),
#         })

#     @http.route('/mediterraneo_legal/mediterraneo_legal/objects/<model("mediterraneo_legal.mediterraneo_legal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mediterraneo_legal.object', {
#             'object': obj
#         })
