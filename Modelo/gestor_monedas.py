from .event_handler import ModeloObservable
from .monedas_DAO import Monedas_DAO
from .conectorBD import ConectorBD

class Gestor_Monedas(ModeloObservable):

    # Inicializa la clase con el modelo Observable y el conector a la base de datos
    def __init__(self):
        super().__init__()
        self.conector_bd = ConectorBD()
        self.monedas_dao = Monedas_DAO(self.conector_bd)
        self.moneda_seleccionada = None  # Variable para almacenar la moneda seleccionada

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
    
    # Recupera y almacena una moneda seleccionada
    def seleccionar_moneda(self, cod_moneda):
        estado, moneda_dto = self.monedas_dao.recuperar_una_moneda(cod_moneda)
        if estado == 0 and moneda_dto:
            self.moneda_seleccionada = moneda_dto
            self.trigger_event("modificar_tipo_cambio") 
            return moneda_dto
        self.moneda_seleccionada = None  
        return None
    
    # Dispara el evento para modificar el tipo de cambio de la moneda seleccionada
    def notificar_modificar_tipo_cambio(self):
        self.trigger_event("modificar_tipo_cambio")

    # Obtiene el tipo de cambio de una moneda específica
    def obtener_tipo_cambio(self, cod_moneda):
        estado, tipo_cambio_dto = self.monedas_dao.obtener_tipo_cambio(cod_moneda)
        if estado == 0:
            return tipo_cambio_dto
        
    # Recupera los datos de una moneda específica por su código
    def recuperar_una_moneda(self, cod_moneda):
        estado, moneda_dto = self.monedas_dao.recuperar_una_moneda(cod_moneda)
        return estado, moneda_dto

    # Recupera la moneda seleccionada actual
    def obtener_moneda_seleccionada(self):
        return self.moneda_seleccionada
    
    # Actualiza el tipo de cambio de una moneda en la base de datos
    def actualizar_tipo_cambio(self, cod_moneda, nuevo_tipo_cambio):
       estado = self.monedas_dao.modificar_tipo_de_cambio(cod_moneda, nuevo_tipo_cambio)
       return estado
