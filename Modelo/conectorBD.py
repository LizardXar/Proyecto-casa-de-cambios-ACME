# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:01:03 2024

@author: Carlos Luco Montofré
"""

import mysql.connector

class ConectorBD:
    # Atributo estático para almacenar la única instancia de la clase
    _instance = None  

    # Método para controlar la creación de la instancia única (patrón Singleton)
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ConectorBD, cls).__new__(cls)
        return cls._instance

    # Inicializa los parámetros de conexión solo la primera vez
    def __init__(self, hostdb="localhost", userdb="root", passwordb="", basedatosdb="casa_ACME"):
        if not hasattr(self, 'conexion'):  # Verifica si ya se inicializó la conexión
            self.__hostdb = hostdb
            self.__userdb = userdb
            self.__passwordb = passwordb
            self.__basedatosdb = basedatosdb
            self.conexion = None
            self.cursor = None

    # Activa la conexión a la base de datos
    def activarConexion(self):
        try:
            if not self.conexion or not self.conexion.is_connected():  # Verifica si la conexión no existe o no está activa
                self.conexion = mysql.connector.connect(
                    host=self.getHost(),
                    user=self.getUser(),
                    password=self.getPassword(),
                    database=self.getBasedatos()
                )
                self.cursor = self.conexion.cursor()  # Crea el cursor de la base de datos
            return 0  # Éxito
        except Exception as e:
            print('DRIVER={MySQL};SERVER=' + self.getHost() +
                ';DATABASE='+ self.getBasedatos() + ';UID='+ self.getUser() +
                ';PWD='+ self.getPassword(), "Falló Conexión")
            return 66  # Error de conexión

    # Ejecuta una consulta SELECT que devuelve una sola fila
    def ejecutarSelectOne(self, sql):
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()  # Obtiene una única fila
            return 0, datos  # Éxito
        except Exception as e:
            self.realizarRollback()  # Revierte la transacción en caso de error
            return 1, e  # Error

    # Ejecuta una consulta SELECT que devuelve varias filas
    def ejecutarSelectAll(self, sql):
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()  # Obtiene todas las filas
            return 0, datos  # Éxito
        except Exception as e:
            self.realizarRollback()  # Revierte la transacción en caso de error
            return 1, e  # Error

    # Ejecuta una consulta INSERT
    def ejecutarInsert(self, sql):
        try:
            self.cursor.execute(sql)
            self.realizarCommit()  # Confirma la transacción
            return 0  # Éxito
        except Exception as e:
            self.realizarRollback()  # Revierte la transacción en caso de error
            return 1, e  # Error

    # Ejecuta una consulta DELETE
    def ejecutarDelete(self, sql):
        try:
            self.cursor.execute(sql)
            self.realizarCommit()  # Confirma la transacción
            return 0  # Éxito
        except Exception as e:
            self.realizarRollback()  # Revierte la transacción en caso de error
            return 1, e  # Error

    # Ejecuta una consulta UPDATE
    def ejecutarUpdate(self, sql):
        try:
            self.cursor.execute(sql)
            self.realizarCommit()  # Confirma la transacción
            return 0  # Éxito
        except Exception as e:
            self.realizarRollback()  # Revierte la transacción en caso de error
            return 1, e  # Error

    # Obtiene el nombre del host
    def getHost(self):
        return self.__hostdb

    # Obtiene el nombre de usuario de la base de datos
    def getUser(self):
        return self.__userdb

    # Obtiene la contraseña de la base de datos
    def getPassword(self):
        return self.__passwordb

    # Obtiene el nombre de la base de datos
    def getBasedatos(self):
        return self.__basedatosdb

    # Realiza el commit de la transacción
    def realizarCommit(self):
        try:
            if self.conexion and self.conexion.is_connected():  # Verifica si la conexión está activa
                self.conexion.commit()  # Realiza el commit
        except Exception as e:
            print(f"Error al realizar commit: {e}")  # Imprime el error en caso de fallo

    # Realiza el rollback de la transacción
    def realizarRollback(self):
        try:
            if self.conexion and self.conexion.is_connected():  # Verifica si la conexión está activa
                self.conexion.rollback()  # Realiza el rollback
        except Exception as e:
            print(f"Error al realizar rollback: {e}")  # Imprime el error en caso de fallo

    # Cierra la conexión con la base de datos
    def desactivarConexion(self):
        try:
            if self.conexion and self.conexion.is_connected():  # Verifica si la conexión está activa
                self.cursor.close()  # Cierra el cursor
                self.conexion.close()  # Cierra la conexión
                self.cursor = None  # Limpia el atributo cursor
                self.conexion = None  # Limpia el atributo conexión
            return 0  # Éxito
        except Exception as e:
            print(f"Error al desactivar la conexión: {str(e)}")  # Imprime el error en caso de fallo
            return 1  # Error
