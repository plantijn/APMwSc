# -*- coding: utf-8 -*-. 
'''
Created on 24/04/2015

@author: Luis Colorado   09-11086
@author: Jose Barrientos 10-10800

'''

import sys

# Ruta que permite utilizar el módulo model.py
sys.path.append('../../business/access-control')
from login import clsLogin

import unittest
from login import clsLogin

class lTesterCheckPasword(unittest.TestCase):
    
    # Casos Esquina .............................
    
    # Caso cadena de 17 caracteres
    def testStringSevenTeen(self):
        sevenTeenString = clsLogin()
        caso17 = "U.i4J#l2P@k8N+b0t"
        casoResultado = sevenTeenString.check_password("", caso17)
        self.assertFalse(casoResultado)
    
    # Caso cadena de 7 caracteres    
    def testStringSeven(self):
        sevenString = clsLogin()
        caso7 = "MG.#ne4"
        casoResultado = sevenString.check_password("", caso7)
        self.assertFalse(casoResultado)
        
    # Csaos Frontera  ......................
    
    # Caso cadena valida de 8 caracteres
    def testStringEightValid(self):
        eightValidString = clsLogin()
        caso8 = "lMan4n4."
        casoTrue = eightValidString.encript(caso8)
        casoResultado = eightValidString.check_password(casoTrue, caso8)
        self.assertTrue(casoResultado)
        
    # Caso cadena valida de 8 caracteres y cadena valida de 8 caracteres distinta
    def testStringEightValidValid(self):
        eightValidValidString = clsLogin()
        caso8 = "lMan4n4."
        aux = "Luis.21x"
        casoTrue = eightValidValidString.encript(aux)
        casoResultado = eightValidValidString.check_password(casoTrue, caso8)
        self.assertFalse(casoResultado)
    
    # Caso cadena valida de 8 caracteres y cadena invalidade 8 caracteres
    def testStringEightValidInvalid(self):
        eightValidInvalidString = clsLogin()
        caso8 = "lMan4n4."
        aux = "L4l4."
        casoTrue = eightValidInvalidString.encript(aux)
        casoResultado = eightValidInvalidString.check_password(casoTrue, caso8)
        self.assertFalse(casoResultado)
 
    # Caso cadena valida de 16 caracteres    
    def testStringSixteenValid(self):
        sixteenValidString = clsLogin()
        caso16 = "#mcjubJBs86*gTK."
        casoTrue = sixteenValidString.encript(caso16)
        casoResultado = sixteenValidString.check_password(casoTrue, caso16)
        self.assertTrue(casoResultado)
        
    # Caso cadena valida de 16 caracteres    
    def testStringSixteenValidValid(self):
        sixteenValidValidString = clsLogin()
        caso16 = "#mcjubJBs86*gTK."
        aux = "#mc45bJBs86*gTK."
        casoTrue = sixteenValidValidString.encript(aux)
        casoResultado = sixteenValidValidString.check_password(casoTrue, caso16)
        self.assertFalse(casoResultado)
        
    # Caso cadena valida de 8 caracteres y cadena invalidade 8 caracteres
    def testStringSixteenValidInvalid(self):
        sixteenValidInvalidString = clsLogin()
        caso8 = "ynsaciHGSD*+.213"
        aux = "L4l4."
        casoTrue = sixteenValidInvalidString.encript(aux)
        casoResultado = sixteenValidInvalidString.check_password(casoTrue, caso8)
        self.assertFalse(casoResultado)
  
    # Casos Malicia ............................
    
    # Caso cadena de 8 caracteres vacios
    def testStringEightSpace(self):
        spaceString = clsLogin()
        caso = "        "
        casoResultado = spaceString.check_password("", caso)
        self.assertFalse(casoResultado)
    
    # Cadena vacia
    def testStringEmpty(self):
        stringEmpty = clsLogin()
        caso = ''
        casoResultado = stringEmpty.check_password('', caso)
        self.assertFalse(casoResultado)
    
    # Cadena valida de 14 caracteres y una cadena invalida de 14 caracteres    
    def testStringValidInvalid14(self):
        validInvalidString = clsLogin()
        caso = "#mcjubs86*gTK."
        aux = "#mcjuBs86*gTK."
        casoTrue = validInvalidString.encript(aux)
        casoResultado = validInvalidString.check_password(casoTrue, caso)
        self.assertFalse(casoResultado)
    
    # Cadena invalida de 8 caracteres y una cadena valida de 8 caracteres  
    def testStringInvalidValid8(self):
        invalidValidString = clsLogin()
        caso = "12345678"
        aux = "1Tr45#e."
        casoTrue = invalidValidString.encript(aux)
        casoResultado = invalidValidString.check_password(casoTrue, caso)
        self.assertFalse(casoResultado)
    
    # Cadena invalida de 16 caracteres y una cadena valida de 16 caracteres    
    def testStringInvalidValid16(self):
        invalidValidString = clsLogin()
        caso = "1234567890asdfgl"
        aux = "Tr45#e..*+#kdcSD"
        casoTrue = invalidValidString.encript(aux)
        casoResultado = invalidValidString.check_password(casoTrue, caso)
        self.assertFalse(casoResultado)
    
    # Cadena invalida de 8 caracteres y una cadena invalida de 8 caracteres    
    def testStringInvalidInvalid8(self):
        invalidInvalidString = clsLogin()
        caso = "12345678"
        aux = "tr45#e.."
        casoTrue = invalidInvalidString.encript(aux)
        casoResultado = invalidInvalidString.check_password(casoTrue, caso)
        self.assertFalse(casoResultado)
            
    # Cadena invalida de 16 caracteres y una cadena invalida de 16 caracteres    
    def testStringInvalidInvalid16(self):
        invalidInvalidString = clsLogin()
        caso = "1234567890asdfgl"
        aux = "tr45#e..*+#kdcsd"
        casoTrue = invalidInvalidString.encript(aux)
        casoResultado = invalidInvalidString.check_password(casoTrue, caso)
        self.assertFalse(casoResultado)
                
    