from .home_menu_ejecutivo import HomeEjecutivoController
from .home_menu_gerente import HomeGerenteController
from .list_monedas_activas import ListActiveController
from .list_monedas_todas import ListAllController
from .list_cajas import ListCajaController
from .list_saldos import ListSaldoController
from .login_usuario import LoginController
from .list_ganancias import ListGananciasController

class Controller:

    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.home_menu_ejecutivo = HomeEjecutivoController(model, view)
        self.home_menu_gerente = HomeGerenteController(model, view)
        self.list_active_controller = ListActiveController(model, view)
        self.list_all_controller = ListAllController(model, view)
        self.list_cajas = ListCajaController(model, view)
        self.list_saldos = ListSaldoController(model, view)
        self.login_usuario = LoginController(model, view)
        self.list_ganancias = ListGananciasController(model, view)

        self.model.gestor_usuarios.add_event_listener(
            "ingreso_ejecutivo", self.ingreso_ejecutivo_listener)

        self.model.gestor_usuarios.add_event_listener(
            "ingreso_gerente", self.ingreso_gerente_listener)

        self.model.gestor_monedas.add_event_listener(
            "lista_monedas_activas", self.monedas_activas_list_listener)
        
        self.model.gestor_monedas.add_event_listener(
            "lista_monedas", self.monedas_todas_list_listener)
        
        self.model.gestor_caja.add_event_listener(
            "lista_caja", self.cajas_list_listener)
        
        self.model.gestor_caja.add_event_listener(
            "lista_saldos", self.saldos_list_listener)
        
        self.model.gestor_usuarios.add_event_listener(
            "salida_sistema", self.autentificacion_signout_listener)
        
        self.model.gestor_transaccion.add_event_listener(
            "lista_ganancias", self.ganancias_list_listener)    #DIEGO G
    
    def ingreso_ejecutivo_listener(self, data):
        self.home_menu_ejecutivo.update_view()
        self.view.switch("homeEjecutivo")
    
    def ingreso_gerente_listener(self, data):
        self.home_menu_gerente.update_view()
        self.view.switch("homeGerente")

    def monedas_activas_list_listener(self, data):
        self.list_active_controller.update_view()
        self.view.switch("listActive")
    
    def monedas_todas_list_listener(self, data):
        self.list_all_controller.update_view()
        self.view.switch("listAll")

    def cajas_list_listener(self, data):
        self.list_cajas.update_view()
        self.view.switch("listAllCajas")
    
    def saldos_list_listener(self, data):
        self.list_saldos.update_view()
        self.view.switch("listAllSaldos")

    def autentificacion_signout_listener(self, data):
        self.view.switch("login")

    def ganancias_list_listener(self, data):
        self.list_ganancias.update_view()
        self.view.switch("listGanancias")

    def start(self):
        self.view.switch("login")
        self.view.start_mainloop()
