from odoo import models, fields


class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    student_id = fields.Char(string='Student ID', required=True, unique=True)
    date_of_birth = fields.Date(string='Date of Birth')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    courses_ids = fields.Many2many('school.course', string='Courses')
    fees_ids = fields.One2many('school.fees', 'student_id', string='Fees')
