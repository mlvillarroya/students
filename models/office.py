from odoo import models, fields

class Office(models.Model):
    _name = 'students.office'
    _description = 'Offices'

    name = fields.Char(string="Name")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")