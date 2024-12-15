class ControladorListaSaldos:
    
    # Inicializa la clase con el modelo y la vista proporcionados
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.frame = self.vista.frames["listaTodosSaldos"]
        self._bind()
    
    # Configura los eventos de la interfaz de usuario
    def _bind(self):
        self.frame.return_btn.config(command=self.retorno)
    
    # Maneja el evento de retorno
    def retorno(self):
        self.vista.switch("listaTodasCajas")
    
    # Finaliza la aplicación
    def close(self):
        self.vista.stop_mainloop()
    
    # Actualiza la vista con la lista de saldos
    def update_view(self, codigo):
        lista_dto = self.modelo.gestor_caja.desplegar_saldo(codigo)
        print(f"pide listar saldos de la caja {codigo}")
        self.frame.listar_saldo(lista_dto)
