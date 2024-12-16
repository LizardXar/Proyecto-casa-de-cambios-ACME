import re  # Importa la librería de expresiones regulares

class ControladorRealizarTransaccion:
    
    # Inicializa la clase con el modelo y la vista proporcionados
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.repositorio = modelo.repositorio_transacciones
        self.frame = self.vista.frames["realizarTransaccion"]
        self._bind()

    # Configura los eventos de la interfaz de usuario
    def _bind(self):
        self.frame.transact_btn.config(command=self.realizar_transaccion)
        self.frame.caja_combo.bind("<<ComboboxSelected>>", self.actualizar_saldo)
        self.frame.amount_input.bind("<KeyRelease>", self.actualizar_total)
        self.frame.return_btn.config(command=self.retorno)

    # Maneja la operación de realizar una transacción
    def realizar_transaccion(self):
        try:
            # Obtener datos del formulario
            data_dto = self.frame.data_transaction()
            caja_seleccionada = data_dto["caja"]
            moneda_seleccionada = data_dto["moneda"]
            cantidad = data_dto["cantidad"]

            # Validaciones
            if not caja_seleccionada or caja_seleccionada == "---Seleccione caja---":
                self.frame.error_label.config(fg="red", text="Seleccione una caja.")
                return

            if not moneda_seleccionada or moneda_seleccionada == "---Seleccione moneda---":
                self.frame.error_label.config(fg="red", text="Seleccione una moneda.")
                return

            if not cantidad or not re.match(r"^\d+(\.\d{0,2})?$", cantidad):
                self.frame.error_label.config(fg="red", text="Ingrese un monto válido (máximo 2 decimales).")
                return

            cantidad = float(cantidad)  # Convertir cantidad validada a float

            if cantidad <= 0:
                self.frame.error_label.config(fg="red", text="El monto debe ser un número positivo mayor a 0.")
                return

            # Convertir datos validados
            cod_caja = int(caja_seleccionada.split(" - ")[0])
            cod_moneda = int(moneda_seleccionada.split(" - ")[0])
            monto_clp = cantidad

            # Obtener saldo disponible y tipo de cambio
            saldo_disponible = self.repositorio.obtener_saldo_clp(cod_caja)
            tipo_cambio = self.repositorio.obtener_tipo_cambio(cod_moneda)
            total = monto_clp * tipo_cambio

            # Verificar si hay saldo suficiente
            if total > saldo_disponible:
                self.frame.error_label.config(fg="red", text="Saldo insuficiente para realizar la transacción.")
                return

            # Realizar la transacción a través del repositorio
            self.repositorio.realizar_transaccion(cod_caja, cod_moneda, monto_clp)
            self.frame.error_label.config(fg="green", text="Transacción realizada exitosamente.")

            # Actualizar el saldo disponible en la vista
            self.actualizar_saldo()

        except ValueError as e:
            self.frame.error_label.config(fg="red", text=f"Error de validación: {str(e)}")
        except Exception as e:
            self.frame.error_label.config(fg="red", text=f"Error: {str(e)}")

    # Actualiza el saldo disponible al seleccionar una caja
    def actualizar_saldo(self, event=None):
        try:
            caja_seleccionada = self.frame.caja_var.get()
            if caja_seleccionada and caja_seleccionada != "---Seleccione caja---":
                cod_caja = int(caja_seleccionada.split(" - ")[0])
                saldo_clp = self.repositorio.obtener_saldo_clp(cod_caja)
                self.frame.balance_amount.config(text=f"${saldo_clp:.2f}" if saldo_clp else "$0.00")
            else:
                self.frame.balance_amount.config(text="$0.00")
        except Exception as e:
            self.frame.error_label.config(fg="red", text=f"Error al actualizar el saldo: {str(e)}")

    # Actualiza el total basado en el monto ingresado y el tipo de cambio
    def actualizar_total(self, event=None):
        try:
            moneda_seleccionada = self.frame.currency_var.get()
            monto = self.frame.amount_input.get()
            if moneda_seleccionada and moneda_seleccionada != "---Seleccione moneda---" and re.match(r"^\d+(\.\d{0,2})?$", monto):
                cod_moneda = int(moneda_seleccionada.split(" - ")[0])
                tipo_cambio = self.repositorio.obtener_tipo_cambio(cod_moneda)
                total = float(monto) * tipo_cambio
                self.frame.total_amount.config(text=f"${total:.2f}")
            else:
                self.frame.total_amount.config(text="$0")
        except Exception as e:
            self.frame.error_label.config(fg="red", text=f"Error al calcular el total: {str(e)}")

    # Cambia la vista a la vista de inicio del ejecutivo
    def retorno(self):
        self.vista.switch("inicioEjecutivo")

    # Actualiza la vista con las opciones de cajas y monedas
    def update_view(self):
        try:
            # Recuperar y poblar cajas
            cajas_dto = self.repositorio.recuperar_cajas()
            opciones_cajas = ["---Seleccione caja---"] + [f"{caja['codigo']}" for caja in cajas_dto.values()]
            self.frame.caja_combo["values"] = opciones_cajas
            self.frame.caja_var.set("---Seleccione caja---")  # Selección inicial

            # Recuperar y poblar monedas
            monedas_dto = self.repositorio.recuperar_monedas()
            opciones_monedas = ["---Seleccione moneda---"] + [f"{moneda['codigo']} - {moneda['nombre']}" for moneda in monedas_dto.values()]
            self.frame.currency_combo["values"] = opciones_monedas
            self.frame.currency_var.set("---Seleccione moneda---")  # Selección inicial

            # Limpiar el campo de monto
            self.frame.amount_input.delete(0, "end")

            # Limpiar etiquetas de saldo y total
            self.frame.balance_amount.config(text="$0.00")
            self.frame.total_amount.config(text="$0.00")

            # Limpiar mensajes de error
            self.frame.error_label.config(text="")
        except Exception as e:
            self.frame.error_label.config(fg="red", text=f"Error al actualizar la vista: {str(e)}")
