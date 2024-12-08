class HomeEjecutivoController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["homeEjecutivo"]
        self._bind()

    def _bind(self):
        self.frame.list_active_btn.config(command=self.lists_active)
        self.frame.list_all_btn.config(command=self.lists_all)
        self.frame.list_all_cajas_btn.config(command=self.lists_cajas)
        self.frame.signout_btn.config(command=self.logout)

    def lists_active(self):
        self.model.gestor_monedas.recuperar_monedas_activas()

    def lists_all(self):
        self.model.gestor_monedas.recuperar_monedas()
    
    def lists_cajas(self):
        self.model.gestor_caja.recuperar_cajas()

    def logout(self):
        self.model.gestor_usuarios.logout()
    
    def update_view(self):
        current_user = self.model.gestor_usuarios.saludo_usuario()
        if current_user:
            nombre = current_user
        else:
            nombre = 'Set-up sistema'
        self.frame.greeting.config(text=f"Bienvenido, {nombre}!")

