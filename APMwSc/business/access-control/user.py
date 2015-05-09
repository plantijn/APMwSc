'''
Created on 08/05/2015

@author: Carlos Plantijn 10-10572
@author: Luis Colorado   09-11086
         
Descripcion: Definicion de la clase clsUser junto a sus metodos para
             administrar los usuarios del sistema.
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
CONST_MINPASSWD = 8
CONST_MAXFULLNAME = 50
CONST_MAXUSERNAME = 16
CONST_MAXPASSWD = 16
CONST_MAXEMAIL = 30
 
 # Conexion con la base de datos 
dbsession = sessionmaker(bind= model.engine)
session   = dbsession()
 
class clsUser(object):
    
    def findUsername(self, username):
        """Permite buscar a un usuario por su username en la base de datos"""
        if type(username) == str:
            if len(username) >= CONST_MINLENGTH and len(username) <= CONST_MAXUSERNAME:
                found = session.query(model.User).filter(model.User.username==username).all()
                return found
        return([])


    def insertUser(self, fullname, username, password, email, iddpt, idrole):
        """Permite insertar un nuevo usuario en la base de datos"""
        
        # Chequeo del tipo de dato de los parámetros
        checkfullname = type(fullname) == str
        checkusername = type(username) == str
        checkpassword = type(password) == str
        checkemail    = type(email) == str
        checkiddpt    = type(iddpt) == int
        checkidrole   = type(idrole) == int
        
        checkconditions = checkfullname and checkusername and checkpassword and checkemail and checkiddpt and checkidrole
        
        if checkconditions:

            # Chequeo de la longitud de los parámetros
            checkfullname = CONST_MINLENGTH <= len(fullname) <= CONST_MAXFULLNAME
            checkusername = CONST_MINLENGTH <= len(username) <= CONST_MAXUSERNAME
            checkpassword = CONST_MINPASSWD <= len(password) <= CONST_MAXPASSWD
            checkemail    = CONST_MINLENGTH <= len(email) <= CONST_MAXEMAIL
                       
            checkconditions = checkfullname and checkusername and checkpassword and checkemail

            if checkconditions:
                findUserName = self.findUserName(username)
        
                if findUserName == []:
                    newuser = model.User(fullname,username,password,email,iddpt,idrole)
                    session.add(newuser)
                    session.commit()
                    inserted = self.findUserName(newuser.username)
                    return (inserted != [])
        return False
    
    def modifyUser(self, fullname, username, password, email, iddpt, idrole):       
        """Permite modificar"""
        # Verificacion de los tipos de los parametros del metodo
        validFullname = type(fullname) == str
        validUsermame = type(username) == str
        validPassword = type(password) == str
        validEmail = type(email) == str
        validIddpt = type(iddpt) == int
        validIdrole = type(idrole) == int
        if ((validFullname) and (validUsermame) and (validPassword) and (validEmail) and (validIddpt) and (validIdrole)):
            # Verificacion de la longitud de los parametros del metodo
            lenFullname = CONST_MINLENGTH <= len(fullname) <= CONST_MAXFULLNAME
            lenUsername = CONST_MINLENGTH <= len(username) <= CONST_MAXUSERNAME
            lenPassword = CONST_MINPASSWD <= len(password) <= CONST_MAXPASSWD
            lenEmail = CONST_MINLENGTH <= len(email) <= CONST_MAXEMAIL
            
        # buscar username
        
        # si existe 
        
        # buscar iddpt
        
        # buscar idrole
        
        # si existen, hacemos update de todos los parametros
        
        
        
    def deleteUser(self, username):
        pass

if __name__ == '__main__':
    a = clsUser()
    a.insertUser('Luis', 'oskcolorado', '123456', 'oskcolorado@gmail.com', 1, 1)
    print("Hola")