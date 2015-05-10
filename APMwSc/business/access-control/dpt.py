# -*- coding: utf-8 -*-. 
'''
Created on 08/05/2015

@author: Carlos Plantijn 10-10572
@author: Luis Colorado   09-11086
         
Descripcion: Definicion de la clase clsDpt junto a sus metodos para
             administrar los departamentos a los cuales estan adscritos 
             los usuarios del sistema.
'''


# Librerias a utilizar
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
 

class clsDpt(object):

    def findNameDpt(self, name):
        """Permite buscar un departamento por su nombre en la base de datos"""
        if type(name) == str: # Verificacion de que el nombre sea de tipo String
            if len(name) >= CONST_MINLENGTH and len(name) <= CONST_MAXLENGTH:
                found = session.query(model.Dpt).filter(model.Dpt.namedpt==name).all()
                return found
            return([])
        return([])
        
    def findIdDpt(self, id):
        """Permite buscar un departamento por su id (identificador) en la base de datos"""
        if type(id) == int:    # Verificacion de que el id sea de tipo entero 
            found = session.query(model.Dpt).filter(model.Dpt.iddpt==id).all()
            return found
        return([])
        
    def insertDpt(self, namedpt):
        """Permite insertar un nuevo departamento en la base de datos"""
        if type(namedpt) == str:  # Verificacion de que el nombre sea de tipo String
            if len(namedpt) >= CONST_MINLENGTH and len(namedpt) <= CONST_MAXLENGTH:  
                findName = self.findNameDpt(namedpt)
        
                if findName == []:
                    newdpt = model.Dpt(namedpt)
                    session.add(newdpt)
                    session.commit()
                    # Verificacion de que hemos agregado el nuevo departamento
                    inserted = self.findIdDpt(newdpt.iddpt)
                    return (inserted != [])
                return False
            return False
        return False

    def modifyNameDpt(self, name, newNameDpt):
        """Permite modificar el nombre de un rol en la base de datos"""
        # Verificacion de que los nombres del departamento sean de tipo String
        validname    = (type(name) == str)
        validnewname = (type(newNameDpt) == str)  
        if ((validname) and (validnewname)):
            # Verificacion de la longitud de los nombre de los departamentos
            lengthname    = CONST_MINLENGTH <= len(name) <= CONST_MAXLENGTH
            lengthnewname = CONST_MINLENGTH <= len(newNameDpt) <= CONST_MAXLENGTH
            if ((lengthname) and (lengthnewname)):                
                # Verificacion de que existe el departamento a modificar
                found1 = self.findNameDpt(name)
                # Verificacion de que no existe el nuevo nombre de departamento
                found2 = self.findNameDpt(newNameDpt)
                if (found1 != []) and (found2 == []):
                    session.query(model.Dpt).filter(model.Dpt.namedpt == name).update({'namedpt':(newNameDpt)})
                    session.commit()
                    return True
                return False
            return False
        return False    
        
    def deleteIdDpt(self, id):
        """Permite eliminar un rol por su id (identificador) de la base de datos"""
        if type(id) == int:    # Verificacion de que el id sea de tipo entero 
            findId = self.findIdDpt(id)
            if findId != []:
                session.query(model.Dpt).filter(model.Dpt.iddpt == id).delete()
                session.commit()
                return True
            return False
        return False    
