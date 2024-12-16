from tkinter import Frame, Label, Button
from tkinter import ttk

class VistaListaGanancias(Frame):
    
    # Inicializa la vista para mostrar la lista de ganancias
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configura la grilla para la disposición de los widgets
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Título de la vista de lista de ganancias
        self.header = Label(self, text="Lista de Ganancias")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Configura el Treeview para mostrar la información de las ganancias
        self.treeview = ttk.Treeview(self, columns=("Moneda", "Monto", "Ganancia"), show="headings")
        self.treeview.grid(row=1, column=0, padx=(0, 30), sticky="e")

        # Encabezados de las columnas del Treeview
        self.treeview.heading("Moneda", text="Moneda")
        self.treeview.heading("Monto", text="Monto")
        self.treeview.heading("Ganancia", text="Ganancia")

        # Ancho de las columnas
        self.treeview.column("Moneda", width=100)
        self.treeview.column("Monto", width=100)
        self.treeview.column("Ganancia", width=100)

        # Botón para retornar al menú principal
        self.return_btn = Button(self, text="Retornar al menú")
        self.return_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    # Lista las ganancias en el Treeview a partir de un diccionario de datos DTO
    def listar_ganancias(self, lista_DTO): 
        # Limpia las filas actuales del Treeview
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        
        # Inserta las nuevas filas en el Treeview
        for i, ganancia_dto in lista_DTO[1].items():
            self.treeview.insert("", "end", values=(ganancia_dto['moneda'], ganancia_dto['monto'], ganancia_dto['ganancia']))
