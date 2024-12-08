class LoginController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["login"]
        self._bind()

    def _bind(self):
        self.frame.login_btn.config(command=self.log_in)
        self.frame.close_btn.config(command=self.close)

    def log_in(self):
        datos_DTO = self.frame.data_signin()
        self.model.gestor_usuarios.login(datos_DTO)
           
    def close(self):
        self.view.stop_mainloop()