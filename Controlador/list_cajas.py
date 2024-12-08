class ListCajaController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["listAllCajas"]
        self._bind()

    def _bind(self):
        self.frame.return_btn.config(command=self.retorno)
        self.frame.ver_saldo_btn.config(command=self.ver_saldo)

    def retorno(self):
        self.view.switch("homeEjecutivo")
    
    def ver_saldo(self):
        cod_caja = self.frame.obtener_cod_caja_seleccionado()
        lista_saldos = self.model.gestor_caja.desplegar_saldo(cod_caja)
        if cod_caja:
            print(f"Caja seleccionada: {cod_caja}")
            lista_saldos = self.model.gestor_caja.desplegar_saldo(cod_caja)
            if lista_saldos:
                self.view.frames["listAllSaldos"].listar_saldo(lista_saldos)
                self.view.switch("listAllSaldos")
            else:
                print(f"No se encontró saldo para la caja {cod_caja}")
        else:
            print("Ninguna caja seleccionada")


    def close(self):
        self.view.stop_mainloop()
        
    def update_view(self):
        lista_DTO = self.model.gestor_caja.desplegar_cajas()
        print("pide listar cajas")
        self.frame.listar_cajas(lista_DTO)
