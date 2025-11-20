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

    # legal_action_id = fields.Many2one(
    #     'mgmtsystem.action',
    #     string='Acción Legal',
    #     help='Acción legal asociada al acuerdo legal',
    #     copy=False,
    # )

    legal_action_ids = fields.One2many(
        'mgmtsystem.action',
        'agreement_id',  # Este campo ya existe en mgmtsystem_legal.py
        string='Acciones Legales'
    )

    # def action_generar_accion_legal(self):
    #     Action = self.env['mgmtsystem.action']
    #     for legal in self:
    #         responsable_id = legal.assigned_user_id.id if legal.assigned_user_id else self.env.user.id
    #         action = Action.create({
    #             'name': _('Acción legal para Acuerdo %s') % (legal.name or ''),
    #             'type_action': 'immediate',
    #             'user_id': responsable_id,
    #             'date_deadline': fields.Date.today(),
    #             'project_id': legal.project_id.id,
    #             'agreement_id': legal.id,
    #             'is_legal': True,
    #         })
    #         legal.legal_action_id = action.id

    #metodo origanl que funciona
    # def action_generar_accion_legal(self):
    #     Action = self.env['mgmtsystem.action']
    #     for legal in self:
    #         # Lógica del responsable que vimos antes
    #         responsable_id = legal.assigned_user_id.id if legal.assigned_user_id else self.env.user.id
    #
    #         # Creamos la acción. Al pasar 'agreement_id': legal.id,
    #         # se vincula automáticamente a la lista legal_action_ids.
    #         Action.create({
    #             'name': _('Acción legal para Acuerdo %s') % (legal.name or ''),
    #             'type_action': 'immediate',
    #             'user_id': responsable_id,
    #             'date_deadline': fields.Date.today(),
    #             'project_id': legal.project_id.id,
    #             'agreement_id': legal.id,  # <--- Esto hace el vínculo
    #             'is_legal': True,
    #         })

    def action_generar_accion_legal(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Crear tarea legal'),
            'res_model': 'legal.action.create.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_agreement_id': self.id,
                'default_project_id': self.project_id.id,
                'default_user_id': (
                    self.assigned_user_id.id
                    if hasattr(self, 'assigned_user_id') and self.assigned_user_id
                    else self.env.user.id
                ),
            },
        }

    @api.onchange('project_id')
    def _onchange_project_id_set_partner(self):
        for rec in self:
            rec.partner_id = rec.project_id.partner_id
