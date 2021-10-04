# -*- coding: utf-8 -*-
# from odoo import http


# class FleetModule(http.Controller):
#     @http.route('/fleet_module/fleet_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fleet_module/fleet_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fleet_module.listing', {
#             'root': '/fleet_module/fleet_module',
#             'objects': http.request.env['fleet_module.fleet_module'].search([]),
#         })

#     @http.route('/fleet_module/fleet_module/objects/<model("fleet_module.fleet_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fleet_module.object', {
#             'object': obj
#         })
