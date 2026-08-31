from odoo import models, fields


class ErpKpi(models.Model):
    _name = 'ai.erp.kpi'
    _description = 'AI ERP KPI'
    _order = 'sequence, id'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    note = fields.Text(string='Notes')
