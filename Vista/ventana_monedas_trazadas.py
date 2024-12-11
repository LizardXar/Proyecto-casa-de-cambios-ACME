from tkinter import Frame, Label, Button
from tkinter import ttk  # Import ttk module for Treeview

class ListViewMonedasTrazadas(Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Lista de Monedas Más Trazadas")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Replace Listbox with Treeview
        self.treeview = ttk.Treeview(self, columns=("Moneda", "Trazada"), show="headings")
        self.treeview.grid(row=1, column=0, padx=(0, 30), sticky="e")

        # Define columns and headings
        self.treeview.heading("Moneda", text="Moneda")
        self.treeview.heading("Trazada", text="Trazada")

        # Configure column width
        self.treeview.column("Moneda", width=100)
        self.treeview.column("Trazada", width=100)

        # Button to return to the menu
        self.return_btn = Button(self, text="Retornar menú")
        self.return_btn.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    def listar_monedas(self, lista_monedas):
        # Clear previous entries in the treeview
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        
        # Insert new rows into the treeview
        for i, moneda in lista_monedas[1].items():
            self.treeview.insert("", "end", values=(moneda['moneda'], moneda['trazada']))
