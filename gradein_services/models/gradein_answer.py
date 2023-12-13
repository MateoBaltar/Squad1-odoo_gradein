from odoo import fields, models, _, api

class GradeinAnswer(models.Model):
    _name = "gradein.answer"
    _rec_name = "name"
    _description = "Gradein Answer"
    
    name = fields.Char(string="Name")
    active = fields.Boolean(string="Active", default=True)
    price_reduction = fields.Float(string="Reduce the price by")
    
    
    
    
    
    
    