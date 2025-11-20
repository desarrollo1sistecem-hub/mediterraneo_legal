from odoo import models, fields

class LegalTaskType(models.Model):
    _name = 'legal.task.type'
    _description = 'Tipo de tarea legal'
    _order = 'sequence, name'

    name = fields.Char('Nombre', required=True)
    code = fields.Char('Código interno')
    sequence = fields.Integer('Secuencia', default=10)
    active = fields.Boolean('Activo', default=True)
    description = fields.Text('Descripción')
