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


{
    "name": "Gestión de Albergue",
    "version": "0.1",
    "category": "",
    "depends": [
                'base', 'sale', 'hr'               
                ],
    "author": "Felipe Corral y Juan Muñiz",
    "description": "Módulo para gestión básica de un albergue de peregrinos",
    "init_xml": [],
    "data": [             
             'albergue_view.xml'
             ],
    "demo_xml": [],
    "installable": True,
    "active": False,
}
