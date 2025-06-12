from odoo import models, fields

class School(models.Model):
    _name = 'students.school'
    _description = 'Schools'

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    phone = fields.Char(string="Phone")