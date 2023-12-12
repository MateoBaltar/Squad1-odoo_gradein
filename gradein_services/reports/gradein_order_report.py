from odoo import models, fields,api


class GradeinOrderReport(models.AbstractModel):
    _name = 'report.gradein_services.gradein_order_report'
    _description = 'Gradein Service Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        if data and data.get('docs'):
            docids = data.get('docs')
        docs = self.env['gradein.order'].browse(docids)    
        return {
            'doc_ids': docids,
            'doc_model': 'gradein.order',
            'docs': docs,
        }