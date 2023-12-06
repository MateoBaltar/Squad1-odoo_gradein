from odoo import fields, models, _, api


class GradeinQuestion(models.Model):
    _name = 'gradein.question'
    _description = 'Gradein Question'

    name = fields.Char(string="Name")
    active = fields.Boolean(string="Active", default=True)
    equipment_type_ids = fields.Many2many('gradein.equipment', string="Equipment Type")
    answer_ids = fields.Many2many('gradein.answer', string="Answers")