from .controlador_inicio_ejecutivo import ControladorInicioEjecutivo
from .controlador_inicio_gerente import ControladorInicioGerente
from .controlador_lista_monedas_activas import ControladorListaActivos
from .controlador_lista_monedas_todas import ControladorListaTodos
from .controlador_lista_cajas import ControladorListaCajas
from .controlador_lista_saldos import ControladorListaSaldos
from .controlador_login_usuario import ControladorLogin
from .controlador_lista_ganancias import ControladorListaGanancias
from .controlador_lista_monedas_trazadas import ControladorListaMonedasTrazadas
from .controlador_inicio_cajero import ControladorInicioCajero
from .controlador_realizar_transaccion import ControladorRealizarTransaccion
from .controlador_modificar_tipo_cambio import ControladorModificarTipoCambio
from .controlador_registrar_disponibilidad import ControladorRegistrarDisponibilidadPesos

class Controlador:

    # Inicializa la clase con el modelo y la vista proporcionados, y configura los controladores específicos
    def __init__(self, modelo, vista):
        self.vista = vista
        self.modelo = modelo
        self.home_menu_ejecutivo = ControladorInicioEjecutivo(modelo, vista)
        self.home_menu_gerente = ControladorInicioGerente(modelo, vista)
        self.home_menu_cajero = ControladorInicioCajero(modelo, vista)
        self.list_active_controller = ControladorListaActivos(modelo, vista)
        self.list_all_controller = ControladorListaTodos(modelo, vista)
        self.list_cajas = ControladorListaCajas(modelo, vista)
        self.list_saldos = ControladorListaSaldos(modelo, vista)
        self.login_usuario = ControladorLogin(modelo, vista)
        self.list_ganancias = ControladorListaGanancias(modelo, vista)
        self.list_monedas_trazadas = ControladorListaMonedasTrazadas(modelo, vista)
        self.realizar_transaccion = ControladorRealizarTransaccion(modelo, vista)
        self.modificar_tipo_de_cambio = ControladorModificarTipoCambio(modelo, vista)
        self.registrar_disponibilidad_pesos = ControladorRegistrarDisponibilidadPesos(modelo, vista)

        # Configura los eventos para los diferentes controladores
        self.modelo.gestor_usuarios.add_event_listener(
            "ingreso_ejecutivo", self.ingreso_ejecutivo_listener)

        self.modelo.gestor_usuarios.add_event_listener(
            "ingreso_gerente", self.ingreso_gerente_listener)
        
        self.modelo.gestor_usuarios.add_event_listener(
            "ingreso_cajero", self.ingreso_cajero_listener)

        self.modelo.gestor_monedas.add_event_listener(
            "lista_monedas_activas", self.lista_monedas_activas_listener)
        
        self.modelo.gestor_monedas.add_event_listener(
            "lista_monedas", self.lista_todas_monedas_listener)
        
        self.modelo.gestor_caja.add_event_listener(
            "lista_caja", self.lista_cajas_listener)
        
        self.modelo.gestor_caja.add_event_listener(
            "lista_saldos", self.lista_saldos_listener)
        
        self.modelo.gestor_usuarios.add_event_listener(
            "salida_sistema", self.autenticacion_signout_listener)
        
        self.modelo.gestor_transaccion.add_event_listener(
            "lista_ganancias", self.lista_ganancias_listener)
        
        self.modelo.gestor_transaccion.add_event_listener(
            "lista_monedas_trazadas", self.lista_monedas_trazadas_listener)
        
        self.modelo.gestor_transaccion.add_event_listener(
            "realizar_transaccion", self.realizar_transaccion_listener)
        
        self.modelo.gestor_monedas.add_event_listener(
            "modificar_tipo_cambio", self.modificar_tipo_cambio_listener)
        
        self.modelo.gestor_caja.add_event_listener(
        "registrarDisponibilidadPesos", self.registrar_disponibilidad_listener)
    
    # Listener para el evento de ingreso como ejecutivo
    def ingreso_ejecutivo_listener(self, data):
        self.home_menu_ejecutivo.update_view()
        self.vista.switch("inicioEjecutivo")
    
    # Listener para el evento de ingreso como gerente
    def ingreso_gerente_listener(self, data):
        self.home_menu_gerente.update_view()
        self.vista.switch("inicioGerente")

    # Listener para el evento de ingreso como cajero
    def ingreso_cajero_listener(self, data):
        self.home_menu_cajero.update_view()
        self.vista.switch("inicioCajero")

    # Listener para la lista de monedas activas
    def lista_monedas_activas_listener(self, data):
        self.list_active_controller.update_view()
        self.vista.switch("listaActivos")
    
    # Listener para la lista de todas las monedas
    def lista_todas_monedas_listener(self, data):
        self.list_all_controller.update_view()
        self.vista.switch("listaTodos")

    # Listener para la lista de cajas
    def lista_cajas_listener(self, data):
        self.list_cajas.update_view()
        self.vista.switch("listaTodasCajas")
    
    # Listener para la lista de saldos
    def lista_saldos_listener(self, data):
        self.list_saldos.update_view()
        self.vista.switch("listaTodosSaldos")

    # Listener para el evento de cierre de sesión
    def autenticacion_signout_listener(self, data):
        self.vista.switch("login")

    # Listener para la lista de ganancias
    def lista_ganancias_listener(self, data):
        self.list_ganancias.update_view()
        self.vista.switch("listaGanancias")

    # Listener para la lista de monedas trazadas
    def lista_monedas_trazadas_listener(self, data):
        self.list_monedas_trazadas.update_view()
        self.vista.switch("listaMonedasTrazadas")
    
    def realizar_transaccion_listener(self, data):
        self.realizar_transaccion.update_view()
        self.vista.switch("realizarTransaccion")
    
    def modificar_tipo_cambio_listener(self, data):
        self.modificar_tipo_de_cambio.update_view()
        self.vista.switch("modificarTipoCambio")
    
    def registrar_disponibilidad_listener(self, data):
        self.registrar_disponibilidad_pesos.update_view()
        self.vista.switch("registrarDisponibilidadPesos")


    # Inicia la aplicación mostrando la vista de inicio de sesión
    def start(self):
        self.vista.switch("login")
        self.vista.start_mainloop()
