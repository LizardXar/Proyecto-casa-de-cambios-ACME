from .event_handler import ObservableModel
from .transaccion_DAO import Transaccion_DAO
from .conectorBD import ConectorBD

class Gestor_Transaccion(ObservableModel):
    def __init__(self):
        super().__init__()
        self.conectorBD = ConectorBD(hostdb="localhost", userdb="root", passwordb="", basedatosdb="casa_acme")
        self.transaccion_DAO = Transaccion_DAO(self.conectorBD)
    
    def recuperar_ganancias(self):
        self.trigger_event("lista_ganancias")

    def desplegar_ganancias(self):
        lista_DTO = self.transaccion_DAO.recuperar_ganancias()
        return lista_DTO
    
    def recuperar_moneda_mas_vendida(self):
        self.trigger_event("lista_monedas_trazadas")

    def desplegar_moneda_mas_vendida(self):
        lista_DTO = self.transaccion_DAO.obtener_moneda_mas_vendida()
        return lista_DTO