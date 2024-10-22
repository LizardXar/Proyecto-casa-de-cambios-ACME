class HomeController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self):
        self.frame.list_active_btn.config(command=self.lists_active)
        self.frame.list_all_btn.config(command=self.lists_all)

    def lists_active(self):
        self.model.gestor_monedas.recuperar_monedas_activas()

    def lists_all(self):
        self.model.gestor_monedas.recuperar_monedas()