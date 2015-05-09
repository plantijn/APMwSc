# -*- coding: utf-8 -*-. 
'''
Created on 24/04/2015

Modificado

@author: Luis Colorado   09-11086
@author: Jose Barrientos 10-10800

'''
import sys

# Ruta que permite utilizar el módulo model.py
sys.path.append('../../business/access-control')
from login import clsLogin

import unittest
from login import clsLogin

class cTesterLengthPassword(unittest.TestCase):

    # Caso Valido--------------------------------------------
    def testLengthStringValid(self):
        sizeStringValid = clsLogin()
        caso = 'JOS1E*M*A1'
        casoResultado = sizeStringValid.length_password(caso)
        self.assertTrue(casoResultado)
    #-------------------------------------------------------

    # Caso Malicia------------------------------------------
    def testLengthStringEmpty(self):
        sizeStringEmpty = clsLogin()
        caso = ""
        casoResultado = sizeStringEmpty.length_password(caso)
        self.assertFalse(casoResultado)
      
    def testLengthStringGreatest(self):
        sizeStringGreatest = clsLogin()
        caso = 'a'*((2**28)-1)
        casoResultado = sizeStringGreatest.length_password(caso)
        self.assertEqual(casoResultado, (2**28) - 1, "Cadena demasiado grande")
    
        
    def testStringInterSpace(self):
        stringInterSpace = clsLogin()
        caso = 'Celtics #23'
        casoResultado = stringInterSpace.length_password(caso)
        self.assertEqual(casoResultado, 11)
    #---------------------------------------------------------

    # Caso Frontera-------------------------------------------
    def testLengthStringEight(self):
        sizeStringEight = clsLogin()
        caso8 = "LUIS.*12"
        casoResultado = sizeStringEight.length_password(caso8)
        self.assertTrue(casoResultado)
        
    def testLengthStringSixteen(self):
        sizeStringSixteen = clsLogin()
        caso16 = "LUIS.*12JO*SE$MA"
        casoResultado = sizeStringSixteen.length_password(caso16)
        self.assertTrue(casoResultado)
        
    # Caso Esquina----------------------------------------       
    def testLengthStringSeven(self):
        sizeStringSeven = clsLogin()
        caso7 = "LUIS.*1"
        casoResultado = sizeStringSeven.length_password(caso7)
        self.assertTrue(casoResultado)

    def testLengthStringNine(self):
        sizeStringNine = clsLogin()
        caso9 = "S.*12JOA$"
        casoResultado = sizeStringNine.length_password(caso9)
        self.assertTrue(casoResultado)

    def testLengthStringFifteen(self):
        sizeStringFifteen = clsLogin()
        caso15 = "LUIS.*1JO*SE$MA1"
        casoResultado = sizeStringFifteen.length_password(caso15)
        self.assertTrue(casoResultado)

    def testLengthStringSeventeen(self):
        sizeStringSeventeen = clsLogin()
        caso17 = "LUI1S.*12JO*SE$MA"
        casoResultado = sizeStringSeventeen.length_password(caso17)
        self.assertTrue(casoResultado)