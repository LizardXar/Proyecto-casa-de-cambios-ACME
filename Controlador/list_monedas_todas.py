class ListAllController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["listAll"]
        self._bind()

    def _bind(self):
        self.frame.return_btn.config(command=self.retorno)

    def retorno(self):
        self.view.switch("homeEjecutivo")
           
    def close(self):
        self.view.stop_mainloop()
        
    def update_view(self):
        lista_DTO = self.model.gestor_monedas.desplegar_monedas()
        print("pide listar todas")
        self.frame.listar_monedas(lista_DTO)