# -*- coding: utf-8 -*-. 
'''
Created on 08/05/2015

@author: Carlos
         Luis Colorado
         
Descripción: Defición de la clase clsRole que contiene los métodos necesarios para
             administrar los roles que juegan los usuaros del sistema.
'''


# Librerías a utilizar.

import os
import sys

# Ruta que permite utilizar el módulo model.py
sys.path.append('../../data')
import model

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Declaración de constantes
CONST_MINLEN = 1
CONST_MAXLEN = 50

# Conexión con la base de datos. 
dbsession = sessionmaker(bind= model.engine)
session   = dbsession()
 

class clsRole(object):

    def findNameRole(self, name):
        """Permite buscar un elemento en la base de datos"""
        if type(name) == str:
            if len(name) >= CONST_MINLEN and len(name) <= CONST_MAXLEN:
                found = session.query(model.Role).filter(model.Role.namerole==name).all()
                return found
        return([])
        
    def findIdRole(self, id):
        """Permite buscar un identificador en la base de datos"""
        if type(id) == int:
            found = session.query(model.Role).filter(model.Role.idrole==id).all()
            return found
        return([])
        
    def insertRole(self, namerole):
        """Permite insertar un nuevo rol en la base de datos"""
        if type(namerole) == str:
            if len(namerole) >= CONST_MINLEN and len(namerole) <= CONST_MAXLEN:  
                findName = self.findNameRole(namerole)
        
                if findName == []:
                    newrole = model.Role(namerole)
                    session.add(newrole)
                    session.commit()
                    inserted = self.findIdRole(newrole.idrole)
                    return (inserted != [])
        return False
        pass
                
    def modifyNameRole(self, name, newNameRole):
        pass   
        
    def deleteIdRole(self, id):
        pass
        
    def deleteNameRole(self, name):
        pass