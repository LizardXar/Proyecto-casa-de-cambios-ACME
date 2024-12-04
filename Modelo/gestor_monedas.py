from .event_handler import ObservableModel
from .monedas_DAO import Monedas_DAO
from .conectorBD import ConectorBD

class Gestor_Monedas(ObservableModel):

    def __init__(self):
        super().__init__()
        self.conectorBD = ConectorBD(hostdb="localhost", userdb="root", passwordb="", basedatosdb="casa_ACME")
        self.monedas_DAO = Monedas_DAO(self.conectorBD)

    def recuperar_monedas(self):
        self.trigger_event("lista_monedas")
    
    def desplegar_monedas(self):
        lista_DTO = self.monedas_DAO.recuperar_listaMonedas()
        return lista_DTO
    
    def recuperar_monedas_activas(self):
        self.trigger_event("lista_monedas_activas")
    
    def desplegar_monedas_activas(self):
        lista_DTO = self.monedas_DAO.recuperar_listaMonedas_activas()
        return lista_DTO
    