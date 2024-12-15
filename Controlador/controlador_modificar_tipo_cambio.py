class ControladorModificarTipoCambio:

    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.frame = self.vista.frames["modificarTipoCambio"]
        self._bind()

    def _bind(self):
        self.frame.return_btn.config(command=self.retorno)
        self.frame.confirmar_btn.config(command=self.confirmar_cambio)

    def update_view(self):
        try:
            cod_moneda = self.modelo.gestor_monedas.moneda_seleccionada
            if not cod_moneda:
                raise ValueError("No se seleccionó ninguna moneda.")

            estado, moneda = self.modelo.gestor_monedas.recuperar_una_moneda(cod_moneda)
            if estado == 0 and moneda:
                self.frame.mostrar_moneda(moneda["codigo"], moneda["nombre"], moneda["tipo"])
                self.frame.tipo_cambio_entry.delete(0, "end")
                self.frame.error_label.config(text="")
            else:
                self.frame.error_label.config(fg="red", text="No se pudo recuperar la información de la moneda seleccionada.")
        except Exception as e:
            self.frame.error_label.config(fg="red", text=f"Error al actualizar la vista: {str(e)}")

    def confirmar_cambio(self):
        nuevo_tipo_cambio = self.frame.tipo_cambio_entry.get()
        cod_moneda = self.modelo.gestor_monedas.moneda_seleccionada

        if not cod_moneda:
            self.frame.error_label.config(fg="red", text="No se seleccionó ninguna moneda.")
            return

        if not nuevo_tipo_cambio or not nuevo_tipo_cambio.isdigit():
            self.frame.error_label.config(fg="red", text="Por favor, ingrese un tipo de cambio válido.")
            return

        try:
            # Actualizar el tipo de cambio en la base de datos
            self.modelo.gestor_monedas.actualizar_tipo_cambio(cod_moneda, float(nuevo_tipo_cambio))

            # Recuperar nuevamente los datos de la moneda para actualizar la etiqueta
            estado, moneda_actualizada = self.modelo.gestor_monedas.recuperar_una_moneda(cod_moneda)
            if estado == 0 and moneda_actualizada:
                # Crear el texto de la moneda seleccionada sin guiones adicionales
                self.frame.mostrar_moneda(moneda_actualizada["codigo"], moneda_actualizada["nombre"], moneda_actualizada["tipo"])
            else:
                self.frame.error_label.config(fg="red", text="No se pudo actualizar la información en la vista.")

            # Mensaje de éxito
            self.frame.error_label.config(fg="green", text="Tipo de cambio actualizado correctamente.")
        except Exception as e:
            self.frame.error_label.config(fg="red", text=f"Error al actualizar el tipo de cambio: {str(e)}")


    def retorno(self):
        self.modelo.gestor_monedas.recuperar_monedas()
