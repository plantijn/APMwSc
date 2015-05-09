# -*- coding: utf-8 -*-. 
'''
Created on 09/5/2015
@author: Carlos Plantijn
         Luis Colorado
         
Descripción: 
'''

# Librerías a utilizar.

import os
import sys
from _ast import Str

# Ruta que permite utilizar el módulo model.py
sys.path.append('../../data')
import model

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Declaración de constantes
CONST_MINLEN = 1
CONST_FULLNAME_MAXLEN = 50
CONST_USERNAME_MAXLEN = 16
CONST_PASSWORD_MINLEN = 8
CONST_PASSWORD_MAXLEN = 16
CONST_EMAIL_MAXLEN    = 30 

# Conexión con la base de datos. 
dbsession = sessionmaker(bind= model.engine)
session   = dbsession()


class clsUser(object):

    def findUserName(self, name):
        """Permite buscar un elemento en la base de datos"""
        if type(name) == str:
            if len(name) >= CONST_MINLEN and len(name) <= CONST_USERNAME_MAXLEN:
                found = session.query(model.User).filter(model.User.username==name).all()
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
            checkfullname = CONST_MINLEN <= len(fullname) <= CONST_FULLNAME_MAXLEN
            checkusername = CONST_MINLEN <= len(username) <= CONST_USERNAME_MAXLEN
            checkpassword = CONST_PASSWORD_MINLEN <= len(password) <= CONST_PASSWORD_MAXLEN
            checkemail    = CONST_MINLEN <= len(email) <= CONST_EMAIL_MAXLEN
                       
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

    def modifyUserName(self, newfullname, username, newpassword, newemail, newiddpt, newidrole):
        """Permite modificar un usuario que esté en la base de datos"""

        # Chequeo del tipo de dato de los parámetros
        checkfullname = type(newfullname) == str
        checkusername = type(username) == str
        checkpassword = type(newpassword) == str
        checkemail    = type(newemail) == str
        checkiddpt    = type(newiddpt) == int
        checkidrole   = type(newidrole) == int
        
        checkconditions = checkfullname and checkusername and checkpassword and checkemail and checkiddpt and checkidrole
        
        if checkconditions:

            # Chequeo de la longitud de los parámetros
            checkfullname = CONST_MINLEN <= len(newfullname) <= CONST_FULLNAME_MAXLEN
            checkusername = CONST_MINLEN <= len(username) <= CONST_USERNAME_MAXLEN
            checkpassword = CONST_MINLEN <= len(newpassword) <= CONST_PASSWORD_MAXLEN
            checkemail    = CONST_MINLEN <= len(newemail) <= CONST_EMAIL_MAXLEN
                       
            checkconditions = checkfullname and checkusername and checkpassword and checkemail

            if checkconditions:
                findUserName = self.findUserName(username)
                if findUserName != []:
                    foundiddpt  = session.query(model.Dpt).filter(model.Dpt.iddpt == newiddpt).all()
                    foundidrole = session.query(model.Role).filter(model.Role.idrole==newidrole).all()
                    if (foundiddpt != [] and foundidrole != []):
                        session.query(model.User).filter(model.User.username == username).update({'fullname':(newfullname)})
                        session.query(model.User).filter(model.User.username == username).update({'password':(newpassword)})
                        session.query(model.User).filter(model.User.username == username).update({'email':(newemail)})
                        session.query(model.User).filter(model.User.username == username).update({'iddpt':(newiddpt)})
                        session.query(model.User).filter(model.User.username == username).update({'idrole':(newidrole)})                        
                        session.commit()
                    return True
        return False

    def deleteUserName(self, username):
        """Permite eliminar un elemento de la base de datos por identificador"""
        if (type(username) == str):
            findNameUser = self.findUserName(username)
            if findNameUser != []:
                session.query(model.User).filter(model.User.username == username).delete()
                session.commit()
                findNameUser = self.findUserName(username)
                return (findNameUser == [])
