import unittest
import os
import sys

# Ruta que permite utilizar el módulo model.py
sys.path.append('../../business/access-control')

from role import clsRole

class TestcslRole(unittest.TestCase):

    
    #############################################      
    #       Suite de Pruebas para Insert        #
    #############################################
    
    # Caso Inicial
 
     # Prueba 1
    def test1InsertExists(self):
        role = clsRole()
        role.insertRole('Scrum Master')  
    
    def test2InsertExists(self):
        role = clsRole()
        role.insertRole('Product Owner')  
         
    def test3ModifyNameRole(self):
        role = clsRole()
        #role.modifyNameRole('Scrum Master', 'Team Member')
        #role.modifyNameRole('Team Member', 'Scrum Master')
        role.modifyNameRole('Product Owner', 'Team Member')
        
    def test4DeleteIdRole(self):
        role = clsRole()
        role.deleteIdRole(1)
    