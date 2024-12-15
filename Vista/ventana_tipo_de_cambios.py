from tkinter import Frame, Label, Entry, Button


class VistaTipoDeCambio(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configuración de la grilla
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        # Header de la ventana
        self.header = Label(self, text="Modificar Tipo de Cambio")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Campo para mostrar el código y nombre de la moneda
        self.moneda_label = Label(self, text="Moneda seleccionada:")
        self.moneda_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.moneda_entry = Entry(self, state="disabled")
        self.moneda_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Campo para ingresar el nuevo tipo de cambio
        self.tipo_cambio_label = Label(self, text="Nuevo tipo de cambio:")
        self.tipo_cambio_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.tipo_cambio_entry = Entry(self)
        self.tipo_cambio_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        # Campo para mostrar mensajes de error
        self.error_label = Label(self, text="", anchor="w", fg="red")
        self.error_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky="w")

        # Botón para confirmar el cambio
        self.confirmar_btn = Button(self, text="Confirmar cambio")
        self.confirmar_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Botón para retornar al menú anterior
        self.return_btn = Button(self, text="Retornar")
        self.return_btn.grid(row=5, column=0, padx=10, pady=10, sticky="w")

    def mostrar_moneda(self, cod_moneda, nombre, tipo):
        self.moneda_entry.config(state="normal")
        self.moneda_entry.delete(0, "end")
        self.moneda_entry.insert(0, f"{cod_moneda} - {nombre} - {tipo}")
        self.moneda_entry.config(state="disabled")

    def obtener_tipo_cambio(self):
        return self.tipo_cambio_entry.get()
