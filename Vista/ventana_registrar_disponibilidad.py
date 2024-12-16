from tkinter import Frame, Label, Button, Entry

class VistaRegistrarDisponibilidadPesos(Frame):

    # Inicializa la vista para registrar la disponibilidad de pesos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configuración de la grilla
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # Encabezado de la vista
        self.header = Label(self, text="Registrar disponibilidad", font=("Arial", 12, "bold"))
        self.header.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        # Información de la caja asignada
        self.caja_label = Label(self, text="Caja:")
        self.caja_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.caja_value = Label(self, text="No asignada", anchor="w", font=("Arial", 10))
        self.caja_value.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Información del saldo actual
        self.saldo_label = Label(self, text="Saldo actual:")
        self.saldo_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.saldo_value = Label(self, text="0.00", anchor="w", font=("Arial", 10))
        self.saldo_value.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Campo para ingresar la nueva disponibilidad
        self.cantidad_label = Label(self, text="Nueva disponibilidad:")
        self.cantidad_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.cantidad_entry = Entry(self, font=("Arial", 10), width=10)
        self.cantidad_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Mensaje de error para mostrar validaciones fallidas
        self.error_label = Label(self, text="", fg="red", font=("Arial", 9), anchor="w")
        self.error_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Botón para registrar la nueva disponibilidad
        self.registrar_btn = Button(self, text="Registrar disponibilidad", font=("Arial", 10))
        self.registrar_btn.grid(row=5, column=0, columnspan=2, pady=(10, 5))

        # Botón para retornar a la vista anterior
        self.return_btn = Button(self, text="volver", font=("Arial", 10))
        self.return_btn.grid(row=6, column=0, columnspan=2, pady=10)

    # Obtiene la cantidad ingresada en el campo de disponibilidad
    def obtener_datos_disponibilidad(self):
        cantidad = self.cantidad_entry.get()
        return {"cantidad": cantidad}

    # Muestra la caja asignada al usuario en la interfaz
    def mostrar_caja_asignada(self, caja):
        self.caja_value.config(text=str(caja))

    # Muestra el saldo actual en la interfaz
    def mostrar_saldo_actual(self, saldo):
        self.saldo_value.config(text=f"{saldo:.2f}")
