from odoo import models, fields, api

class LegalActionCreateWizard(models.TransientModel):
    _name = 'legal.action.create.wizard'
    _description = 'Asistente para crear tarea legal'

    # Ahora NO requerido: así puede venir vacío cuando se llame desde Contactos
    agreement_id = fields.Many2one(
        'agreement',
        string='Contrato',
    )
    project_id = fields.Many2one(
        'project.project',
        string='Obra'
    )
    # Nuevo: contacto
    partner_id = fields.Many2one(
        'res.partner',
        string='Contacto'
    )

    user_id = fields.Many2one(
        'res.users',
        string='Responsable',
        required=True
    )
    legal_task_type_id = fields.Many2one(
        'legal.task.type',
        string='Tipo de tarea legal',
        required=True
    )
    description = fields.Text('Descripción / Detalle')

    @api.onchange('agreement_id')
    def _onchange_agreement_id(self):
        """Si viene de un contrato, rellenamos obra y contacto automáticamente."""
        if self.agreement_id:
            # Ajusta estos campos según tu modelo de agreement
            self.project_id = self.agreement_id.project_id.id or False
            self.partner_id = self.agreement_id.partner_id.id or False

    def action_create(self):
        self.ensure_one()
        Action = self.env['mgmtsystem.action']

        # Nombre de la acción según de dónde venga
        if self.agreement_id:
            name = "%s - %s" % (
                self.legal_task_type_id.name,
                self.agreement_id.name or ''
            )
        elif self.partner_id:
            name = "%s - %s" % (
                self.legal_task_type_id.name,
                self.partner_id.display_name
            )
        else:
            name = self.legal_task_type_id.name

        deadline = fields.Date.today()

        vals = {
            'name': name,
            'user_id': self.user_id.id,
            'is_legal': True,
            'legal_task_type_id': self.legal_task_type_id.id,
            'description': self.description or '',
            'type_action': 'immediate',   # obligatorio en mgmtsystem.action
            'date_deadline': deadline,
        }

        # Solo añado estos si existen, así no rompes nada
        if self.project_id:
            vals['project_id'] = self.project_id.id
        if self.agreement_id:
            vals['agreement_id'] = self.agreement_id.id
        if self.partner_id:
            # Asumiendo que tienes este campo en mgmtsystem.action
            vals['partner_id'] = self.partner_id.id

        action = Action.create(vals)
        return action.get_formview_action()
