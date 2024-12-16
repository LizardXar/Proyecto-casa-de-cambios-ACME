from tkinter import Frame, Label, Button
from tkinter import ttk

class VistaListaSaldoCaja(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configuración de la grilla
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Encabezado
        self.header = Label(self, text="Saldo de la caja")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Nuevo Label para mostrar el saldo CLP
        self.saldo_clp_label = Label(self, text="Saldo en CLP: $0.00", anchor="w")
        self.saldo_clp_label.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="w")

        # TreeView para listar monedas y saldo
        self.treeview = ttk.Treeview(self, columns=("Moneda", "Saldo"), show="headings")
        self.treeview.grid(row=2, column=0, padx=(0, 30), sticky="e")

        self.treeview.heading("Moneda", text="Moneda")
        self.treeview.heading("Saldo", text="Saldo")

        self.treeview.column("Moneda", width=100)
        self.treeview.column("Saldo", width=100)

        # Botón para retornar al menú
        self.return_btn = Button(self, text="Retornar")
        self.return_btn.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
    def listar_saldo(self, lista_DTO): 
        # Limpiar el TreeView
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Insertar saldos en el TreeView
        for i, saldo in lista_DTO[1].items():
            self.treeview.insert("", "end", values=(saldo['moneda'], saldo['saldo']))


