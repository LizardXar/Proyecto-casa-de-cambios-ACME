from .event_handler import ModeloObservable
from .transaccion_DAO import Transaccion_DAO
from .conectorBD import ConectorBD

class Gestor_Transaccion(ModeloObservable):

    # Inicializa la clase con el modelo Observable y el conector a la base de datos
    def __init__(self):
        super().__init__()
        self.conector_bd = ConectorBD()
        self.transaccion_dao = Transaccion_DAO(self.conector_bd)
    
    # Dispara el evento para recuperar la lista de ganancias
    def recuperar_ganancias(self):
        self.trigger_event("lista_ganancias")

    # Recupera y devuelve la lista de ganancias desde el DAO
    def desplegar_ganancias(self):
        lista_dto = self.transaccion_dao.recuperar_ganancias()
        return lista_dto
    
    # Dispara el evento para recuperar la lista de monedas más vendidas
    def recuperar_moneda_mas_vendida(self):
        self.trigger_event("lista_monedas_trazadas")

    # Recupera y devuelve la lista de monedas más vendidas desde el DAO
    def desplegar_moneda_mas_vendida(self):
        lista_dto = self.transaccion_dao.obtener_moneda_mas_vendida()
        return lista_dto

    # Dispara el evento para realizar una transacción
    def realizar_transaccion(self):
        self.trigger_event("realizar_transaccion")

    # Registra una transacción en la base de datos
    def registrar_transaccion(self, caja_dto, moneda_dto, monto_clp_dto):
        return self.transaccion_dao.registrar_transaccion(caja_dto, moneda_dto, monto_clp_dto)
