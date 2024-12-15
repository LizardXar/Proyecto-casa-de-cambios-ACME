class ControladorListaTodos:
    
    # Inicializa la clase con el modelo y la vista proporcionados
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.frame = self.vista.frames["listaTodos"]
        self._bind()

    # Configura los eventos de la interfaz de usuario
    def _bind(self):
        self.frame.return_btn.config(command=self.retorno)
        self.frame.tipo_cambio_btn.config(command=self.modificar_tipo_cambio)

    # Maneja el evento de retorno
    def retorno(self):
        self.vista.switch("inicioEjecutivo")
    
    def modificar_tipo_cambio(self):
        cod_moneda = self.frame.obtener_cod_moneda_seleccionado()
        if cod_moneda:
            self.modelo.gestor_monedas.moneda_seleccionada = cod_moneda
            self.modelo.gestor_monedas.notificar_modificar_tipo_cambio()
        else:
            print("Ninguna moneda seleccionada")

    # Finaliza la aplicación
    def close(self):
        self.vista.stop_mainloop()
    
    # Actualiza la vista con la lista de todos los elementos
    def update_view(self):
        lista_dto = self.modelo.gestor_monedas.desplegar_monedas()
        print("pide listar todos")
        self.frame.listar_monedas(lista_dto)
