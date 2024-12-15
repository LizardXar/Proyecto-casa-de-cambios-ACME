from tkinter import Frame, Label, Button

class VistaInicioEjecutivo(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="Menu principal ejecutivo")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.greeting = Label(self, text="")
        self.greeting.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.list_active_btn = Button(self, text="Listar monedas Activas")
        self.list_active_btn.grid(row=2, column=0, padx=10, pady=10)
        
        
        self.list_all_btn = Button(self, text="Listar todas las monedas")
        self.list_all_btn.grid(row=3, column=0, padx=10, pady=10)

        self.list_all_cajas_btn = Button(self, text="Listar todas las cajas")
        self.list_all_cajas_btn.grid(row=4, column=0, padx=10, pady=10)

        self.realizar_transaccion_btn = Button(self, text="Realizar Transacción")
        self.realizar_transaccion_btn.grid(row=4, column=0, padx=10, pady=10)

        self.signout_btn = Button(self, text="Salir")
        self.signout_btn.grid(row=5, column=0, padx=10, pady=10)
