from tkinter import Frame, Label, Button

class VistaInicioGerente(Frame):
    
    # Inicializa la vista principal del gerente
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configura la grilla para la disposición de los widgets
        self.grid_columnconfigure(0, weight=1)

        # Título del menú principal del gerente
        self.header = Label(self, text="Menu principal gerente")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Mensaje de bienvenida para el usuario
        self.greeting = Label(self, text="")
        self.greeting.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Botón para listar las monedas más trazadas
        self.list_monedas_trazadas_btn = Button(self, text="Listar monedas mas trazadas")
        self.list_monedas_trazadas_btn.grid(row=2, column=0, padx=10, pady=10)
        
        # Botón para listar las ganancias
        self.list_ganancias_btn = Button(self, text="Listar ganancias")
        self.list_ganancias_btn.grid(row=3, column=0, padx=10, pady=10)

        # Botón para cerrar sesión
        self.signout_btn = Button(self, text="Salir")
        self.signout_btn.grid(row=4, column=0, padx=10, pady=10)
