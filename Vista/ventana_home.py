from tkinter import Frame, Label, Button

class HomeView(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="Menu principal")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.list_active_btn = Button(self, text="Listar monedas Activas")
        self.list_active_btn.grid(row=2, column=0, padx=10, pady=10)
        
        
        self.list_all_btn = Button(self, text="Listar todas las monedas")
        self.list_all_btn.grid(row=3, column=0, padx=10, pady=10)