class ControladorInicioEjecutivo:
    
    # Inicializa la clase con el modelo y la vista proporcionados
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.frame = self.vista.frames["inicioEjecutivo"]
        self._bind()

    # Configura los eventos de los botones de la vista
    def _bind(self):
        self.frame.list_active_btn.config(command=self.listar_monedas_activas)
        self.frame.list_all_btn.config(command=self.listar_todas_monedas)
        self.frame.list_all_cajas_btn.config(command=self.listar_todas_cajas)
        self.frame.realizar_transaccion_btn.config(command=self.realizar_transaccion)
        self.frame.signout_btn.config(command=self.cerrar_sesion)

    # Notifica al modelo para recuperar la lista de monedas activas
    def listar_monedas_activas(self):
        self.modelo.gestor_monedas.recuperar_monedas_activas()

    # Notifica al modelo para recuperar la lista de todas las monedas
    def listar_todas_monedas(self):
        self.modelo.gestor_monedas.recuperar_monedas()
    
    # Notifica al modelo para recuperar la lista de todas las cajas
    def listar_todas_cajas(self):
        self.modelo.gestor_caja.recuperar_cajas()
    
    # Notifica al modelo para realizar una transacción
    def realizar_transaccion(self):
        self.modelo.gestor_transaccion.realizar_transaccion()

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
