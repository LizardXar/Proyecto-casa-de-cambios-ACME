class ControladorInicioGerente:

    # Inicializa la clase con el modelo y la vista proporcionados
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.frame = self.vista.frames["inicioGerente"]
        self._bind()
    
    # Configura los eventos de los botones de la vista
    def _bind(self):
        self.frame.list_monedas_trazadas_btn.config(command=self.listar_monedas_trazadas)
        self.frame.list_ganancias_btn.config(command=self.listar_ganancias)
        self.frame.signout_btn.config(command=self.cerrar_sesion)

    # Notifica al modelo para recuperar la lista de monedas trazadas
    def listar_monedas_trazadas(self):
        self.modelo.gestor_transaccion.recuperar_moneda_mas_vendida()

    # Notifica al modelo para recuperar la lista de ganancias
    def listar_ganancias(self):
        self.modelo.gestor_transaccion.recuperar_ganancias()

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
