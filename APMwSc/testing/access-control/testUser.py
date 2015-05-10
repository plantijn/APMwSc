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
    
    # Pruebas para ModifyName

     
    # Pruebas para FindName

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

