class ControladorInicioEjecutivo:
    
    # Inicializa la clase con el modelo y la vista proporcionados
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.frame = self.vista.frames["inicioEjecutivo"]
        self._bind()

    # Configura los eventos de la interfaz de usuario
    def _bind(self):
        self.frame.list_active_btn.config(command=self.listar_monedas_activas)
        self.frame.list_all_btn.config(command=self.listar_todas_monedas)
        self.frame.list_all_cajas_btn.config(command=self.listar_todas_cajas)
        self.frame.signout_btn.config(command=self.cerrar_sesion)

    # Maneja el evento de listar monedas activas
    def listar_monedas_activas(self):
        self.modelo.gestor_monedas.recuperar_monedas_activas()

    # Maneja el evento de listar todas las monedas
    def listar_todas_monedas(self):
        self.modelo.gestor_monedas.recuperar_monedas()
    
    # Maneja el evento de listar todas las cajas
    def listar_todas_cajas(self):
        self.modelo.gestor_caja.recuperar_cajas()

    # Maneja el evento de cerrar sesión
    def cerrar_sesion(self):
        self.modelo.gestor_usuarios.cerrar_sesion()

    # Actualiza la vista con el saludo al usuario actual
    def update_view(self):
        current_user = self.modelo.gestor_usuarios.saludo_usuario()
        if current_user:
            nombre = current_user
        else:
            nombre = 'Set-up sistema'
        self.frame.greeting.config(text=f"¡Bienvenido, {nombre}!")
