class ListSaldoController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["listAllSaldos"]
        self._bind()
    
    def _bind(self):
        self.frame.return_btn.config(command=self.retorno)
    
    def retorno(self):
        self.view.switch("listAllCajas")
    
    def close(self):
        self.view.stop_mainloop()
    
    def update_view(self, codigo):
        lista_DTO = self.model.gestor_caja.desplegar_saldo(codigo)
        print(f"pide listar saldos de la caja {codigo}")
        self.frame.listar_saldo(lista_DTO)