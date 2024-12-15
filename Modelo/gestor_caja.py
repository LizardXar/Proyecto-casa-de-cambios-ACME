from .event_handler import ModeloObservable
from .caja_DAO import Caja_DAO
from .conectorBD import ConectorBD

class Gestor_Caja(ModeloObservable):

    # Inicializa la clase con el modelo Observable y el conector a la base de datos
    def __init__(self):
        super().__init__()
        self.conector_bd = ConectorBD(hostdb="localhost", userdb="root", passwordb="", basedatosdb="casa_ACME")
        self.caja_dao = Caja_DAO(self.conector_bd)

    # Dispara el evento para recuperar la lista de todas las cajas
    def recuperar_cajas(self):
        self.trigger_event("lista_caja")

    # Recupera y devuelve la lista de todas las cajas desde el DAO
    def desplegar_cajas(self):
        lista_dto = self.caja_dao.recuperar_cajas()
        return lista_dto
    
    # Dispara el evento para recuperar la lista de saldos
    def recuperar_saldo(self):
        self.trigger_event("lista_saldos")

    # Recupera y devuelve el saldo de una caja específica desde el DAO
    def desplegar_saldo(self, codigo):
        lista_dto = self.caja_dao.recuperar_saldo_caja(codigo)
        return lista_dto

    def actualizar_saldo_clp(self, cod_caja, monto):
        return self.caja_dao.actualizar_saldo_clp(cod_caja, monto)

    def actualizar_saldo_moneda(self, cod_caja, cod_moneda, cantidad):
        return self.caja_dao.actualizar_saldo_moneda(cod_caja, cod_moneda, cantidad)