# -*- coding: utf-8 -*-. 
'''
Created on 03/5/2015
@author: Carlos
         Luis Colorado
         
Descripción: 
'''

# Librerías a usar

import conexiondb

import os
from flask import Flask
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

app = Flask(__name__) 

# Instancia de la base de datos
db = declarative_base(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Definición de las tablas de la base de datos

# Definicion modelo usuario.
class User(db):
    __tablename__ = 'users'
    fullname = Column(String(50), index = True)
    username = Column(String(16), primary_key = True)
    email    = Column(String(30), index = True, unique = True)
    password = Column(String(16), index = True)
    iddpt    = Column(Integer, ForeignKey('dpts.iddpt'))
    idrole   = Column(Integer, ForeignKey('roles.idrole'))
    
    def __init__(self, fullname, username, password, email, iddpt, idrole):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email    = email
        self.iddpt    = iddpt
        self.idrole   = idrole
        
# Definicion modelo departamento.
class Dpt(db):
    
     __tablename__ = 'dpts' 
     iddpt    = Column(Integer, primary_key = True)
     namedpt  = Column(String(50), index = True, unique = True)
     usersdpt = relationship('User', backref = 'dpt', cascade = "all, delete, delete-orphan")
     
     def __init__(self, iddpt, namedpt):
         self.iddpt   = iddpt
         self.namedpt = namedpt
         
# Definicion modelo rol.
class Role(db):
    
     __tablename__ = 'roles'
     idrole    = Column(Integer, primary_key = True)
     namerole  = Column(String(50), index = True, unique = True)
     usersrole = relationship('User', backref = 'role', cascade = "all, delete, delete-orphan")
          
     def __init__(self, namerole):
         self.namerole = namerole 
         
# Creamos el motor de almacenamiento para la base de datos local.
engine = create_engine(URL(**conexiondb.DATABASE))

# Borramos las tablas de la base de datos
db.metadata.drop_all(engine)

# Creamos las tablas de la base de datos.
db.metadata.create_all(engine)
     
if __name__ == '__name__':
    manager.run

