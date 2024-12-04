from .home_menu import HomeController
from .list_monedas_activas import ListActiveController
from .list_monedas_todas import ListAllController
from .list_cajas import ListCajaController
from .list_saldos import ListSaldoController

class Controller:

    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.home_controller = HomeController(model, view)
        self.list_active_controller = ListActiveController(model, view)
        self.list_all_controller = ListAllController(model, view)
        self.list_cajas = ListCajaController(model, view)
        self.list_saldos = ListSaldoController(model, view)

        self.model.gestor_monedas.add_event_listener(
            "lista_monedas_activas", self.monedas_activas_list_listener)
        
        self.model.gestor_monedas.add_event_listener(
            "lista_monedas", self.monedas_todas_list_listener)
        
        self.model.gestor_caja.add_event_listener(
            "lista_caja", self.cajas_list_listener)
        
        self.model.gestor_caja.add_event_listener(
            "lista_saldos", self.saldos_list_listener)
    
    def monedas_activas_list_listener(self, data):
        self.list_active_controller.update_view()
        self.view.switch("listActive")
    
    
    def monedas_todas_list_listener(self, data):
        self.list_all_controller.update_view()
        self.view.switch("listAll")

    def cajas_list_listener(self, data):
        self.list_cajas.update_view()
        self.view.switch("listAllCajas")
    
    def saldos_list_listener(self,data):
        cod_moneda = self.view.ventana_caja.frame.obtener_cod_moneda_seleccionada()
        self.list_saldos.update_view(cod_moneda)
        print("XDD")
        print(f"el codigo moneda es: {cod_moneda}")
        self.view.switch("listAllSaldos")

    def start(self):
        self.view.switch("home")
        self.view.start_mainloop()