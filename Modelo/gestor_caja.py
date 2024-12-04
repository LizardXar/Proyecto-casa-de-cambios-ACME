from .event_handler import ObservableModel
from .caja_DAO import Caja_DAO
from .conectorBD import ConectorBD

class Gestor_Caja(ObservableModel):

    def __init__(self):
        super().__init__()
        self.conectorBD = ConectorBD(hostdb="localhost", userdb="root", passwordb="", basedatosdb="casa_ACME")
        self.caja_DAO = Caja_DAO(self.conectorBD)

    def recuperar_cajas(self):
        self.trigger_event("lista_caja")

    def desplegar_cajas(self):
        lista_DTO = self.caja_DAO.recuperar_cajas()
        return lista_DTO
    
    def recuperar_saldo(self):
        self.trigger_event("lista_saldos")

    def desplegar_saldo(self, codigo):
        lista_DTO = self.caja_DAO.recuperar_saldo_caja(codigo)
        return lista_DTO