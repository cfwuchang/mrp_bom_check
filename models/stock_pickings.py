
from odoo import api,fields,models,_
class StockPickings(models.Model):
    _inherit = "mrp.bom"

    check=fields.Char(string=u'查询值')
    check_list=fields.One2many('mrp.bom.line', 'bom_id',string=u'查询行')

    @api.onchange('check')
    def _get_check_list(self):
        id=[]
        for i in self.bom_line_ids:
            if self.check in i.product_id.name:
                id.append(i.id)
        self.check_list = [(6, 0, id)]