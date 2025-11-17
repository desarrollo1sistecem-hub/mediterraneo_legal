from odoo import fields, models

from email.policy import default


class ProjectProject(models.Model):
    _inherit = 'project.project'

    agreement_ids = fields.One2many(
        'agreement', 'project_id',
        string='Contratos / Acuerdos legales'
    )

    legal_action_ids = fields.One2many(
        'mgmtsystem.action', 'project_id',
        string='Acciones / Tareas legales',
        domain=[('is_legal', '=', True)]
    )

    dms_directory_legal_id = fields.Many2one(
        'dms.directory',
        string='Directorio DMS Legal',
        help='Directorio raiz de documentos legales de esta obra.'
    )
