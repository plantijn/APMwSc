import unittest
import os
import sys
from xmlrpc.client import MAXINT
from urllib.parse import ResultBase

# Ruta que permite utilizar el módulo model.py
sys.path.append('../../business/access-control')

from role import clsRole

class TestcslRole(unittest.TestCase):
 
    #        Pruebas para clsRole
    
    # Pruebas para insertRol
    
    # Casos Normales
    def test1InsertExists(self):
        role = clsRole()
        role.insertRole('Scrum Master')  
    
    def test2InsertExists(self):
        role = clsRole()
        role.insertRole('Product Owner') 
    
    def test3InsertExists(self):
        role = clsRole()
        role.insertRole('Team Member')  
    
    # Casos bordes
    def test4InsertNotExists(self):
        role = clsRole()
        result = role.insertRole('Estudiante')
        self.assertFalse(result)
        
    def test10_12InsertNotExists(self):
        role = clsRole()
        result = role.insertRole('a'*1)
        self.assertFalse(result)
        
    def test10_13InsertNotExists(self):
        role = clsRole()
        result = role.insertRole('a'*50)
        self.assertFalse(result)
        
    def test10_20InsertNotExists(self):
        role = clsRole()
        result = role.insertRole('a'*51)
        self.assertFalse(result)
    
    def test10_20_21InsertNotExists(self):
        role = clsRole()
        result = role.insertRole('a'*0)
        self.assertFalse(result)
        
    #def test10_14InsertNotExists(self):
    #    role = clsRole()
    #    result = role.insertRole('a'* ((2^500000000)-1) )
    #   self.assertFalse(result)
        
    # Casos Malicia    
    def test9InsertNotExists(self):
        role = clsRole()
        result = role.insertRole(3456788765)
        self.assertFalse(result)
    
    def test10InsertNotExists(self):
        role = clsRole()
        result = role.insertRole('')
        self.assertFalse(result)
        
    def test10_11InsertNotExists(self):
        role = clsRole()
        result = role.insertRole(None)
        
    def test10_15InsertNotExists(self):
        role = clsRole()
        result = role.insertRole(True)
        
    def test10_16InsertNotExists(self):
        role = clsRole()
        result = role.insertRole(False)
        
    def test10_17InsertNotExists(self):
        role = clsRole()
        result = role.insertRole([MAXINT])
        
    def test10_18InsertNotExists(self):
        role = clsRole()
        result = role.insertRole({MAXINT})
    
    def test10_20_22InsertNotExists(self):
        role = clsRole()
        result = role.insertRole('a'*-1)
        self.assertFalse(result)
        
    def test10_20_23InsertNotExists(self):
        role = clsRole()
        result = role.insertRole('a'*-(MAXINT))
        self.assertFalse(result)
        
    # Pruebas para modifyRol
    
    # Casos Normales        
    def test5ModifyNameRole(self):
        role = clsRole()
        role.modifyNameRole('Product Owner', 'Team Member')
        
    def test6ModifyNameRole(self):
        role = clsRole()
        role.modifyNameRole('Scrum Master', 'Team Member')

    def test7ModifyNameRole(self):
        role = clsRole()
        role.modifyNameRole('Team Member', 'Team Member')
        
    # Casos frontera
    def test10_19ModifyNameRole(self):
        role = clsRole()
        result = role.modifyNameRole('Product Owner', 'Luis')
        self.assertFalse(result)
        
    def test10_20_24ModifyNameRole(self):
        role = clsRole()
        result = role.modifyNameRole('Product Owner', '')
        self.assertFalse(result)
        
    def test10_20_25ModifyNameRole(self):
        role = clsRole()
        result = role.modifyNameRole('', '')
        self.assertFalse(result)
        
    def test10_20_26ModifyNameRole(self):
        role = clsRole()
        result = role.modifyNameRole('', 'Team Member')
        self.assertFalse(result)
        
    def test10_20_27ModifyNameRole(self):
        role = clsRole()
        result = role.modifyNameRole('Carlos', 'Team Member')
        self.assertFalse(result)
    
    # Casos Malicia
    def test10_20_28ModifyNameRole(self):
        role = clsRole()
        result = role.modifyNameRole({}, 'Team Member')
        self.assertFalse(result)
        
    def test10_20_29ModifyNameRole(self):
        role = clsRole()
        result = role.modifyNameRole([], 'Team Member')
        self.assertFalse(result)
        
    def test10_20_30ModifyNameRole(self):
        role = clsRole()
        result = role.modifyNameRole([MAXINT], 'Team Member')
        self.assertFalse(result)
        
    def test10_20_31ModifyNameRole(self):
        role = clsRole()
        result = role.modifyNameRole({MAXINT}, 'Team Member')
        self.assertFalse(result)
        
    def test10_20_32ModifyNameRole(self):
        role = clsRole()
        result = role.modifyNameRole('Team Member',{})
        self.assertFalse(result)
        
    def test10_20_33ModifyNameRole(self):
        role = clsRole()
        result = role.modifyNameRole('Team Member',[])
        self.assertFalse(result)
        
    def test10_20_34ModifyNameRole(self):
        role = clsRole()
        result = role.modifyNameRole('Team Member',[MAXINT])
        self.assertFalse(result)
        
    def test10_20_35ModifyNameRole(self):
        role = clsRole()
        result = role.modifyNameRole('Team Member',{MAXINT})
        self.assertFalse(result)
    
    def test10_20_36ModifyNameRole(self):
        role = clsRole()
        result = role.modifyNameRole('Team Member',1234)
        self.assertFalse(result)
    
    def test10_20_37ModifyNameRole(self):
        role = clsRole()
        result = role.modifyNameRole(1234,'Team Member')
        self.assertFalse(result)
    
    
    # Pruebas para deleteRol
    
    # Casos Normales     
    def test8DeleteIdRole(self):
        role = clsRole()
        result = role.deleteIdRole(1)
        self.assertTrue(result)
        
    # Casos Frontera
    def test10_20_38DeleteIdRoleNotExist(self):
        role = clsRole()
        result = role.deleteIdRole(1)  
        self.assertFalse(result)
    
    def test10_20_39DeleteIdRoleNotExist(self):
        role = clsRole()
        result = role.deleteIdRole((2^38)-1)  
        self.assertFalse(result)
        
    def test10_20_30_1DeleteIdRoleNotExist(self):
        role = clsRole()
        result = role.deleteIdRole(-((2^38)-1))  
        self.assertFalse(result)    
    
    # Casos Malicia    
    def test10_20_30_2DeleteIdRoleNotExist(self):
        role = clsRole()
        result = role.deleteIdRole("a")  
        self.assertFalse(result)  
        
    def test10_20_30_3DeleteIdRoleNotExist(self):
        role = clsRole()
        result = role.deleteIdRole("a"*((2^38)-1) )  
        self.assertFalse(result)  
        
    def test10_20_30_4DeleteIdRoleNotExist(self):
        role = clsRole()
        result = role.deleteIdRole("a"*(-((2^38)-1)) )  
        self.assertFalse(result) 
        
    def test10_20_30_5DeleteIdRoleNotExist(self):
        role = clsRole()
        result = role.deleteIdRole("")  
        self.assertFalse(result)     
        
    def test10_20_30_6DeleteIdRoleNotExist(self):
        role = clsRole()
        result = role.deleteIdRole(True)  
        self.assertFalse(result)
        
    def test10_20_30_7DeleteIdRoleNotExist(self):
        role = clsRole()
        result = role.deleteIdRole(False)  
        self.assertFalse(result)
        
    def test10_20_30_8DeleteIdRoleNotExist(self):
        role = clsRole()
        result = role.deleteIdRole(False)  
        self.assertFalse(result)
        
    def test10_20_30_9DeleteIdRoleNotExist(self):
        role = clsRole()
        result = role.deleteIdRole(None)  
        self.assertFalse(result)
        
    def test10_20_30_40_1DeleteIdRoleNotExist(self):
        role = clsRole()
        result = role.deleteIdRole({})  
        self.assertFalse(result)
        
    def test10_20_30_40_2DeleteIdRoleNotExist(self):
        role = clsRole()
        result = role.deleteIdRole([])  
        self.assertFalse(result)
           
    def test10_20_30_40_3DeleteIdRoleNotExist(self):
        role = clsRole()
        result = role.deleteIdRole({MAXINT})  
        self.assertFalse(result)
        
    def test10_20_30_40_4DeleteIdRoleNotExist(self):
        role = clsRole()
        result = role.deleteIdRole([MAXINT])  
        self.assertFalse(result)    
    
        
        
        
        
        
        
        
        