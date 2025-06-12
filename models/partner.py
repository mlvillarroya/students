from odoo import api, models, fields
from datetime import date

class ResPartner(models.Model):
    _inherit = 'res.partner'
    lastname = fields.Char(string="Last name")
    birthdate = fields.Date(string="Birthdate")
    age = fields.Integer(
        string="Edad",
        compute='_compute_age',
        store=False,  # No se almacena, se calcula al vuelo
    )

    is_student = fields.Boolean(string="Is Student")
    is_family_member = fields.Boolean(string="Is relative")

    relatives_ids = fields.Many2many(
        'res.partner',
        relation='student_relative_rel',
        column1='student_id',
        column2='relative_id',
        string="Relatives",
        domain=[('is_family_member', '=', True)]
    )

    student_ids = fields.Many2many(
        'res.partner',
        compute='_compute_student_ids',
        string="Associated students",
        domain=[('is_student', '=', True)]
    )

    meeting_ids = fields.One2many(
        'students.meeting',
        'student_id',
        string="Meetings"
    )

    school_id = fields.Many2one("students.school", string="School")

    @api.depends('relatives_ids')
    def _compute_student_ids(self):
        for partner in self:
            partner.student_ids = self.search([
                ('relatives_ids', 'in', partner.id),
                ('is_student', '=', True)
            ])

    @api.depends('birthdate')
    def _compute_age(self):
        today = date.today()
        for partner in self:
            if partner.birthdate:
                birthdate = fields.Date.from_string(partner.birthdate)
                partner.age = today.year - birthdate.year - (
                        (today.month, today.day) < (birthdate.month, birthdate.day)
                )
            else:
                partner.age = 0

    is_customer = fields.Boolean(
        string="Is Customer",
        compute='_compute_is_customer',
        inverse='_inverse_is_customer',
        store=False,  # No se guarda en la base de datos
    )

    @api.depends('customer_rank')
    def _compute_is_customer(self):
        for partner in self:
            partner.is_customer = partner.customer_rank == 1

    def _inverse_is_customer(self):
        for partner in self:
            partner.customer_rank = 1 if partner.is_customer else 0

    @api.depends('name', 'lastname')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.name} {rec.lastname}" if rec.lastname else rec.name