from odoo import fields, models, _, api


class GradeInEquipment(models.Model):
    _name = 'gradein.equipment'
    _description = 'Gradein Equipment'

    name = fields.Char(string="Name")
    image = fields.Image(string="Image")
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True)
    price = fields.Float(string="Price")