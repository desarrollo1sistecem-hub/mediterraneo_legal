from gevent.resolver.cares import result
from odoo import fields, api, models, _

class ResPartnerLegal(models.Model):
    _inherit = 'res.partner'

    legal_state=fields.Selection([
        ('peding', 'Pendiente revision Legal'),
        ('approved', 'Aprobado por Legal'),
        ('rejected', 'Rechazado por Legal'),
        ('validated', 'Validado por Legal'),

    ] , required=True, string='Estado Legal', default='peding')

    legal_notes = fields.Text('Notas legales', required=True)
    legal_doc_number = fields.Char('N° contrato marco / doc. legal', required=True)
    legal_doc_valid_until = fields.Date('Vigencia documento legal', required=True)


    legal_identifier = fields.Char( string='Identificador legal', required=True)
    legal_razon_social = fields.Char( string='Razón social', required=True)
    legal_representative = fields.Char( string='Representante legal', required=True)
    legal_address = fields.Char( string='Dirección legal', required=True)
    legal_tax_id = fields.Char( string='NIT / CIF', required=True)
    legal_phone = fields.Char( string='Teléfono legal', required=True)
    legal_email = fields.Char(string='Email legal', required=True)
    nit_archivo = fields.Binary(
        string='Foto/Scan NIT/CI',
        attachment=True,
        store=True,
        help='Sube el archivo escaneado o foto del NIT o Cédula de Identidad.', required=True
    )
    # # esto solo  puse para que pueda le
    # legal_status = fields.Selection([])
    # legal_last_review_date = fields.Date('Last revisada')
    # legal_source_document = fields.Binary()


    # @api.model
    # def funcionalidad_create_task_legal(self):
    #     task_legal = self.env['agreement']
    #     result = task_legal.action_generar_accion_legal()
    #     return result
    #
    # def action_llamar_funcionalidad_create_task_legal(self):
    #     for record in self:
    #         record.funcionalidad_create_task_legal()

    def action_generar_accion_legal(self):


        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'name': _('Crear tarea legal'),
            'res_model': 'legal.action.create.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                # Contacto actual
                'default_partner_id': self.id,
                # Responsable por defecto: el usuario logueado
                'default_user_id': self.env.user.id,
                # Bandera por si quieres distinguir en el wizard
                'from_res_partner': True,
            },
        }