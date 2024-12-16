class ControladorInicioCajero:
    
    # Inicializa la clase con el modelo y la vista proporcionados
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.frame = self.vista.frames["inicioCajero"]
        self._bind()
    
    # Configura los eventos de los botones de la vista
    def _bind(self):
        self.frame.registrar_disponibilidad_btn.config(command=self.registrar_disponibilidad)
        self.frame.signout_btn.config(command=self.cerrar_sesion)
    
    # Notifica al modelo para iniciar la acción de registrar disponibilidad de caja
    def registrar_disponibilidad(self):
        self.modelo.gestor_caja.notificar_registrar_disponibilidad_caja()
    
    # Maneja el evento de cerrar sesión y notifica al modelo para cerrar la sesión del usuario actual
    def cerrar_sesion(self):
        self.modelo.gestor_usuarios.cerrar_sesion()
    
    # Actualiza la vista con el saludo del usuario actual
    def update_view(self):
        current_user = self.modelo.gestor_usuarios.saludo_usuario()
        if current_user:
            nombre = current_user
        else:
            nombre = 'Set-up sistema'
        self.frame.greeting.config(text=f"¡Bienvenido, {nombre}!")
