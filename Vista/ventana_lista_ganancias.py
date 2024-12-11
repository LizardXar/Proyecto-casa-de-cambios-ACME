from tkinter import Frame, Label, Button
from tkinter import ttk  # Import ttk module for Treeview

class ListViewGanancias(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Lista de Ganancias")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.treeview = ttk.Treeview(self, columns=("Moneda", "Monto", "Ganancia"), show="headings")
        self.treeview.grid(row=1, column=0, padx=(0, 30), sticky="e")

        self.treeview.heading("Moneda", text="Moneda")
        self.treeview.heading("Monto", text="Monto")
        self.treeview.heading("Ganancia", text="Ganancia")

        self.treeview.column("Moneda", width=100)
        self.treeview.column("Monto", width=100)
        self.treeview.column("Ganancia", width=100)

        self.return_btn = Button(self, text="Retornar al menú")
        self.return_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    def listar_ganancias(self, lista_DTO): 
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        
        for i, ganancia in lista_DTO[1].items():
            self.treeview.insert("", "end", values=(ganancia['moneda'], ganancia['monto'], ganancia['ganancia']))
