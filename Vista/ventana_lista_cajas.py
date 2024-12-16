from tkinter import Frame, Label, Button
from tkinter import ttk

class VistaListaCajas(Frame):
    
    # Inicializa la vista para mostrar la lista de cajas
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configura la grilla para la disposición de los widgets
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Título de la vista de lista de cajas
        self.header = Label(self, text="Lista de Cajas")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Configura el Treeview para mostrar la información de las cajas
        self.treeview = ttk.Treeview(self, columns=("Código", "Empleado", "Estado"), show="headings", selectmode="browse")
        self.treeview.grid(row=1, column=0, padx=(0, 30), sticky="e")

        # Encabezados de las columnas del Treeview
        self.treeview.heading("Código", text="Código")
        self.treeview.heading("Empleado", text="Empleado")
        self.treeview.heading("Estado", text="Estado")

        # Ancho de las columnas
        self.treeview.column("Código", width=50)
        self.treeview.column("Empleado", width=100)
        self.treeview.column("Estado", width=50)

        # Botón para ver el saldo de la caja seleccionada
        self.ver_saldo_btn = Button(self, text="Ver saldo de caja")
        self.ver_saldo_btn.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        # Botón para retornar al menú principal
        self.return_btn = Button(self, text="Retornar menu")
        self.return_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")
 
    # Lista las cajas en el Treeview a partir de un diccionario de datos DTO
    def listar_cajas(self, lista_DTO): 
        # Limpia las filas actuales del Treeview
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Inserta las nuevas filas en el Treeview
        for i, caja_dto in lista_DTO[1].items():
            self.treeview.insert("", "end", values=(caja_dto['codigo'], caja_dto['empleado'], caja_dto['estado']))

    # Obtiene el código de la caja seleccionada en el Treeview
    def obtener_cod_caja_seleccionado(self):
        seleccion = self.treeview.selection()
        if seleccion:
            item = self.treeview.item(seleccion[0])['values']
            cod_caja = item[0]
            return cod_caja
        return None
