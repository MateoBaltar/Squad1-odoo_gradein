from odoo import models, fields


class GradeinRejectMotive(models.Model):
    _name = 'gradein.reject.motive'
    _rec_name = 'name'
    _description = 'Gradein Reject Motive'
    
    name = fields.Char(string="Name")
    active = fields.Boolean(string="Active")
    
    
 