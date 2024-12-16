from .event_handler import ModeloObservable
from .caja_DAO import Caja_DAO
from .conectorBD import ConectorBD

class Gestor_Caja(ModeloObservable):

    # Inicializa la clase con el modelo Observable y el conector a la base de datos
    def __init__(self):
        super().__init__()
        self.conector_bd = ConectorBD()
        self.caja_dao = Caja_DAO(self.conector_bd)
        self.caja_seleccionada = None

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
    
    # Recupera y devuelve el saldo de CLP de una caja específica
    def desplegar_saldo_clp(self, codigo):
        estado, saldo_dto = self.caja_dao.recuperar_clp_caja(codigo)
        return saldo_dto  # Retorna el saldo directamente como float

    # Actualiza el saldo de CLP de una caja específica
    def actualizar_saldo_clp(self, cod_caja, monto):
        return self.caja_dao.actualizar_saldo_clp(cod_caja, monto)

    # Actualiza el saldo de una moneda específica en una caja
    def actualizar_saldo_moneda(self, cod_caja, cod_moneda, cantidad):
        return self.caja_dao.actualizar_saldo_moneda(cod_caja, cod_moneda, cantidad)
    
    # Obtiene la caja actualmente seleccionada
    def obtener_caja_seleccionada(self):
        return self.caja_seleccionada
    
    # Dispara el evento para ver el saldo de la caja seleccionada
    def notificar_ver_saldo(self):
        self.trigger_event("lista_saldos")
    
    # Dispara el evento para registrar la disponibilidad de una caja
    def notificar_registrar_disponibilidad_caja(self):
        self.trigger_event("registrarDisponibilidadPesos")

    # Obtiene el código de la caja asociada a un empleado
    def obtener_caja_asociada(self, cod_empleado):
        estado, cod_caja_dto = self.caja_dao.obtener_caja_de_empleado(cod_empleado)
        if estado == 0:
            return cod_caja_dto
