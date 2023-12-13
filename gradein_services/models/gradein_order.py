from odoo import fields, models, _, api

class GradeinOrder(models.Model):
    _name = 'gradein.order'
    _description = 'GradeIn Order'

    name = fields.Char(string='Name')
    date = fields.Date(string='Date')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected')],
                             string='Status', default='draft')
    equipment_id = fields.Many2one('gradein.equipment', string='Equipment')
    imei = fields.Char(string='IMEI')
    image_ids = fields.Many2one('ir.attachment', string='Images')
    partner_id = fields.Many2one('res.partner', string='Client')
    reject_motive_id = fields.Many2one('gradein.reject.motive', string='Reason for rejection')
    price = fields.Float(string='Amount to pay')
    review = fields.Text(string='Evaluation Summary')
    answer_ids = fields.Many2one('gradein.answer', string='Answers')
    question_ids = fields.Many2one('gradein.question', string='Questions')
