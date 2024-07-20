from odoo import models, fields

class Class(models.Model):
    _name = 'school.class'
    _description = 'Class'

    name = fields.Char(string='Name', required=True)
    class_code = fields.Char(string='Class Code', required=True, unique=True)
    course_id = fields.Many2one('school.course', string='Course', required=True)
    teacher_id = fields.Many2one('school.teacher', string='Teacher', required=True)
    student_ids = fields.Many2many('school.student', string='Students')
    schedule = fields.Text(string='Schedule')
