from odoo import fields, models

class MgmtsystemAction(models.Model):
    _inherit = 'mgmtsystem.action'

    project_id = fields.Many2one(
        'project.project',
        string='Obra',
        help='Obra relacionada con esta acción legal.'
    )

    agreement_id = fields.Many2one(
        'agreement',
        string='Acuerdo / Contrato'
    )

    is_legal = fields.Boolean(
        string='Acción legal',
        default=False,
        help='Marca esta acción como perteneciente al área legal.'
    )

    legal_task_type_id = fields.Many2one(
        'legal.task.type',
        string='Tipo de tarea legal'
    )

    partner_id = fields.Many2one(
        'res.partner',
        string='Contacto relacionado',
        help='Contacto asociado a esta acción legal.'
    )
