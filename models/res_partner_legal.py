from odoo import models, fields,api

class ResPartnerLegal(models.Model):
    _inherit = 'res.partner'

    legal_state=fields.Selection([
        ('peding', 'Pendiente revision Legal'),
        ('approved', 'Aprobado por Legal'),
        ('rejected', 'Rechazado por Legal'),
        ('validated', 'Validado por Legal'),

    ])

    legal_notes = fields.Text('Notas legales')
    legal_doc_number = fields.Char('N° contrato marco / doc. legal')
    legal_doc_valid_until = fields.Date('Vigencia documento legal')


    legal_identifier = fields.Char( string='Identificador legal')
    legal_razon_social = fields.Char( string='Razón social')
    legal_representative = fields.Char( string='Representante legal')
    legal_address = fields.Char( string='Dirección legal')
    legal_tax_id = fields.Char( string='NIT / CIF')
    legal_phone = fields.Char( string='Teléfono legal')
    legal_email = fields.Char(string='Email legal')
    nit_archivo = fields.Binary(
        string='Foto/Scan NIT/CI',
        attachment=True,
        store=True,
        help='Sube el archivo escaneado o foto del NIT o Cédula de Identidad.'
    )