from odoo import fields, models, _, api


class GradeInEquipment(models.Model):
    _name = 'gradein.equipment'
    _description = 'Gradein Equipment'

    name = fields.Char(string="Name")
    image = fields.Image(string="Imagen")
    description = fields.Text(string="Descripción")
    active = fields.Boolean(string="Activo", default=True)
    price = fields.Float(string="Precio")