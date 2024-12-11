class ControladorListaCajas:
    
    # Inicializa la clase con el modelo y la vista proporcionados
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.frame = self.vista.frames["listaTodasCajas"]
        self._bind()

    # Configura los eventos de la interfaz de usuario
    def _bind(self):
        self.frame.return_btn.config(command=self.retorno)
        self.frame.ver_saldo_btn.config(command=self.ver_saldo)

    # Maneja el evento de retorno
    def retorno(self):
        self.vista.switch("inicioEjecutivo")
    
    # Maneja el evento de ver saldo de la caja seleccionada
    def ver_saldo(self):
        cod_caja = self.frame.obtener_cod_caja_seleccionado()
        lista_saldos = self.modelo.gestor_caja.desplegar_saldo(cod_caja)
        if cod_caja:
            print(f"Caja seleccionada: {cod_caja}")
            lista_saldos = self.modelo.gestor_caja.desplegar_saldo(cod_caja)
            if lista_saldos:
                self.vista.frames["listaTodosSaldos"].listar_saldo(lista_saldos)
                self.vista.switch("listaTodosSaldos")
            else:
                print(f"No se encontró saldo para la caja {cod_caja}")
        else:
            print("Ninguna caja seleccionada")

    # Finaliza la aplicación
    def close(self):
        self.vista.stop_mainloop()
        
    # Actualiza la vista con la lista de cajas
    def update_view(self):
        lista_dto = self.modelo.gestor_caja.desplegar_cajas()
        print("pide listar cajas")
        self.frame.listar_cajas(lista_dto)
