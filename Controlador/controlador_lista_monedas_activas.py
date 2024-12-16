class ControladorListaActivos:
    
    # Inicializa la clase con el modelo y la vista proporcionados
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.frame = self.vista.frames["listaActivos"]
        self._bind()

    # Configura los eventos de los botones de la vista
    def _bind(self):
        self.frame.return_btn.config(command=self.retorno)

    # Cambia la vista al inicio del ejecutivo
    def retorno(self):
        self.vista.switch("inicioEjecutivo")
    
    # Finaliza la aplicación
    def close(self):
        self.vista.stop_mainloop()
    
    # Actualiza la vista con la lista de activos
    def update_view(self):
        lista_dto = self.modelo.gestor_monedas.desplegar_monedas_activas()
        print("Solicitando listar activos")
        self.frame.listar_monedas_autorizadas(lista_dto)
