# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2015-2015  Wagner Pereira (BGI OpenSolutions)                 #
#                                                                             #
#This program is free software: you can redistribute it and/or modify         #
#it under the terms of the GNU Affero General Public License as published by  #
#the Free Software Foundation, either version 3 of the License, or            #
#(at your option) any later version.                                          #
#                                                                             #
#This program is distributed in the hope that it will be useful,              #
#but WITHOUT ANY WARRANTY; without even the implied warranty of               #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
#GNU Affero General Public License for more details.                          #
#                                                                             #
#You should have received a copy of the GNU Affero General Public License     #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
###############################################################################

from openerp.osv import orm
from openerp import api
import requests,logging

class ResCompany(orm.Model):
    _inherit = 'res.company'

    @api.one
    def zip_search(self):
       get_url_viacep = 'http://viacep.com.br/ws/' + self.zip + '/json'
       obj_viacep = requests.get(get_url_viacep)
       data_viacep = obj_viacep.json()
       # Ignore if error returned
       if ("error" in data_viacep):
          return True
       else:
          self.street   = data_viacep['logradouro']
          self.district = data_viacep['bairro']

          # Locate Country Code
          Country = self.env['res.country']
          cod_pais = Country.search([('name','=','Brasil')])
          self.country_id = cod_pais.id

          # Locate State Code
          State = self.env['res.country.state']
          cod_estado = State.search([('code','=',data_viacep['uf'])])
          self.state_id = cod_estado.id

          # Locate City
          City = self.env['l10n_br_base.city']
          City.filtered
          cod_cidade = City.search(['&',('name','=',data_viacep['localidade']),(
'state_id','=',cod_estado.id)])
          self.l10n_br_city_id = cod_cidade.id

       return True

              
