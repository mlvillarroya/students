from odoo import models, fields, api

class Meeting(models.Model):
    _name = 'students.meeting'
    _description = 'Meetings with students'

    student_id = fields.Many2one('res.partner', string="Student", domain=[('is_student', '=', True)])
    date = fields.Datetime(string="Date")
    duration = fields.Float(string="Duration (hours)", default=1.0)
    subject = fields.Char(string="Subject")
    notes = fields.Text(string="Notes")

    @api.depends('student_id')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.student_id.name} {rec.student_id.lastname}" if rec.student_id.lastname else rec.student_id.name

    def save_and_new(self):
        # Guardar los valores actuales
        current_values = {
            'subject': self.subject,
            'duration': self.duration,
            'student_id': self.student_id.id
        }

        # Crear acción para abrir nuevo formulario
        return {
            'type': 'ir.actions.act_window',
            'name': 'Duplicate meeting',
            'res_model': 'students.meeting',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                'default_subject': current_values.get('subject'),
                'default_duration': current_values.get('duration'),
                'default_student_id': current_values.get('student_id'),
            }
        }

    def save_and_close(self):
        # Crear acción para abrir nuevo formulario
        return {
            'type': 'ir.actions.act_window',
            'name': 'Open calendar',
            'res_model': 'students.meeting',
            'view_mode': 'calendar',
            'target': 'current'
        }