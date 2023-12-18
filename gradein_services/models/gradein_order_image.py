from odoo import fields, models, _

class GradeInOrderImage(models.Model):
    _name = "gradein.order.image"
    _rec_name = "name"
    _order = "name ASC"
    _description = "Order Image"
    _inherit = ['image.mixin']
    _order = 'sequence, id'

    name = fields.Char("Name", required=True)
    sequence = fields.Integer(default=1)
    image_1920 = fields.Image(required=True)
    grade_order_id = fields.Many2one(
        'gradein.order', "GradeIn Order", ondelete='cascade')
