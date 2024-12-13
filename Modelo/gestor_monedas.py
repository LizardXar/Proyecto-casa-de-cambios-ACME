from .event_handler import ModeloObservable
from .monedas_DAO import Monedas_DAO
from .conectorBD import ConectorBD

class Gestor_Monedas(ModeloObservable):

    # Inicializa la clase con el modelo Observable y el conector a la base de datos
    def __init__(self):
        super().__init__()
        self.conector_bd = ConectorBD(hostdb="localhost", userdb="root", passwordb="", basedatosdb="casa_ACME")
        self.monedas_dao = Monedas_DAO(self.conector_bd)

    # Dispara el evento para recuperar la lista de todas las monedas
    def recuperar_monedas(self):
        self.trigger_event("lista_monedas")
    
    # Recupera y devuelve la lista de todas las monedas desde el DAO
    def desplegar_monedas(self):
        lista_dto = self.monedas_dao.recuperar_lista_monedas()
        return lista_dto
    
    # Dispara el evento para recuperar la lista de monedas activas
    def recuperar_monedas_activas(self):
        self.trigger_event("lista_monedas_activas")
    
    # Recupera y devuelve la lista de monedas activas desde el DAO
    def desplegar_monedas_activas(self):
        lista_dto = self.monedas_dao.recuperar_lista_monedas_activas()
        return lista_dto
