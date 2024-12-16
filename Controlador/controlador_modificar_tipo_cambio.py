import re  # Importa la librería de expresiones regulares

class ControladorModificarTipoCambio:

    # Inicializa la clase con el modelo y la vista proporcionados
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.frame = self.vista.frames["modificarTipoCambio"]
        self._bind()

    # Configura los eventos de la interfaz de usuario
    def _bind(self):
        self.frame.return_btn.config(command=self.retorno)
        self.frame.confirmar_btn.config(command=self.confirmar_cambio)

    # Actualiza la vista con la información de la moneda seleccionada
    def update_view(self):
        try:
            cod_moneda = self.modelo.gestor_monedas.moneda_seleccionada
            if not cod_moneda:
                raise ValueError("No se seleccionó ninguna moneda.")

            estado, moneda_dto = self.modelo.gestor_monedas.recuperar_una_moneda(cod_moneda)
            if estado == 0 and moneda_dto:
                self.frame.mostrar_moneda(moneda_dto["codigo"], moneda_dto["nombre"], moneda_dto["tipo"])
                self.frame.tipo_cambio_entry.delete(0, "end")
                self.frame.error_label.config(text="")
            else:
                self.frame.error_label.config(fg="red", text="No se pudo recuperar la información de la moneda seleccionada.")
        except Exception as e:
            self.frame.error_label.config(fg="red", text=f"Error al actualizar la vista: {str(e)}")

    # Maneja la operación de confirmar el cambio del tipo de cambio
    def confirmar_cambio(self):
        nuevo_tipo_cambio = self.frame.tipo_cambio_entry.get()
        cod_moneda = self.modelo.gestor_monedas.moneda_seleccionada

        if not cod_moneda:
            self.frame.error_label.config(fg="red", text="No se seleccionó ninguna moneda.")
            return

        # Validación usando expresiones regulares para 1 o más dígitos, con hasta 2 decimales
        if not re.match(r"^\d+(\.\d{1,2})?$", nuevo_tipo_cambio):
            self.frame.error_label.config(fg="red", text="El tipo de cambio debe tener hasta 2 decimales.")
            return

        try:
            nuevo_tipo_cambio = float(nuevo_tipo_cambio)

            if nuevo_tipo_cambio <= 0:
                self.frame.error_label.config(fg="red", text="El tipo de cambio debe ser un número positivo mayor a 0.")
                return

            # Actualizar el tipo de cambio en la base de datos
            self.modelo.gestor_monedas.actualizar_tipo_cambio(cod_moneda, nuevo_tipo_cambio)

            # Recuperar nuevamente los datos de la moneda para actualizar la etiqueta
            estado, moneda_dto = self.modelo.gestor_monedas.recuperar_una_moneda(cod_moneda)
            if estado == 0 and moneda_dto:
                self.frame.mostrar_moneda(moneda_dto["codigo"], moneda_dto["nombre"], moneda_dto["tipo"])
            else:
                self.frame.error_label.config(fg="red", text="No se pudo actualizar la información en la vista.")

            # Mensaje de éxito
            self.frame.error_label.config(fg="green", text="Tipo de cambio actualizado correctamente.")
        except ValueError:
            self.frame.error_label.config(fg="red", text="Error: El tipo de cambio ingresado no es válido.")
        except Exception as e:
            self.frame.error_label.config(fg="red", text=f"Error al actualizar el tipo de cambio: {str(e)}")

    # Maneja el evento de retorno a la vista de lista de monedas
    def retorno(self):
        self.modelo.gestor_monedas.recuperar_monedas()
