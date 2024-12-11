class ControladorListaMonedasTrazadas:

    # Inicializa la clase con el modelo y la vista proporcionados
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.frame = self.vista.frames["listaMonedasTrazadas"]
        self._bind()

    # Configura los eventos de la interfaz de usuario
    def _bind(self):
        self.frame.return_btn.config(command=self.retorno)

    # Maneja el evento de retorno
    def retorno(self):
        self.vista.switch("inicioGerente")
    
    # Finaliza la aplicación
    def close(self):
        self.vista.stop_mainloop()

    # Actualiza la vista con la lista de monedas trazadas
    def update_view(self):
        lista_dto = self.modelo.gestor_transaccion.desplegar_moneda_mas_vendida()
        print("Listar Monedas Trazadas")
        self.frame.listar_monedas(lista_dto)
