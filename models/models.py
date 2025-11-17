# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class mediterraneo_legal(models.Model):
#     _name = 'mediterraneo_legal.mediterraneo_legal'
#     _description = 'mediterraneo_legal.mediterraneo_legal'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
