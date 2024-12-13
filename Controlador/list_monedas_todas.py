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

    # Maneja el evento de retorno
    def retorno(self):
        self.vista.switch("inicioEjecutivo")
    
    # Finaliza la aplicación
    def close(self):
        self.vista.stop_mainloop()
    
    # Actualiza la vista con la lista de todos los elementos
    def update_view(self):
        lista_dto = self.modelo.gestor_monedas.desplegar_monedas()
        print("pide listar todos")
        self.frame.listar_monedas(lista_dto)
