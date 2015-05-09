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


    # Prueba 1
    def test1InsertExists(self):
        # Agregando Roles
        newrole = model.Role("Product Owner")
        session.add(newrole)
        session.commit()
        
        newrole = model.Role("Scrum Master")
        session.add(newrole)
        session.commit()

        newrole = model.Role("Team Master")
        session.add(newrole)
        session.commit()

        # Agregando departamentos
        newdpt = model.Dpt("Matemáticas")
        session.add(newdpt)
        session.commit()

        
        
        newdpt = model.Dpt("Computación")
        session.add(newdpt)
        session.commit()

        
        newdpt = model.Dpt("Mecánica")
        session.add(newdpt)
        session.commit()

        
        newdpt = model.Dpt("Física")
        session.add(newdpt)
        session.commit()

        
        
        newdpt = model.Dpt("Materiales")
        session.add(newdpt)
        session.commit()

        newuser = clsUser()
        newuser.insertUser("Luis","oskcolorado","c0l0r4D0!","oskcolorado@gmail.com",1,1)
    
    # Casos Normales

    # Prueba 2    
    def test2InsertUser(self):        
        newuser = clsUser()
        result = newuser.insertUser("Carlos","mr.carlos","C4rl0sPlan.","carlosplantijn@gmail.com",2,2)
        self.assertTrue(result)

    # Prueba 3    
    def test3InsertUser(self):        
        newuser = clsUser()
        result = newuser.insertUser("Astrid","astridjhc","4Str1d.30","astridjhc@gmail.com",3,3)
        self.assertTrue(result)

    # Casos Fronteras
    
    # Prueba 4
    def test4InsertIDS1(self):
        newuser = clsUser()
        result = newuser.insertUser("Jose","josema","12345678","josema@hotmail.com",1,1)    
        self.assertTrue(result)

    # Prueba 5
    def test5InsertName1(self):
        newuser = clsUser()
        result = newuser.insertUser("Leo","leotms","87654321","leotms@yahoo.com",4,3)    
        self.assertTrue(result)
        
              
    # Pruebas para ModifyName

     
    # Pruebas para FindName

    
    # Pruebas para DeleteId


    def testDeleteNameExists(self):
        user = clsUser()
        user.deleteUserName("oskcolorado")
        

    # Casos Normales

    # Prueba 
    def testDeleteName(self):
         user   = clsUser()
         result = user.deleteUserName("mr.carlos")
         self.assertTrue(result)
         
    # Casos Fronteras
    
     # Prueba
    def testDeleteName1(self):
        user   = clsUser()
        result = user.deleteUserName("astridjhc")
        self.assertTrue(result)

    # Prueba
    def testDeleteName0(self):
        user   = clsUser()
        result = user.deleteUserName(" ")
        self.assertFalse(result,"Válido")
        
    def testDeleteNameNotExists(self):
        user = clsUser()
        result = user.deleteUserName("josema19")
        self.assertFalse(result, "Válido")

