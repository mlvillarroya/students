# -*- coding: utf-8 -*-
# from odoo import http


# class Students(http.Controller):
#     @http.route('/students/students', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/students/students/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('students.listing', {
#             'root': '/students/students',
#             'objects': http.request.env['students.students'].search([]),
#         })

#     @http.route('/students/students/objects/<model("students.students"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('students.object', {
#             'object': obj
#         })

