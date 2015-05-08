# -*- coding: utf-8 -*-. 
'''
Created on 22/04/2015

@author: Luis Colorado   09-11086
@author: Jose Barrientos 10-10800

'''
import unittest
from mdlaccesscontrol import clsAccessControl

class controlTester(unittest.TestCase):
    
    # Casos validos----------------------------------------
    def testEncriptStringValid1(self):
        stringValid1 = clsAccessControl()
        caso = 'Josema#996'
        casoResultado = stringValid1.encript(caso)
        self.assertTrue(casoResultado)
    
    def testEncriptStringValid2(self):
        stringValid2 = clsAccessControl()
        caso = 'Oskcolorado.21'
        casoResultado = stringValid2.encript(caso)
        self.assertTrue(casoResultado)
    #------------------------------------------------------

    # Casos Malicia----------------------------------------
    def testEncriptStringEmpty(self):
        stringEmpty = clsAccessControl()
        caso = ""
        casoResultado = stringEmpty.encript(caso)
        self.assertEqual(casoResultado, "")

    def testEncriptStringWithSpace(self):
        stringWithEmpty = clsAccessControl()
        caso = "CYT 123*OWH"
        casoResultado = stringWithEmpty.encript(caso)
        self.assertFalse(casoResultado,"No puede haber espacios en blanco")
        
    def testEncriptStringUpper(self):
        stringUpper = clsAccessControl()
        caso8 = "ABCDEFGH"
        caso16 = "ABCDEFGHIJKLMNOP"
        casoResultado8 = stringUpper.encript(caso8)
        casoResultado16 = stringUpper.encript(caso16)
        self.assertFalse(casoResultado8, None)
        self.assertFalse(casoResultado16, None)
        
    def testEncriptStringLower(self):
        stringLower = clsAccessControl()
        caso8 = "abcdefgh"
        caso16 = "abcdefghijklmnop"
        casoResultado8 = stringLower.encript(caso8)
        casoResultado16 = stringLower.encript(caso16)
        self.assertFalse(casoResultado8, None)
        self.assertFalse(casoResultado16, None)  
    
    def testEncriptStringNumeric(self):
        stringNumeric = clsAccessControl()
        caso8 = "12345678"
        caso16 = "1234567887654321"
        casoResultado8 = stringNumeric.encript(caso8)
        casoResultado16 = stringNumeric.encript(caso16)
        self.assertFalse(casoResultado8, None)
        self.assertFalse(casoResultado16, None)    
    
    def testEncriptStringChar(self):
        stringChar = clsAccessControl()
        caso8 = "@*+.$+$#"
        caso16 = "@*+.$+$#@*+.$+$#"
        casoResultado8 = stringChar.encript(caso8)
        casoResultado16 = stringChar.encript(caso16)
        self.assertFalse(casoResultado8, None)
        self.assertFalse(casoResultado16, None)      
    #-------------------------------------------------------
  
    # Casos Frontera----------------------------------------
    def testEncriptStringLongEight(self):
        stringLongEight = clsAccessControl()
        caso8 = "JHGF.45J"
        casoResultado8 = stringLongEight.encript(caso8)
        self.assertTrue(casoResultado8)
     
    def testEncriptStringLongSixteen(self):
        stringLongSixteen = clsAccessControl()
        caso16 = "#@+HGBGTDK98**K."
        casoResultado16 = stringLongSixteen.encript(caso16)
        self.assertTrue(casoResultado16)
    #------------------------------------------------------
    
    # Casos Esquina----------------------------------------
    def testEncriptStringLongSeven(self):
        stringLongSeven = clsAccessControl()
        caso7 = "HGF.45J"
        casoResultado7 = stringLongSeven.encript(caso7)
        self.assertFalse(casoResultado7,"")
        
    def testEncriptStringLongSeventeen(self):
        stringLongSeventeen = clsAccessControl()
        caso17 = "#@+HGB.GTDK98**k."
        casoResultado17 = stringLongSeventeen.encript(caso17)
        self.assertFalse(casoResultado17)
    
    def testEncriptStringWithoutChar(self):
        stringWithoutChar = clsAccessControl()
        caso = "AT2SAD65SCD75"
        casoResultado = stringWithoutChar.encript(caso)
        self.assertEqual(casoResultado, "")    
    
    def testEncriptStringWithoutNumber(self):
        stringWithoutNumber = clsAccessControl()
        caso = "ATSSA*DDSCE,#"
        casoResultado = stringWithoutNumber.encript(caso)
        self.assertEqual(casoResultado, "")
            
    def testEncriptStringWithoutLetter(self):
        stringWithoutLetter = clsAccessControl()
        caso = "76254*123*#,#"
        casoResultado = stringWithoutLetter.encript(caso)
        self.assertEqual(casoResultado, "")
        
    def testEncriptStringNumberUpper(self):
        stringNumberUpper = clsAccessControl()
        caso = "12345MJGDT"
        casoResultado = stringNumberUpper.encript(caso)
        self.assertEqual(casoResultado, "")
        
    def testEncriptStringNumberSlow(self):
        stringNumberSlow = clsAccessControl()
        caso = "12345njsf"
        casoResultado = stringNumberSlow.encript(caso)
        self.assertEqual(casoResultado, "")
        
    def testEncriptStringNumberChar(self):
        stringNumberChar = clsAccessControl()
        caso = "12345.*+#"
        casoResultado = stringNumberChar.encript(caso)
        self.assertEqual(casoResultado, "")
        
    def testEncriptStringUpperChar(self):
        stringUpperChar = clsAccessControl()
        caso = "MJDH.*+#"
        casoResultado = stringUpperChar.encript(caso)
        self.assertEqual(casoResultado, "")
        
    def testEncriptStringSlowChar(self):
        stringSlowChar = clsAccessControl()
        caso = "mdsfg.*+#"
        casoResultado = stringSlowChar.encript(caso)
        self.assertEqual(casoResultado, "")

    #------------------------------------------------------