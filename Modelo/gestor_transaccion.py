from .event_handler import ObservableModel
from .transaccion_DAO import Transaccion_DAO
from .conectorBD import ConectorBD

class Gestor_transaccion(ObservableModel):

    def __init__(self):
        super().__init__()
        self.conectorBD = ConectorBD(hostdb="localhost", userdb="root", passwordb="", basedatosdb="casa_ACME")
        self.transaccion_DAO = Transaccion_DAO(self.conectorBD)

    def recuperar_moneda_mas_vendida(self):
        self.trigger_event("lista_monedas_trazadas")

    def desplegar_moneda_mas_vendida(self):
        moneda_DTO = self.transaccion_DAO.obtener_moneda_mas_vendida()
        return moneda_DTO

