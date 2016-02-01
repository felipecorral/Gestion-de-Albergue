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
	_name = "product.template"
	_inherit = 'product.template' 
	
	camas = fields.Char('Camas', size=5)
	
      
	#name = fields.Char('Nombre', size=50)
	#codigo = fields.Char('Código', size=5)
	#ubicacion = fields.Char('Ubicación', size=50)
	
		#_name = 'habitacion'
	
	
habitacion()


class huesped(models.Model):
	_inherit = 'res.partner'	

	fecha_nacimiento = fields.Date('Fecha de Nacimiento')
	es_huesped = fields.Boolean("Huesped")
	
	#estancia_id = fields.Many2many('estancia', 'Estancia')
		
#    name = fields.Char('Nombre', size=50)
#    direccion = fields.Char('Dirección', size=50)
#    localidad = fields.Char('Localidad', size=50)
#    provincia = fields.Char('Provincia', size=30)
#    telefono = fields.Char('Teléfono', size=12)
#    email = fields.Char('Email', size=50)

huesped()


	
class estancia(models.Model): 
  
	_name = 'estancia'   
	name = fields.Char('Nombre', size=50)
	descripcion = fields.Char('Descripción', size=100)
	estudios = fields.Char('Estudios', size=30)
	fecha_entrada = fields.Date()
	fecha_salida = fields.Date()
	fecha_reserva = fields.Date(fields.Date.today())
	habitacion_ids = fields.Many2one('habitacion', string='Habitaciones')
       
estancia()



class reserva(models.Model):
	_inherit = 'sale.order'
	
reserva()
