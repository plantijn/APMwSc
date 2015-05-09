# -*- coding: utf-8 -*-. 
'''
Created on 08/05/2015

@author: Carlos Plantijn 10-10572
@author: Luis Colorado   09-11086
         
Descripcion: Definicion de la clase clsRole junto a sus metodos para
             administrar los roles que juegan los usuaros del sistema.
'''


# Librerias a utilizar.

import os
import sys

# Ruta que permite utilizar el modulo model.py
sys.path.append('../../data')
import model

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Declaracion de constantes
CONST_MINLENGTH = 1
CONST_MAXLENGTH = 50

# Conexion con la base de datos 
dbsession = sessionmaker(bind= model.engine)
session   = dbsession()
 

class clsRole(object):

    def findNameRole(self, name):
        """Permite buscar un rol por su nombre en la base de datos"""
        if type(name) == str: # Verificacion de que el nombre sea de tipo String
            if len(name) >= CONST_MINLENGTH and len(name) <= CONST_MAXLENGTH:
                found = session.query(model.Role).filter(model.Role.namerole==name).all()
                return found
        return([])
        
    def findIdRole(self, id):
        """Permite buscar un rol por su id (identificador) en la base de datos"""
        if type(id) == int:    # Verificacion de que el id sea de tipo entero 
            found = session.query(model.Role).filter(model.Role.idrole==id).all()
            return found
        return([])
        
    def insertRole(self, namerole):
        """Permite insertar un nuevo rol en la base de datos"""
        if type(namerole) == str:  # Verificacion de que el nombre sea de tipo String
            if len(namerole) >= CONST_MINLENGTH and len(namerole) <= CONST_MAXLENGTH:  
                findName = self.findNameRole(namerole)
        
                if findName == []:
                    newrole = model.Role(namerole)
                    session.add(newrole)
                    session.commit()
                    # Verificacion de que hemos agregado el nuevo rol
                    inserted = self.findIdRole(newrole.idrole)
                    return (inserted != [])
        return False

    def modifyNameRole(self, name, newNameRole):
        """Permite modificar el nombre de un rol en la base de datos"""
        # Verificacion de que los nombres de rol sean de tipo String
        validname    = (type(name) == str)
        validnewname = (type(newNameRole) == str)  
        if ((validname) and (validnewname)):
            # Verificacion de la longitud de los nombre de los roles
            lengthname    = CONST_MINLENGTH <= len(name) <= CONST_MAXLENGTH
            lengthnewname = CONST_MINLENGTH <= len(newNameRole) <= CONST_MAXLENGTH
            if ((lengthname) and (lengthnewname)):                
                # Verificacion de que existe el rol a modificar
                found1 = self.findNameRole(name)
                # Verificacion de que no existe el nuevo nombre de rol
                found2 = self.findNameRole(newNameRole)
                if (found1 != []) and (found2 == []):
                    session.query(model.Role).filter(model.Role.namerole == name).update({'namerole':(newNameRole)})
                    session.commit()
                    return True
        return False    
        
    def deleteIdRole(self, id):
        """Permite eliminar un rol por su id (identificador) de la base de datos"""
        if type(id) == int:    # Verificacion de que el id sea de tipo entero 
            findId = self.findIdRole(id)
            if findId != []:
                session.query(model.Role).filter(model.Role.idrole == id).delete()
                session.commit()
                return True
        return False    
