# -*- coding: utf-8 -*-
from odoo import http

class BasicApp(http.Controller):
    @http.route('/basic_app/basic_app/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/basic_app/basic_app/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('basic_app.listing', {
            'root': '/basic_app/basic_app',
            'objects': http.request.env['basic_app.basic_app'].search([]),
        })

    @http.route('/basic_app/basic_app/objects/<model("basic_app.basic_app"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('basic_app.object', {
            'object': obj
        })