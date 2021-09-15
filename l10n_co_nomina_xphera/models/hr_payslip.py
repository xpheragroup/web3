from datetime import date, datetime
from odoo import api, fields, models, _

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    prima = fields.Boolean(string='Pago de Prima')

    @api.onchange('date_from','date_to')
    def es_prima(self):
        year = datetime.now().year

        primera_prima = self.env['hr.rule.parameter.value'].search([('rule_parameter_id.code','=','FPP')],limit=1).parameter_value
        date_primera_prima = datetime.strptime(primera_prima + '/' + str(year), '%d/%m/%Y').date()
        segunda_prima = self.env['hr.rule.parameter.value'].search([('rule_parameter_id.code','=','FSP')],limit=1).parameter_value
        date_segunda_prima = datetime.strptime(segunda_prima + '/' + str(year), '%d/%m/%Y').date()

        if (self.date_from <= date_primera_prima <= self.date_to) or (self.date_from <= date_segunda_prima <= self.date_to):
            self.prima = True
        else:
            self.prima = False