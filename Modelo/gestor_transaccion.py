from .event_handler import ObservableModel
from .transaccion_DAO import Transaccion_DAO
from .conectorBD import ConectorBD

class Gestor_transaccion(ObservableModel):
    
    def __init__(self):
        super().__init__()
        self.conectorBD = ConectorBD(hostdb="localhost", userdb="root", passwordb="", basedatosdb="casa_ACME")
        self.usuario_DAO = Transaccion_DAO(self.conectorBD)