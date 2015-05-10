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
   
    # Pruebas para insertDpt
 
    # Casos Normales
    def test1InsertExists(self):
        dpt = clsDpt()
        dpt.insertDpt('Computacion')  
    
    def test2InsertExists(self):
        dpt = clsDpt()
        dpt.insertDpt('Quimica')  
         
    def test3ModifyNameDpt(self):
        dpt = clsDpt()
        dpt.modifyNameDpt('Mecánica', 'Geofísica')
         
    def test4DeleteIdDpt(self):
        dpt = clsDpt()
        dpt.deleteIdDpt(3)
    
    # Casos Fronteras
    def test4InsertLongName50(self):
        dpt    = clsDpt()
        result = dpt.insertDpt('D'*50)
        self.assertTrue(result)

    def test5InsertLongName51(self):
        dpt    = clsDpt()
        result = dpt.insertDpt('L'*51) 
        self.assertFalse(result, "Elemento insertado.")

    def test6InsertShortName0(self):
        dpt    = clsDpt()
        result = dpt.insertDpt('')
        self.assertFalse(result, "Elemento insertado.") 

    def test7InsertLongName1(self):
        dpt    = clsDpt()
        result = dpt.insertDpt('D')
        self.assertTrue(result)
                                        
    # Casos Malicia
    def test8InsertNotString(self):
        dpt    = clsDpt()
        result = dpt.insertDpt(1234)
        self.assertFalse(result,"Elemento insertado.")

    def test9InsertNoneString(self):
        dpt    = clsDpt()
        result = dpt.insertDpt(None)
        self.assertFalse(result,"No válido.")
    
    # Casos de prueba para findId

    # Casos Normales 
    def test_17FindIdExists(self):
        dpt   = clsDpt()
        dpt.findIdDpt(2)
        
    def test_18FindIdValidId(self):
        dpt    = clsDpt()
        result = dpt.findIdDpt(3)
        self.assertTrue(result)
          
    # Casos Fronteras

    def test_19FindIdMinValue(self):
        dpt    = clsDpt()
        result = dpt.findIdDpt(1)
        self.assertTrue(result)
      
    # Casos Malicia

    def test_20FindIdMinId0(self):
        dpt    = clsDpt()
        result = dpt.findIdDpt(0)
        self.assertEqual(result,[],"Es válido.")

    def test_21FindIdNotInteger(self):
        dpt    = clsDpt()
        result = dpt.findIdDpt('AldJos')
        self.assertFalse(result, "Es válido.")
    
    # Casos de prueba para findName
        
    # Caso Normal
    def test_10FindNameExists(self):
        dpt    = clsDpt()
        result = dpt.findNameDpt('Matematicas')
            
    # Casos Fronteras
    def test_11FindNameEmpty(self):
        dpt    = clsDpt()
        result = dpt.findNameDpt('')
        self.assertFalse(result, "Expresión válida.")
           
    def test_12FindNameShortName1(self):
        dpt    = clsDpt()
        result = dpt.findNameDpt('D')
        self.assertNotEqual(result,[],"Elemento no encontrado.")

    def test_13FindNameLongName50(self):
        dpt    = clsDpt()
        result = dpt.findNameDpt('D'*50)
        self.assertNotEqual(result,[],"Elemento no encontrado.")

    def test_14FindNameLongName51(self):
        dpt    = clsDpt()
        result = dpt.findNameDpt('1'*51)
        self.assertFalse(result, "Cadena no válida.")
         
    # Casos Maliciosos
    def test_15FindNameNotString(self):
        dpt    = clsDpt()
        result = dpt.findNameDpt(1254)
        self.assertFalse(result,"Elemento insertado.") 

    def test_16FindNameNoneString(self):
        dpt    = clsDpt()
        result = dpt.findNameDpt(None)
        self.assertFalse(result,"Válido.") 

    def test_22InsertNoneString(self):
        dpt    = clsDpt()
        result = dpt.findIdDpt(None)
        self.assertFalse(result,"Válido")
         
    # Casos de prueba para modifyNameDpt
    
    # Casos Normales
    def test_23ModifyNameExists(self):
        dpt   = clsDpt()
        dpt.modifyNameDpt('Computacion',25*'Si'+ 's')

    def test_24ModifyName(self):
        dpt    = clsDpt()
        result = dpt.modifyNameDpt('Computacion','AldBar')
        self.assertTrue(result)
          
    # Casos Fronteras
    def test_25ModifyNameRightLen1(self):
        dpt    = clsDpt()
        result = dpt.modifyNameDpt('AldBar','T')
        self.assertTrue(result)

    def test_26ModifyNameLeftLen1(self):
        dpt    = clsDpt()
        result = dpt.modifyNameDpt('T','Usuario')
        self.assertTrue(result)
        
    def test_27ModifyNameRightLen50(self):
       dpt    = clsDpt()
       result = dpt.modifyNameDpt('Usuario',50*'R')
       self.assertTrue(result)

    def test_28ModifyNameLeftLen50(self):
        dpt    = clsDpt()
        result = dpt.modifyNameDpt(50*'R','M')
        self.assertTrue(result)
  
    # Casos Esquinas
    def test_29ModifyNameLeftLen1RightLen50(self):
        dpt    = clsDpt()
        result = dpt.modifyNameDpt('M',25*'Us')
        self.assertTrue(result) 

    def test_30ModifyNameLeftLen50RightLen1(self):
        dpt    = clsDpt()
        result = dpt.modifyNameDpt(25*'Us','M')
        self.assertTrue(result) 

    def test_31ModifyNameLeftLen1RightLen1(self):
        dpt    = clsDpt()
        result = dpt.modifyNameDpt('M','U')
        self.assertTrue(result) 

    def test_32ModifyNameLeftLen50RightLen50(self):
        dpt    = clsDpt()
        result = dpt.modifyNameDpt('D'*50, 25*'Ma')
        self.assertTrue(result) 
 
    # Casos Malicia 
    def test_33ModifySameName(self):
        dpt    = clsDpt()
        result = dpt.modifyNameDpt('Master','Master')
        self.assertFalse(result,"Modificación Válida")

    def test_34ModifyNameLeftLen0RightLen51(self):
        dpt    = clsDpt()
        result = dpt.modifyNameDpt('',25*'Pi' + 'p')
        self.assertFalse(result, "Modificación válida") 

    def test_35ModifyNameLeftLen51RightLen0(self):
        dpt    = clsDpt()
        result = dpt.modifyNameDpt(25*'Us'+ 'a','')
        self.assertFalse(result, "Modificación válida") 

    def test_36ModifyNameLeftLen51RightLen51(self):
        dpt    = clsDpt()
        result = dpt.modifyNameDpt(25*'Si'+ 's',25*'Ma' + 's')
        self.assertFalse(result, "Modificación válida") 
 
    def test_37ModifyNameLeftNoneRightValidString(self):
        dpt    = clsDpt()
        result = dpt.modifyNameDpt(None,'Juana la Iguana')
        self.assertFalse(result,"Modificación válida") 

    def test_38ModifyNameLeftValidStringRightNone(self):
        dpt    = clsDpt()
        result = dpt.modifyNameDpt("Maleta",None)
        self.assertFalse(result) 
    
    # Casos de prueba para deleteDpto
    
    # Casos Normales
    def test_40DeleteId(self):
        dpt    = clsDpt()
        result = dpt.deleteIdDpt(3)
        self.assertTrue(result)
         
    # Casos Fronteras


    # Casos Maliciosos
