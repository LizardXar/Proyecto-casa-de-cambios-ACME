class ControladorInicioGerente:

    # Inicializa la clase con el modelo y la vista proporcionados
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.frame = self.vista.frames["inicioGerente"]
        self._bind()
    
    # Configura los eventos de la interfaz de usuario
    def _bind(self):
        self.frame.list_monedas_trazadas_btn.config(command=self.listar_monedas_trazadas)
        self.frame.list_ganancias_btn.config(command=self.listar_ganancias)
        self.frame.signout_btn.config(command=self.cerrar_sesion)

    # Maneja el evento de listar las monedas trazadas
    def listar_monedas_trazadas(self):
        self.modelo.gestor_transaccion.recuperar_moneda_mas_vendida()

    # Maneja el evento de listar las ganancias
    def listar_ganancias(self):
        self.modelo.gestor_transaccion.recuperar_ganancias()

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
