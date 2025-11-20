from odoo import models, fields

class LegalActionCreateWizard(models.TransientModel):
    _name = 'legal.action.create.wizard'
    _description = 'Asistente para crear tarea legal'

    agreement_id = fields.Many2one(
        'agreement',
        string='Contrato',
        required=True
    )
    project_id = fields.Many2one(
        'project.project',
        string='Obra'
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

    def action_create(self):
        self.ensure_one()
        Action = self.env['mgmtsystem.action']

        # Nombre de la acción
        name = "%s - %s" % (
            self.legal_task_type_id.name,
            self.agreement_id.name or ''
        )

        deadline = fields.Date.today()

        action = Action.create({
            'name': name,
            'user_id': self.user_id.id,
            'project_id': self.project_id.id,
            'agreement_id': self.agreement_id.id,
            'is_legal': True,
            'legal_task_type_id': self.legal_task_type_id.id,
            'description': self.description or '',
            'type_action': 'immediate',   # campo obligatorio en mgmtsystem.action
            'date_deadline': deadline,
        })

        return action.get_formview_action()
