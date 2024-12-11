class ControladorLogin:
    
    # Inicializa la clase con el modelo y la vista proporcionados
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.frame = self.vista.frames["login"]
        self._bind()

    # Configura los eventos de la interfaz de usuario
    def _bind(self):
        self.frame.login_btn.config(command=self.iniciar_sesion)
        self.frame.close_btn.config(command=self.cerrar)

    # Maneja el evento de inicio de sesión
    def iniciar_sesion(self):
        datos_dto = self.frame.data_signin()
        self.modelo.gestor_usuarios.login(datos_dto)
           
    # Finaliza la aplicación
    def cerrar(self):
        self.vista.stop_mainloop()
