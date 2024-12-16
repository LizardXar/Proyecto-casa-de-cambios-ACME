class ControladorListaCajas:
    
    # Inicializa la clase con el modelo y la vista proporcionados
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.frame = self.vista.frames["listaTodasCajas"]
        self._bind()

    # Configura los eventos de los botones de la vista
    def _bind(self):
        self.frame.return_btn.config(command=self.retorno)
        self.frame.ver_saldo_btn.config(command=self.ver_saldo)

    # Cambia la vista al inicio del ejecutivo
    def retorno(self):
        self.vista.switch("inicioEjecutivo")
    
    # Recupera y muestra el saldo de la caja seleccionada
    def ver_saldo(self):
        cod_caja = self.frame.obtener_cod_caja_seleccionado()
        if cod_caja:
            print(f"Caja seleccionada: {cod_caja}")
            self.modelo.gestor_caja.caja_seleccionada = cod_caja
            result = self.modelo.gestor_caja.obtener_caja_seleccionada()
            print(f"Caja seleccionada en modelo: {result}")
            self.modelo.gestor_caja.notificar_ver_saldo()
        else:
            print("Ninguna caja seleccionada")

    # Finaliza la aplicación
    def close(self):
        self.vista.stop_mainloop()
        
    # Actualiza la vista con la lista de todas las cajas
    def update_view(self):
        lista_dto = self.modelo.gestor_caja.desplegar_cajas()
        print("Solicitando listar cajas")
        self.frame.listar_cajas(lista_dto)
