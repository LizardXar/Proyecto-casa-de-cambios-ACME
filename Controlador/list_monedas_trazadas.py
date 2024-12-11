class ListMonedasTrazadasController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["listMonedasTrazadas"]
        self._bind()

    def _bind(self):
        self.frame.return_btn.config(command=self.retorno)

    def retorno(self):
        self.view.switch("homeGerente")
    
    def close(self):
        self.view.stop_mainloop()

    def update_view(self):
        lista_DTO = self.model.gestor_transaccion.desplegar_moneda_mas_vendida()
        print("Listar Monedas Trazadas")
        self.frame.listar_monedas(lista_DTO)