{
 'name': 'BGI - ViaCEP API Integration',
 'description': 'Enables ViaCEP API Integration to automatically fill in address details for Brazil from www.viacep.com.br',
 'author': 'Wagner Pereira - BGI OpenSolutions',
 'category': 'Localization',
 'license': 'AGPL-3',
 'summary': 'This module uses the API from ViaCEP to automatically fill in address data for Brazil users, the api is available in www.viacep.com.br. It depends on Brazil Localization created by Akreation.',
 'version': '1.0',
 'depends': ['l10n_br_base'],
 'application': False,
 'data': [
  'res_partner_view.xml',
  'res_company_view.xml'
 ],
}
