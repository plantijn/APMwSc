# -*- coding: utf-8 -*-. 
'''
Created on 09/05/2015
@author: Carlos Plantijn
         Luis Colorado
'''
import unittest

import os
import sys


# Ruta que permite utilizar el módulo model.py
sys.path.append('../../business/access-control')

from user import *

class TestclsUser(unittest.TestCase):

    # Pruebas para Insert        

    # Insertando roles y departamentos
    def test1InsertExists(self):
        newrole = model.Role("Product Owner")
        session.add(newrole)
        session.commit()
        
        newrole = model.Role("Scrum Master")
        session.add(newrole)
        session.commit()
        
        newrole = model.Role("Team Member")
        session.add(newrole)
        session.commit()
        
        newdpt = model.Dpt("Matemáticas")
        session.add(newdpt)
        session.commit()

        newdpt = model.Dpt("Computación")
        session.add(newdpt)
        session.commit()

        newdpt = model.Dpt("Materiales")
        session.add(newdpt)
        session.commit()
        
        newdpt = model.Dpt("Física")
        session.add(newdpt)
        session.commit()

        newdpt = model.Dpt("Mecánica")
        session.add(newdpt)
        session.commit()

        newuser = clsUser()
        newuser.insertUser("Luis","oskcolorado","C0l0r4d0!","oskcolorado@icloud.com",1,1)
    
    # Casos Normales
   
    def test2InsertUser(self):        
        newuser = clsUser()
        result = newuser.insertUser("Astrid","astridjhc","56789123","def@gmail.com",2,2)
        self.assertTrue(result)
 
    def test3InsertNotExistsUser(self):        
        newuser = clsUser()
        result = newuser.insertUser("Carlos","mr.carlos","33455678","ghi@hotmail.com",3,3)
        self.assertTrue(result)

    # Casos Fronteras
    def test4InsertIDs1(self):
        newuser = clsUser()
        result = newuser.insertUser("Carlos","ccp","1234567845","jkl@yahoo.com",1,1)    
        self.assertTrue(result)

    def test5InsertNameUser1(self):
        newuser = clsUser()
        result = newuser.insertUser("Luis","c","12567887933","mno@hotmail.com",4,3)    
        self.assertTrue(result)

    def test6InsertNameUser16(self):
        newuser = clsUser()
        result = newuser.insertUser("Pedro",16*"c","12567844933","pqr@gmail.com",5,1)    
        self.assertTrue(result)

    def test7InsertNameFull1(self):
        newuser = clsUser()
        result = newuser.insertUser("A","ccc","1256s44933","pqrt@gmail.com",3,2)    
        self.assertTrue(result)

    def test8InsertNameFull50(self):
        newuser = clsUser()
        result = newuser.insertUser(50*"P","cvc","15y6s44933","stu@usb.ve",1,3)    
        self.assertTrue(result)

    def test9InsertNameEmail1(self):
        newuser = clsUser()
        result = newuser.insertUser("Andrea","rvc","15y6sf4933","a@usb.ve",5,2)    
        self.assertTrue(result)

    def test_10InsertNameEmail30(self):
        newuser = clsUser()
        result = newuser.insertUser("Miguel","tsd","15y6sf4993",10*"a3" +"@gamil.com",5,1)    
        self.assertTrue(result)

    def test_11InsertName17(self):
        newuser   = clsUser()
        result = newuser.insertUser("Arleyn",8*"pt" + "h","lkfodfohfiof","xcxc@gmail.com",4,2)
        self.assertFalse(result,"Es válido")

    # Casos Esquinas
    def test_12InsertIDs1Name1(self):
        newuser = clsUser()
        result = newuser.insertUser("Olga","x","1234t67845","jklo@gamil.com",1,1)    
        self.assertTrue(result)

    def test_13InsertPass16NameUser16Email30(self):
        newuser = clsUser()
        result = newuser.insertUser("Juana",8*"ca",2*"12567883",10*"mn"+"@gamil.com",5,1)    

    def test_14InsertPass8NameUser16Email30(self):
        newuser = clsUser()
        result = newuser.insertUser("Pedro",8*"d","1256784t",10*"pr"+"@gamil.com",2,2)    
        self.assertTrue(result)

    def test_15InsertNameUser1FullName1Password8(self):
        newuser = clsUser()
        result = newuser.insertUser("O","p","1256s449","pqrt@gamil.com",1,2)    
        self.assertTrue(result)

    def test_16InsertPassword16NameUser1Email30(self):
        newuser = clsUser()
        result = newuser.insertUser("Leonid","v",8*"15",10*"st"+"@gamil.com",3,3)    
        self.assertTrue(result)

    def test_17InsertNameUser1FullName50(self):
        newuser = clsUser()
        result = newuser.insertUser(10*"Andre","r","15y6sf3563","a@gamil.com",1,1)    
        self.assertTrue(result)

    def test_18InsertNameUser1FullName1(self):
        newuser = clsUser()
        result  = newuser.insertUser("M","d","15y6sf4993",2*"a34"+"@gamil.com",5,1)    
        self.assertTrue(result)

    def test_19InsertNameUser16Password16FullName50(self):
        newuser = clsUser()
        result  = newuser.insertUser(10*"Arley",8*"la",4*"45ag","xcxc@gmail.com",1,1)
        self.assertTrue(result,"Es válido")
        
    # Casos Malicia
    def test_20InsertID0(self):
        newuser = clsUser()
        result  = newuser.insertUser("Alfredo","sE1ex","25das745df2","jmb@gmail.com",0,1)
        self.assertFalse(result,"Inserción válida")
          
    def test_21InsertUserNone(self):
        newuser = clsUser()
        result  = newuser.insertUser("Domingo",None,"dksmcvmska","dmgo@gmail.com",1,2)
        self.assertFalse(result,"Inserción Válida")
        
    def test_22InsertPasswordNone(self):
        newuser = clsUser()
        result  = newuser.insertUser("Lorenars","Vicky",None,"Lorenarst@gmail.com",5,3)
        self.assertFalse(result,"Inserción Válida")
        
    def test_23InsertPasswordNoneNameUserNoneID0NegativeId(self):
        newuser = clsUser()
        result  = newuser.insertUser("Lorenars",None,None,"Lorenarst@gmail.com",0,-1)
        self.assertFalse(result,"Inserción Válida")
              
    def test_24DeleteNameExists(self):
        user = clsUser()
        user.deleteUserName("oskcolorado")
        
    # Casos de prueba para modifyUsername
    
    # Caso Inicial
    def test_31ModifyNameExists(self):
        newuser = clsUser()
        newuser.modifyUserName("Patricia","jmb","08004578","cosas@hotmail.com",1,1) 

    def test_32ModifyNameTrue(self):
        newuser = clsUser()
        result  = newuser.modifyUserName("Maria","d","0800AJMB","coach@hotmail.com",1,3)
        self.assertTrue(result)

    def test_33ModifyNameFalse(self):
        newuser = clsUser()
        result  = newuser.modifyUserName("Olys","c1c","4587djsk","Holis@gmail.com",5,3)
        self.assertFalse(result,"Modicación válida.")   

    def test_34ModifyNameSameName(self): 
        newuser = clsUser()
        result  = newuser.modifyUserName("Patricia",8*"la","33455678","ghi@hotmail.com",3,3)
        self.assertTrue(result)  

    # Casos Fronteras
    def test_35ModifyIDs1(self):
        newuser = clsUser()
        result = newuser.modifyUserName("Carlos","ccp","1234567845","jkl@yahoo.com",1,1)    
        self.assertTrue(result)

    def test_36ModifyNameUser1(self):
        newuser = clsUser()
        result = newuser.modifyUserName("Luis Edgardo","x","12hot78sss933","mnoy@hotmail.com",4,3)    
        self.assertTrue(result)

    def test_37ModifyNameUser16(self):
        newuser = clsUser()
        result = newuser.modifyUserName("Juanitox","d","12567844933","pqr1@gmail.com",3,1)    
        self.assertTrue(result)

    def test_38ModifyNameFull1(self):
        newuser = clsUser()
        result = newuser.modifyUserName("X","p","1256s44933","pqxxccrt@gmail.com",3,2)    
        self.assertTrue(result)

    def test_39ModifyNameFull50(self):
        newuser = clsUser()
        result = newuser.modifyUserName(25*"Na","cvc","15y6s44933","stu69@usb.ve",1,3)    
        self.assertTrue(result)

    def test_40ModifyNameEmail30(self):
        newuser = clsUser()
        result = newuser.modifyUserName("Miguel","tsd","15Holaui3",10*"a3" +"@gamil.com",2,1)    
        self.assertTrue(result)

    def test_41ModifyName17(self):
        newuser   = clsUser()
        result = newuser.modifyUserName("Arleyn Martinez",8*"pt" + "h","lkfodfohfiof","xcxc@gmail.com",4,2)
        self.assertFalse(result,"Es válido")       

    # Casos Esquinas
    def test_41ModifyNamePass8IDLeft1IDRight1(self):
        newuser = clsUser()
        result  = newuser.modifyUserName("Aldrox","tsd","MarI7569","abc@hotmail.com",2,2)
        self.assertTrue(result)

    def test_42ModifyNamePass8IDLeft1IDRight3(self):
        newuser = clsUser()
        result  = newuser.modifyUserName("Leo","cvc","Hectoriod","stu@usb.ve",1,1)
        self.assertTrue(result)

    def test_43ModifyNameEmail30ID1(self):
        newuser = clsUser()
        result  = newuser.modifyUserName("Miguel","tsd","15y6sf4993","miguelcold@gamil.com",4,1)
        self.assertTrue(result)

    def test_44ModifyNameEmail30Pass16ID1(self):
        newuser = clsUser()
        result  = newuser.modifyUserName("Juana",8*"ca","juanalaiguana","juanitaiguana@gmail.com",5,2)
        self.assertTrue(result)

    def test_45ModifyNameEmail30Pass8(self):
        newuser = clsUser()
        result  = newuser.modifyUserName("Pedro Linares", 8*"d","HDJD7546","Pedro69@gmail.com",2,2)
        self.assertTrue(result)

    def test_46ModifyNameFullName1Pass8ID1(self):
        newuser = clsUser()
        result  = newuser.modifyUserName("Oriana","p","jEREMIAS856","Pregrado@gmail.com",5,1)
        self.assertTrue(result)
 
    def test_47ModifyNameFullName50Pass8ID1(self):
        newuser = clsUser()
        result  = newuser.modifyUserName("Nicolas","r","RadioMotor","NicoRico@hotmail.com",4,2)
        self.assertTrue(result)         
                                 
    def test_48ModifyNameEmail30Pass16ID3(self):
        newuser = clsUser()
        result  = newuser.modifyUserName("Leonid","v","THeGreatLion2015","LeoSoporte@usb.ve",1,1)
        self.assertTrue(result)
                                          
    def test_49ModifyNamePass8ID1(self):
        newuser = clsUser()
        result  = newuser.modifyUserName("Josema","ccp","Josesito","Jose16@hotmail.com",5,2)
        self.assertTrue(result)
                                          
    def test_50ModifyNamePass8IDLeft1IDRight3(self):
        newuser = clsUser()
        result  = newuser.modifyUserName("Maria","d","0800AJMB","coach@hotmail.com",5,1)
        self.assertTrue(result)
        
    # Pruebas para FindName
    
    # Caso normal
    def test_24FindUserNameExists(self):
        user   = clsUser()
        user.findUserName('Andrea')
            
    # Casos Fronteras
    def test_25FindUserNameEmpty(self):
        user   = clsUser()
        result = user.findUserName('')
        self.assertFalse(result, "Expresión válida.")

    def test_26FindUserNameShortName1(self):
        user   = clsUser()
        result = user.findUserName('T')
        self.assertEqual(result,[],"Elemento no encontrado.")

    def test_27FindUserNameLongName16(self):
        user   = clsUser()          
        result = user.findUserName('PeroLitox16.drkO')
        self.assertEqual(result,[],"Elemento no encontrado")

    def test_28FindNameLongName17(self):
        user   = clsUser()
        result = user.findUserName('AjmvZanm1234Team1') 
        self.assertFalse(result, "Cadena no válida")
         
    # Casos Malicia    
    def test_29FindNameNotString(self):
        user   = clsUser()
        result = user.findUserName(1254)
        self.assertFalse(result,"Elemento Insertado") 

    def test_30FindNameNoneString(self):
        user   = clsUser()
        result = user.findUserName(None)
        self.assertFalse(result,"Válido") 

    # Casos de prueba para deleteUserName
    
    # Casos Normales
    def test_25DeleteName(self):
         user   = clsUser()
         result = user.deleteUserName("mr.carlos")
         self.assertTrue(result)
         
    # Casos Fronteras
    def test_26DeleteName1(self):
        user   = clsUser()
        result = user.deleteUserName("astridjhc")
        self.assertTrue(result)

    def test_27DeleteName0(self):
        user   = clsUser()
        result = user.deleteUserName(" ")
        self.assertFalse(result,"Válido")
        
    def test_28DeleteNameNotExists(self):
        user = clsUser()
        result = user.deleteUserName("josema19")
        self.assertFalse(result, "Válido")
        
    def test_29DeleteNameNotExists(self):
        user = clsUser()
        result = user.deleteUserName(10*"Arley")
        self.assertFalse(result, "Válido")
        
    def test_30DeleteNameNotExists(self):
        user = clsUser()
        result = user.deleteUserName("T")
        self.assertFalse(result, "Válido")

    def test_31DeleteName16(self):
        user   = clsUser()
        result = user.deleteUserName(8*"cc")
        self.assertTrue(result)
        
    def test_32DeleteName17(self):
        user   = clsUser()
        result = user.deleteUserName(8*"pt" + "h")
        self.assertFalse(result,"Elemento borrado")
        
    # casos Malicia
    def test_27DeleteName0(self):
        user   = clsUser()
        result = user.deleteUserName(" ")
        self.assertFalse(result,"Válido")
        
    def test_33DeleteNameNotString(self):
        user   = clsUser()
        result = user.deleteUserName(0)
        self.assertFalse(result, "Es válida")