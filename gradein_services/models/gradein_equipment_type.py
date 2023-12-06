from odoo import models, fields

class GradeInEquipmentType(models.Model):
    _name = 'gradein.equipment.type'
    _description = 'Grade In Equipment Type'

    name = fields.Char(string="Name")
    image = fields.Binary(string="Image")
    active = fields.Boolean(string="Active")
    question_ids = fields.Many2many('gradein.question', string="Questions")
