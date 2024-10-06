from .event_handler import ObservableModel
from .monedas_DAO import Monedas_DAO

class Gestor_Monedas(ObservableModel):

    def __init__(self):
        super().__init__()
        self.monedas_DAO = Monedas_DAO()

    def recuperar_monedas(self):
        self.trigger_event("lista_monedas")

    def recuperar_monedas_activas(self):
        self.trigger_event("lista_monedas_activas")
    
    def recuperar_monedas_inactivas(self):
        self.trigger_event("lista_monedas_inactivas")
    
    def desplegar_monedas(self):
        lista_DTO = self.monedas_DAO.leer_monedas()
        return lista_DTO
    