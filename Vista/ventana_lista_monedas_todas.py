from tkinter import Frame, Label, Button
from tkinter import ttk

class VistaListaTodas(Frame):
    
    # Inicializa la vista para mostrar la lista de todas las monedas
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configura la grilla para la disposición de los widgets
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Título de la vista de lista de todas las monedas
        self.header = Label(self, text="Lista de Todas las Monedas")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Configura el Treeview para mostrar la información de las monedas
        self.treeview = ttk.Treeview(self, columns=("Código", "Nombre", "Tipo"), show="headings")
        self.treeview.grid(row=1, column=0, padx=(0, 30), sticky="e")

        # Encabezados de las columnas del Treeview
        self.treeview.heading("Código", text="Código")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Tipo", text="Tipo de cambio")

        # Ancho de las columnas
        self.treeview.column("Código", width=50)
        self.treeview.column("Nombre", width=50)
        self.treeview.column("Tipo", width=100)

        # Botón para modificar el tipo de cambio de una moneda seleccionada
        self.tipo_cambio_btn = Button(self, text="Modificar tipo de cambio")
        self.tipo_cambio_btn.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        # Botón para retornar al menú principal
        self.return_btn = Button(self, text="Retornar menu")
        self.return_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    # Lista todas las monedas en el Treeview a partir de un diccionario de datos DTO
    def listar_monedas(self, lista_DTO): 
        # Limpia las filas actuales del Treeview
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        
        # Inserta las nuevas filas en el Treeview
        for i, moneda_dto in lista_DTO[1].items():
            self.treeview.insert("", "end", values=(moneda_dto['codigo'], moneda_dto['nombre'], moneda_dto['tipo']))

    # Obtiene el código de la moneda seleccionada en el Treeview
    def obtener_cod_moneda_seleccionado(self):
        seleccion = self.treeview.selection()
        if seleccion:
            item = self.treeview.item(seleccion[0])['values']
            cod_moneda = item[0]
            return cod_moneda
        return None
