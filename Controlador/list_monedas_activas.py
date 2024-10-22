class ListActiveController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["listActive"]
        self._bind()

    def _bind(self):
        self.frame.return_btn.config(command=self.retorno)

    def retorno(self):
        self.view.switch("home")
           
    def close(self):
        self.view.stop_mainloop()
        
    def update_view(self):
        lista_DTO = self.model.gestor_monedas.desplegar_monedas_activas()
        print("pide listar activas")
        self.frame.listar_monedas_autorizadas(lista_DTO)