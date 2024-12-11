from tkinter import Frame, Label, Button
from tkinter import ttk

class ListViewCajas(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Lista de Cajas")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.treeview = ttk.Treeview(self, columns=("Código", "Empleado", "Estado"), show="headings", selectmode="browse")
        self.treeview.grid(row=1, column=0, padx=(0, 30), sticky="e")

        self.treeview.heading("Código", text="Código")
        self.treeview.heading("Empleado", text="Empleado")
        self.treeview.heading("Estado", text="Estado")

        self.treeview.column("Código", width=50)
        self.treeview.column("Empleado", width=100)
        self.treeview.column("Estado", width=50)

        self.ver_saldo_btn = Button(self, text="Ver saldo de caja")
        self.ver_saldo_btn.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        self.return_btn = Button(self, text="Retornar menu")
        self.return_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")
 
    def listar_cajas(self, lista_DTO): 
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for i, caja in lista_DTO[1].items():
            self.treeview.insert("", "end", values=(caja['codigo'], caja['empleado'], caja['estado']))

    def obtener_cod_caja_seleccionado(self):
        seleccion = self.treeview.selection()
        if seleccion:
            item = self.treeview.item(seleccion[0])['values']
            cod_caja = item[0]
            return cod_caja
        return None
