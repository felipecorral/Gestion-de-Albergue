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
    camas_id = fields.Many2many('product.template', string = 'Camas')

    # def _compute_camas(self):
        # self.camas=0
        # for cam in self.camas_id:
			# self.camas=self.camas + 1
	
		#_name = 'habitacion'
	
	
habitacion()

class ubicacion(models.Model):
    _name = "ubicacion"
    nombre = fields.Char('Nombre', size=50)
    aforo = fields.Integer('Aforo', compute="_compute_aforo", readonly=True)
    pincode = fields.Integer('Pincode',size=6)
    clavewifi = fields.Char('Clave Wifi',size=30)
    adaptada = fields.Boolean('Adaptada')
    descripcion = fields.Char('Descripción',size=300)
    direccion = fields.Char('Dirección',size=200)
    habitacion_id = fields.Many2many('habitacion', string='Habitaciones')
    def _compute_aforo(self):
		self.aforo=0
		for af in self.habitacion_id:
			self.aforo= self.aforo + af.camas
	
	
ubicacion()
	


class huesped(models.Model):
	_inherit = 'res.partner'	

	fecha_nacimiento = fields.Date('Fecha de Nacimiento')
	es_huesped = fields.Boolean("Huésped")
	es_minusvalido = fields.Boolean("Discapacitado")
	documento = fields.Binary('Identificacion', help='Seleccione un documento de identificacion')

huesped()



	
class cama(models.Model): 
  

	_inherit = 'product.template' 
	_name = "product.template"
	es_cama = fields.Boolean('Cama')
    
       
cama()



class reserva(models.Model):
    
    _inherit = 'sale.order'
    fecha_entrada = fields.Date()
    fecha_salida = fields.Date()
    es_reserva = fields.Boolean('Reserva')

	
reserva()



class empleado(models.Model):
	_inherit="hr.employee"
	_name="hr.employee"
	
	fecha_contratado=fields.Date('Fecha de contratación:')
	ubicacion_cargo = fields.Many2one('ubicacion', string='Ubicación')

empleado()
