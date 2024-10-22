from .home_menu import HomeController
from .list_monedas_activas import ListActiveController
from .list_monedas_todas import ListAllController

class Controller:

    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.home_controller = HomeController(model, view)
        self.list_active_controller = ListActiveController(model, view)
        self.list_all_controller = ListAllController(model, view)

        self.model.gestor_monedas.add_event_listener(
            "lista_monedas_activas", self.monedas_activas_list_listener)
        
        self.model.gestor_monedas.add_event_listener(
            "lista_monedas", self.monedas_todas_list_listener)
    
    def monedas_activas_list_listener(self, data):
        self.list_active_controller.update_view()
        self.view.switch("listActive")
    
    
    def monedas_todas_list_listener(self, data):
        self.list_all_controller.update_view()
        self.view.switch("listAll")

    def start(self):
        self.view.switch("home")
        self.view.start_mainloop()