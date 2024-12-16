from tkinter import Frame, Label, Button

class VistaInicioCajero(Frame):
    
    # Inicializa la vista principal del cajero
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configura la grilla para la disposición de los widgets
        self.grid_columnconfigure(0, weight=1)

        # Título del menú principal del cajero
        self.header = Label(self, text="Menu principal Cajero")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Mensaje de bienvenida para el usuario
        self.greeting = Label(self, text="")
        self.greeting.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Botón para registrar la disponibilidad de pesos
        self.registrar_disponibilidad_btn = Button(self, text="Registrar disponibilidad de pesos")
        self.registrar_disponibilidad_btn.grid(row=2, column=0, padx=10, pady=10)

        # Botón para cerrar sesión
        self.signout_btn = Button(self, text="Salir")
        self.signout_btn.grid(row=5, column=0, padx=10, pady=10)
