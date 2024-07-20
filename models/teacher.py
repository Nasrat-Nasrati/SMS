from odoo import models, fields

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    teacher_id = fields.Char(string='Teacher ID', required=True, unique=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    course_ids = fields.One2many('school.course', 'teacher_id', string='Courses')
