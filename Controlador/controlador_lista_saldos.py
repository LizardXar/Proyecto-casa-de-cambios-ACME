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
    
    # Actualiza la vista con la lista de saldos y el saldo CLP
    def update_view(self):
        codigo = self.modelo.gestor_caja.obtener_caja_seleccionada()
        
        # Recuperar saldo en monedas extranjeras
        lista_dto = self.modelo.gestor_caja.desplegar_saldo(codigo)
        print(f"Solicitando listar saldos de la caja {codigo}")
        self.frame.listar_saldo(lista_dto)

        # Recuperar saldo en CLP
        saldo_clp = self.modelo.gestor_caja.desplegar_saldo_clp(codigo)
        self.frame.saldo_clp_label.config(text=f"Saldo en CLP: ${saldo_clp:.2f}")