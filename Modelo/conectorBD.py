# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:01:03 2024

@author: Carlos Luco Montofré
"""

import mysql.connector


class ConectorBD:

    def __init__(self, hostdb, userdb, passwordb, basedatosdb):
        self.__hostdb = hostdb
        self.__userdb = userdb
        self.__passwordb = passwordb
        self.__basedatosdb = basedatosdb

        
    def activarConexion(self):

        try:
            self.conexion = mysql.connector.connect(
                host = self.getHost(),
                user = self.getUser(),
                password = self.getPassword(),
                database = self.getBasedatos()
            )

            self.cursor = self.conexion.cursor()
  
        except Exception as e:
            print('DRIVER={MySQL};SERVER=' + self.getHost() +
                ';DATABASE='+ self.getBasedatos() + ';UID='+ self.getUser() +
                ';PWD='+ self.getPassword(),"Falló Conexión")

            return 66, e      


    def ejecutarSelectOne(self, sql):

        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()

            return 0, datos
        
        except Exception as e:

            self.realizarRollback()
            return 1, e


    def ejecutarSelectAll(self, sql):

        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()

            return 0, datos
        
        except Exception as e:
            self.realizarRollback()
            return 1, e


    def ejecutarInsert(self, sql):

        try:
            self.cursor.execute(sql)
            self.realizarCommit()

            return 0
        
        except Exception as e:
            self.realizarRollback()
            return 1, e


    def ejecutarDelete(self, sql):

        try:
            self.cursor.execute(sql)
            self.realizarCommit()

            return 0
        
        except Exception as e:
            self.realizarRollback()
            return 1, e


    def ejecutarUpdate(self, sql):

        try:
            self.cursor.execute(sql)
            self.realizarCommit()

            return 0
        
        except Exception as e:
            self.realizarRollback()
            return 1, e


    def getHost(self):
        return self.__hostdb


    def getUser(self):
        return self.__userdb


    def getPassword(self):
        return self.__passwordb

    
    def getBasedatos(self):
        return self.__basedatosdb


    def realizarCommit(self):
        self.conexion.commit()


    def realizarRollback(self):
        self.conexion.rollback()  


    def desactivarConexion (self):
        self.conexion.close()
