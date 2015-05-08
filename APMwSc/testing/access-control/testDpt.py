import unittest
import os
import sys

# Ruta que permite utilizar el módulo model.py
sys.path.append('../../business/access-control')

from dpt import clsDpt

class TestcslRole(unittest.TestCase):

    
    #############################################      
    #       Suite de Pruebas para Insert        #
    #############################################
    
    # Caso Inicial
 
     # Prueba 1
    def test1InsertExists(self):
        dpt = clsDpt()
        dpt.insertDpt('Computacion')  
    
    def test2InsertExists(self):
        dpt = clsDpt()
        dpt.insertDpt('Quimica')  
         
    def test3ModifyNameDpt(self):
        dpt = clsDpt()
        #role.modifyNameRole('Scrum Master', 'Team Member')
        #role.modifyNameRole('Team Member', 'Scrum Master')
        dpt.modifyNameDpt('Quimica', 'Estadistica')
         
    def test4DeleteIdDpt(self):
        dpt = clsDpt()
        dpt.deleteIdDpt(3)
    