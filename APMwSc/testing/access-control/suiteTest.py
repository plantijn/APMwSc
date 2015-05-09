# -*- coding: utf-8 -*-. 
'''
Created on 22/04/2015

@author: Luis Colorado   09-11086
@author: Jose Barrientos 10-10800

'''

import sys

# Ruta que permite utilizar el módulo model.py
sys.path.append('../../business/access-control')
from login import clsLogin

import unittest
from login import clsLogin

class controlTester(unittest.TestCase):
    
    # Casos validos----------------------------------------
    def testEncriptStringValid1(self):
        stringValid1 = clsLogin()
        caso = 'Josema#996'
        casoResultado = stringValid1.encript(caso)
        self.assertTrue(casoResultado)
    
    def testEncriptStringValid2(self):
        stringValid2 = clsLogin()
        caso = 'Oskcolorado.21'
        casoResultado = stringValid2.encript(caso)
        self.assertTrue(casoResultado)
    #------------------------------------------------------

    # Casos Malicia----------------------------------------
    def testEncriptStringEmpty(self):
        stringEmpty = clsLogin()
        caso = ""
        casoResultado = stringEmpty.encript(caso)
        self.assertEqual(casoResultado, "")

    def testEncriptStringWithSpace(self):
        stringWithEmpty = clsLogin()
        caso = "CYT 123*OWH"
        casoResultado = stringWithEmpty.encript(caso)
        self.assertFalse(casoResultado,"No puede haber espacios en blanco")
        
    def testEncriptStringUpper(self):
        stringUpper = clsLogin()
        caso8 = "ABCDEFGH"
        caso16 = "ABCDEFGHIJKLMNOP"
        casoResultado8 = stringUpper.encript(caso8)
        casoResultado16 = stringUpper.encript(caso16)
        self.assertFalse(casoResultado8, None)
        self.assertFalse(casoResultado16, None)
        
    def testEncriptStringLower(self):
        stringLower = clsLogin()
        caso8 = "abcdefgh"
        caso16 = "abcdefghijklmnop"
        casoResultado8 = stringLower.encript(caso8)
        casoResultado16 = stringLower.encript(caso16)
        self.assertFalse(casoResultado8, None)
        self.assertFalse(casoResultado16, None)  
    
    def testEncriptStringNumeric(self):
        stringNumeric = clsLogin()
        caso8 = "12345678"
        caso16 = "1234567887654321"
        casoResultado8 = stringNumeric.encript(caso8)
        casoResultado16 = stringNumeric.encript(caso16)
        self.assertFalse(casoResultado8, None)
        self.assertFalse(casoResultado16, None)    
    
    def testEncriptStringChar(self):
        stringChar = clsLogin()
        caso8 = "@*+.$+$#"
        caso16 = "@*+.$+$#@*+.$+$#"
        casoResultado8 = stringChar.encript(caso8)
        casoResultado16 = stringChar.encript(caso16)
        self.assertFalse(casoResultado8, None)
        self.assertFalse(casoResultado16, None)      
    #-------------------------------------------------------
  
    # Casos Frontera----------------------------------------
    def testEncriptStringLongEight(self):
        stringLongEight = clsLogin()
        caso8 = "JHGF.45J"
        casoResultado8 = stringLongEight.encript(caso8)
        self.assertTrue(casoResultado8)
     
    def testEncriptStringLongSixteen(self):
        stringLongSixteen = clsLogin()
        caso16 = "#@+HGBGTDK98**K."
        casoResultado16 = stringLongSixteen.encript(caso16)
        self.assertTrue(casoResultado16)
    #------------------------------------------------------
    
    # Casos Esquina----------------------------------------
    def testEncriptStringLongSeven(self):
        stringLongSeven = clsLogin()
        caso7 = "HGF.45J"
        casoResultado7 = stringLongSeven.encript(caso7)
        self.assertFalse(casoResultado7,"")
        
    def testEncriptStringLongSeventeen(self):
        stringLongSeventeen = clsLogin()
        caso17 = "#@+HGB.GTDK98**k."
        casoResultado17 = stringLongSeventeen.encript(caso17)
        self.assertFalse(casoResultado17)
    
    def testEncriptStringWithoutChar(self):
        stringWithoutChar = clsLogin()
        caso = "AT2SAD65SCD75"
        casoResultado = stringWithoutChar.encript(caso)
        self.assertEqual(casoResultado, "")    
    
    def testEncriptStringWithoutNumber(self):
        stringWithoutNumber = clsLogin()
        caso = "ATSSA*DDSCE,#"
        casoResultado = stringWithoutNumber.encript(caso)
        self.assertEqual(casoResultado, "")
            
    def testEncriptStringWithoutLetter(self):
        stringWithoutLetter = clsLogin()
        caso = "76254*123*#,#"
        casoResultado = stringWithoutLetter.encript(caso)
        self.assertEqual(casoResultado, "")
        
    def testEncriptStringNumberUpper(self):
        stringNumberUpper = clsLogin()
        caso = "12345MJGDT"
        casoResultado = stringNumberUpper.encript(caso)
        self.assertEqual(casoResultado, "")
        
    def testEncriptStringNumberSlow(self):
        stringNumberSlow = clsLogin()
        caso = "12345njsf"
        casoResultado = stringNumberSlow.encript(caso)
        self.assertEqual(casoResultado, "")
        
    def testEncriptStringNumberChar(self):
        stringNumberChar = clsLogin()
        caso = "12345.*+#"
        casoResultado = stringNumberChar.encript(caso)
        self.assertEqual(casoResultado, "")
        
    def testEncriptStringUpperChar(self):
        stringUpperChar = clsLogin()
        caso = "MJDH.*+#"
        casoResultado = stringUpperChar.encript(caso)
        self.assertEqual(casoResultado, "")
        
    def testEncriptStringSlowChar(self):
        stringSlowChar = clsLogin()
        caso = "mdsfg.*+#"
        casoResultado = stringSlowChar.encript(caso)
        self.assertEqual(casoResultado, "")

    #------------------------------------------------------