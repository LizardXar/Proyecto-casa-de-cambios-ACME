from tkinter import Frame, Label, Button
from tkinter import ttk

class VistaListaTodas(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Lista de Todas las Monedas")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.treeview = ttk.Treeview(self, columns=("Código", "Nombre", "Tipo"), show="headings")
        self.treeview.grid(row=1, column=0, padx=(0, 30), sticky="e")

        self.treeview.heading("Código", text="Código")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Tipo", text="Tipo de cambio")

        self.treeview.column("Código", width=50)
        self.treeview.column("Nombre", width=50)
        self.treeview.column("Tipo", width=100)

        self.return_btn = Button(self, text="Retornar menu")
        self.return_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    def listar_monedas(self, lista_DTO): 
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        
        for i, moneda in lista_DTO[1].items():
            self.treeview.insert("", "end", values=(moneda['codigo'], moneda['nombre'], moneda['tipo']))
