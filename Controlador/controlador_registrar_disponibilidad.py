import re  # Importa la librería de expresiones regulares

class ControladorRegistrarDisponibilidadPesos:

    # Constructor de la clase, inicializa los atributos del controlador
    def __init__(self, modelo, vista):
        # Asocia el modelo y la vista proporcionados
        self.modelo = modelo
        self.vista = vista
        # Obtiene el frame correspondiente a la vista de "registrarDisponibilidadPesos"
        self.frame = self.vista.frames["registrarDisponibilidadPesos"]
        # Llama al método para configurar los eventos de los botones
        self._bind()

    # Configura los eventos de los botones presentes en la vista
    def _bind(self):
        # Asocia la acción de retorno al botón de retorno
        self.frame.return_btn.config(command=self.retorno)
        # Asocia la acción de registrar disponibilidad al botón de registro
        self.frame.registrar_btn.config(command=self.registrar_disponibilidad)

    # Maneja la operación de registrar la disponibilidad de pesos
    def registrar_disponibilidad(self):
        try:
            # Obtiene la cantidad ingresada por el usuario desde la entrada de la vista
            data = self.frame.obtener_datos_disponibilidad()
            cantidad = data["cantidad"]

            # Valida que la cantidad sea un número con hasta 2 decimales
            if not cantidad or not re.match(r"^\d+(\.\d{0,2})?$", cantidad):
                # Muestra un mensaje de error si la validación falla
                self.frame.error_label.config(fg="red", text="Ingrese una cantidad válida (máximo 2 decimales).")
                return

            # Convierte la cantidad a tipo float para realizar cálculos
            cantidad = float(cantidad)

            # Verifica que la cantidad sea mayor a 0
            if cantidad <= 0:
                # Muestra un mensaje de error si la cantidad es menor o igual a 0
                self.frame.error_label.config(fg="red", text="La disponibilidad debe ser mayor a 0.")
                return

            # Obtiene el código de empleado actual desde el modelo de usuarios
            cod_empleado = self.modelo.gestor_usuarios.current_user_id
            # Obtiene la caja asignada al empleado actual
            cod_caja = self.modelo.gestor_caja.obtener_caja_asociada(cod_empleado)

            # Verifica si existe una caja asignada al empleado
            if not cod_caja:
                # Muestra un mensaje de error si no se encuentra una caja asignada
                self.frame.error_label.config(fg="red", text="No se encontró la caja asignada.")
                return

            # Actualiza la disponibilidad de CLP en la base de datos
            estado = self.modelo.gestor_caja.actualizar_saldo_clp(cod_caja, cantidad)

            # Verifica si la actualización fue exitosa
            if estado == 0:  # Éxito
                # Muestra un mensaje de éxito
                self.frame.error_label.config(fg="green", text="Disponibilidad registrada con éxito.")
                
                # Obtiene el nuevo saldo de la caja desde el modelo
                nuevo_saldo = self.modelo.gestor_caja.desplegar_saldo_clp(cod_caja)
                # Muestra el nuevo saldo en la vista
                self.frame.mostrar_saldo_actual(nuevo_saldo)

                # Limpia el campo de entrada de la cantidad
                self.frame.cantidad_entry.delete(0, "end")
            else:
                # Muestra un mensaje de error si no se pudo actualizar la disponibilidad
                self.frame.error_label.config(fg="red", text="Error al actualizar la disponibilidad.")
        except Exception as e:
            # Muestra un mensaje de error en caso de que ocurra una excepción
            self.frame.error_label.config(fg="red", text=f"Error: {str(e)}")

    # Cambia la vista actual a la vista de inicio de cajero
    def retorno(self):
        self.vista.switch("inicioCajero")

    # Actualiza la vista de "Registrar Disponibilidad de Pesos"
    def update_view(self):
        # Obtiene el código del empleado actual
        cod_empleado = self.modelo.gestor_usuarios.current_user_id
        # Obtiene la caja asignada al empleado actual
        cod_caja = self.modelo.gestor_caja.obtener_caja_asociada(cod_empleado)
        # Obtiene el saldo actual de la caja desde el modelo
        saldo_actual = self.modelo.gestor_caja.desplegar_saldo_clp(cod_caja)

        # Limpia el campo de entrada de cantidad en la vista
        self.frame.cantidad_entry.delete(0, "end")  
        # Limpia cualquier mensaje de error que se haya mostrado anteriormente
        self.frame.error_label.config(text="") 

        # Muestra el código de la caja asignada en la vista
        self.frame.mostrar_caja_asignada(cod_caja)
        # Muestra el saldo actual de la caja en la vista
        self.frame.mostrar_saldo_actual(saldo_actual)
