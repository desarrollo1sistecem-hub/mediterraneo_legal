from odoo import fields, api, models, _

class AgreementLegal(models.Model):
    _inherit = 'agreement'

    project_id = fields.Many2one(
        'project.project',
        string='Proyecto',
        help='Obra de la constructora a la que se asoció este acuerdo/contrato.'
    )

    dms_directory_id = fields.Many2one(
        'dms.directory',
        string='Directorio DMS Legal',
        help='Directorio DMS asociado al acuerdo legal'
    )

    legal_category = fields.Selection([
        ('contract', 'Contrato'),
        ('nda', 'Acuerdo de Confidencialidad'),
        ('sla', 'Acuerdo de Nivel de Servicio'),
        ('policy', 'Política'),
        ('guarantee', 'Garantía'),
        ('other', 'Otro'),
    ], string='Categoría legal')

    legal_action_id = fields.Many2one(
        'mgmtsystem.action',
        string='Acción Legal',
        help='Acción legal asociada al acuerdo legal',
        copy=False,
    )

    def action_generar_accion_legal(self):
        Action = self.env['mgmtsystem.action']
        for legal in self:
            responsable_id = legal.assigned_user_id.id if legal.assigned_user_id else self.env.user.id
            action = Action.create({
                'name': _('Acción legal para Acuerdo %s') % (legal.name or ''),
                'type_action': 'immediate',
                'user_id': responsable_id,
                'date_deadline': fields.Date.today(),
                'project_id': legal.project_id.id,
                'agreement_id': legal.id,
                'is_legal': True,
            })
            legal.legal_action_id = action.id


