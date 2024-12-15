class ControladorInicioCajero:

    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.frame = self.vista.frames["inicioCajero"]
        self._bind()
    
    def _bind(self):
        self.frame.registrar_disponibilidad_btn.config(command=self.registrar_disponibilidad)
        self.frame.signout_btn.config(command=self.cerrar_sesion)
        
    def registrar_disponibilidad(self):
        pass

        # Maneja el evento de cerrar sesión
    def cerrar_sesion(self):
        self.modelo.gestor_usuarios.cerrar_sesion()

    def update_view(self):
        current_user = self.modelo.gestor_usuarios.saludo_usuario()
        if current_user:
            nombre = current_user
        else:
            nombre = 'Set-up sistema'
        self.frame.greeting.config(text=f"¡Bienvenido, {nombre}!")