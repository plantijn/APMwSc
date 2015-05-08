import unittest
import os
import sys

# Ruta que permite utilizar el módulo model.py
#sys.path.append('../../business/access-control')

from role import clsRole

class TestcslRole(unittest.TestCase):
    
    #############################################      
    #       Suite de Pruebas para Insert        #
    #############################################
    
    # Caso Inicial
 
     # Prueba 1
     def test1InsertExists(self):
         role = clsRole()
         role.insertRole('Product Owner')  