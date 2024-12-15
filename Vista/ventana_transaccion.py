from tkinter import Frame, Label, Entry, Button, StringVar
from tkinter.ttk import Combobox

class VistaTransaccion(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configuración de las columnas de la grilla
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Header de la ventana de transacciones
        self.header = Label(self, text="Realizar Transacción")
        self.header.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Label para seleccionar la caja
        self.caja_label = Label(self, text="Seleccione la caja")
        self.caja_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        # Campo para seleccionar la caja
        self.caja_var = StringVar()
        self.caja_combo = Combobox(self, textvariable=self.caja_var, state="readonly")
        self.caja_combo.grid(row=1, column=1, padx=(0, 20), pady=5, sticky="ew")

        # Label para seleccionar la moneda
        self.currency_label = Label(self, text="Seleccione la moneda")
        self.currency_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
        # Campo para seleccionar la moneda
        self.currency_var = StringVar()
        self.currency_combo = Combobox(self, textvariable=self.currency_var, state="readonly")
        self.currency_combo.grid(row=2, column=1, padx=(0, 20), pady=5, sticky="ew")

        # Campo para mostrar el saldo disponible
        self.balance_label = Label(self, text="Saldo disponible")
        self.balance_label.grid(row=2, column=2, padx=10, pady=5, sticky="e")

        self.balance_amount = Label(self, text="$0", anchor="w")  # Etiqueta que muestra el saldo
        self.balance_amount.grid(row=2, column=3, padx=(0, 20), pady=5, sticky="w")

        # Label para ingresar la cantidad
        self.amount_label = Label(self, text="Monto a comprar")
        self.amount_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        
        # Input para ingresar la cantidad
        self.amount_input = Entry(self)
        self.amount_input.grid(row=3, column=1, padx=(0, 20), pady=5, sticky="ew")

        # Label para mostrar el total
        self.total_label = Label(self, text="Total")
        self.total_label.grid(row=3, column=2, padx=10, pady=5, sticky="e")

        # Campo para mostrar el total
        self.total_amount = Label(self, text="$0", anchor="w")  
        self.total_amount.grid(row=3, column=3, padx=(0, 20), pady=5, sticky="w")

        # Campo para mostrar mensajes de error
        self.error_label = Label(self, text="", anchor="w", fg="red")
        self.error_label.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky="w")

        # Botón para realizar la transacción
        self.transact_btn = Button(self, text="Realizar Transacción")
        self.transact_btn.grid(row=5, column=1, columnspan=2, padx=0, pady=10, sticky="ew")

        self.return_btn = Button(self, text="Retornar menu")
        self.return_btn.grid(row=6, column=0, padx=10, pady=10, sticky="w")

    def data_transaction(self):
        caja = self.caja_var.get()
        currency = self.currency_var.get()
        amount = self.amount_input.get()
        data_dto = {"caja": caja, "moneda": currency, "cantidad": amount}
        
        self.amount_input.delete(0, last=len(amount))
        return data_dto
