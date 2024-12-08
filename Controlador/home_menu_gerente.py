class HomeGerenteController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["homeGerente"]
        self._bind()
    
    def _bind(self):
        self.frame.list_monedas_trazadas_btn.config(command=self.list_monedas_trazadas)
        self.frame.list_ganancias_btn.config(command=self.list_ganancias)
        self.frame.signout_btn.config(command=self.logout)

    def list_monedas_trazadas(self):
        pass

    def list_ganancias(self):
        self.model.gestor_transaccion.recuperar_ganancias()

    def logout(self):
        self.model.gestor_usuarios.logout()

    def update_view(self):
        current_user = self.model.gestor_usuarios.saludo_usuario()
        if current_user:
            nombre = current_user
        else:
            nombre = 'Set-up sistema'
        self.frame.greeting.config(text=f"Bienvenido, {nombre}!")
