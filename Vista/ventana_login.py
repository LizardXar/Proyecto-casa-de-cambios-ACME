# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:01:25 2024

@author: Carlos Luco Montofré
"""

from tkinter import Frame, Label, Entry, Button

class VistaLogin(Frame):
    
    # Inicializa la vista para el login de usuarios
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configura la disposición de la grilla
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # Título de la vista de login
        self.header = Label(self, text="Ingreso a una cuenta existente")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Etiqueta y campo de entrada para el correo
        self.username_label = Label(self, text="Correo")
        self.username_input = Entry(self)
        self.username_label.grid(row=1, column=0, padx=10, sticky="w")
        self.username_input.grid(row=1, column=1, padx=(0, 20), sticky="ew")

        # Etiqueta y campo de entrada para la contraseña
        self.password_label = Label(self, text="Contraseña")
        self.password_input = Entry(self, show="*")
        self.password_label.grid(row=2, column=0, padx=10, sticky="w")
        self.password_input.grid(row=2, column=1, padx=(0, 20), sticky="ew")

        # Botón para iniciar sesión
        self.login_btn = Button(self, text="Iniciar sesión")
        self.login_btn.grid(row=3, column=1, padx=0, pady=10, sticky="w")
             
        # Botón para cerrar el sistema
        self.close_btn = Button(self, text="Cerrar sistema")
        self.close_btn.grid(row=7, column=1, padx=0, pady=10, sticky="w")
        
    # Obtiene los datos ingresados en los campos de entrada y los devuelve en un diccionario DTO
    def data_signin(self):
        username = self.username_input.get()
        pasword = self.password_input.get()
        data_dto = {"correo": username, "clave": pasword}
        self.password_input.delete(0, last=len(pasword))  # Limpia el campo de la contraseña
        return data_dto
