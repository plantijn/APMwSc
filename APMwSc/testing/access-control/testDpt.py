'''
Created on 08/05/2015

@author: Carlos Plantijn 10-10572
@author: Luis Colorado   09-11086
         
Descripcion: 
'''

import unittest
import os
import sys

# Ruta que permite utilizar el módulo model.py
sys.path.append('../../business/access-control')

from dpt import clsDpt

class TestcslRole(unittest.TestCase):
   
    # Pruebas para Insert
 
     # Prueba 1
    def test1InsertExists(self):
        dpt = clsDpt()
        dpt.insertDpt('Computacion')  
    
    def test2InsertExists(self):
        dpt = clsDpt()
        dpt.insertDpt('Quimica')  
         
    def test3ModifyNameDpt(self):
        dpt = clsDpt()
        dpt.modifyNameDpt('Quimica', 'Estadistica')
         
    def test4DeleteIdDpt(self):
        dpt = clsDpt()
        dpt.deleteIdDpt(3)
    