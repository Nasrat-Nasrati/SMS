from odoo import models, fields, api

class Fees(models.Model):
    _name = 'school.fees'
    _description = 'Fees'

    student_id = fields.Many2one('school.student', string='Student', required=True)
    course_id = fields.Many2one('school.course', string='Course', required=True)
    month = fields.Selection([
        ('january', 'January'),
        ('february', 'February'),
        ('march', 'March'),
        ('april', 'April'),
        ('may', 'May'),
        ('june', 'June'),
        ('july', 'July'),
        ('august', 'August'),
        ('september', 'September'),
        ('october', 'October'),
        ('november', 'November'),
        ('december', 'December')
    ], string='Month', required=True)
    year = fields.Integer(string='Year', required=True)
    amount = fields.Float(string='Amount', required=True)
    paid = fields.Boolean(string='Paid', default=False)

    @api.model
    def create(self, vals):
        record = super(Fees, self).create(vals)
        # Add any additional functionality here if needed
        return record
