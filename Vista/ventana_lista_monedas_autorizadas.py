from tkinter import Frame, Label, Button
from tkinter import ttk

class VistaListaActivos(Frame):
    
    # Inicializa la vista para mostrar la lista de monedas autorizadas
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configura la grilla para la disposición de los widgets
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Título de la vista de lista de monedas autorizadas
        self.header = Label(self, text="Lista de Monedas Autorizadas")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Configura el Treeview para mostrar la información de las monedas
        self.treeview = ttk.Treeview(self, columns=("Código", "Nombre", "Tipo"), show="headings", selectmode="browse")
        self.treeview.grid(row=1, column=0, padx=(0, 30), sticky="e")

        # Encabezados de las columnas del Treeview
        self.treeview.heading("Código", text="Código")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Tipo", text="Tipo de cambio")

        # Ancho de las columnas
        self.treeview.column("Código", width=50)
        self.treeview.column("Nombre", width=50)
        self.treeview.column("Tipo", width=100)

        # Botón para retornar al menú principal
        self.return_btn = Button(self, text="Retornar menu")
        self.return_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    # Lista las monedas autorizadas en el Treeview a partir de un diccionario de datos DTO
    def listar_monedas_autorizadas(self, lista_DTO): 
        # Limpia las filas actuales del Treeview
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Inserta las nuevas filas en el Treeview
        for i, moneda_dto in lista_DTO[1].items():
            self.treeview.insert("", "end", values=(moneda_dto['codigo'], moneda_dto['nombre'], moneda_dto['tipo']))
