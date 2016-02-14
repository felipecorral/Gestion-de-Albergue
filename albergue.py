# -*- coding: utf-8 -*-
#################################################################################
#
#    OpenERP, Open Source Management Solution
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################
from openerp import fields, models

class habitacion(models.Model):    
	_name = "habitacion"
	

	camas = fields.Integer('Camas', size=5)
    	
	name = fields.Char('Nombre', size=50)
	codigo = fields.Char('Código', size=5)
	ubicacion = fields.Char('Ubicación', size=50)
	#camas_id = fields.Many2one('product.template', 'Camas')
	
		#_name = 'habitacion'
	
	
habitacion()

class ubicacion(models.Model):
    _name = "ubicacion"
    nombre = fields.Char('Nombre', size=50)
    aforo = fields.Integer('Aforo',size=5)
    pincode = fields.Integer('Pincode',size=6)
ubicacion()
	


class huesped(models.Model):
	_inherit = 'res.partner'	

	fecha_nacimiento = fields.Date('Fecha de Nacimiento')
	es_huesped = fields.Boolean("Huesped")
	documento = fields.Binary('Identificacion', help='Seleccione un documento de identificacion')

huesped()



	
class cama(models.Model): 
  

	_inherit = 'product.template' 
	_name = "product.template"
	es_cama = fields.Boolean('Cama')
	#habitacion_id = fields.Many2one('habitacion','Habitacion')
    
	#huesped_ids = fields.Many2one('partner_id', string='Habitaciones')
       
cama()



class reserva(models.Model):
    
    _inherit = 'sale.order'
    #partner_id = fields.Many2one('res.partner', 'Huesped', domain=[("es_huesped", "=", True)])
    fecha_entrada = fields.Date()
    fecha_salida = fields.Date()
    es_reserva = fields.Boolean('Reserva')

	
reserva()



class empleado(models.Model):
	_inherit="hr.employee"
	_name="hr.employee"
	
	fecha_contratado=fields.Date("Fecha de contratación:")
	#ubicacion_cargo = fields.Many2one("ubicacion", "Ubicaciones", delegate=True)

empleado()
