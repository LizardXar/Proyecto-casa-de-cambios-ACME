from tkinter import Frame, Label, Button
from tkinter import ttk  # Importar el módulo ttk para Treeview

class VistaListaMonedasTrazadas(Frame):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Lista de Monedas Más Trazadas")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


        # Reemplazar Listbox con Treeview
        self.treeview = ttk.Treeview(self, columns=("Moneda", "Trazada"), show="headings")
        self.treeview.grid(row=1, column=0, padx=(0, 30), sticky="e")

        # Definir columnas y encabezados
        self.treeview.heading("Moneda", text="Moneda")
        self.treeview.heading("Trazada", text="Trazada")

        # Configurar ancho de columna
        self.treeview.column("Moneda", width=100)
        self.treeview.column("Trazada", width=100)

        # Botón para retornar al menú
        self.return_btn = Button(self, text="Retornar menú")
        self.return_btn.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    def listar_monedas(self, lista_monedas):
        # Limpiar entradas anteriores en el treeview
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        
        # Insertar nuevas filas en el treeview
        for i, moneda in lista_monedas[1].items():
            self.treeview.insert("", "end", values=(moneda['moneda'], moneda['trazada']))
