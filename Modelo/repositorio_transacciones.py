import re  # Importar la librería para trabajar con expresiones regulares
from .gestor_caja import Gestor_Caja
from .gestor_transaccion import Gestor_Transaccion
from .gestor_monedas import Gestor_Monedas

class RepositorioTransacciones:

    # Inicializa la clase con los gestores de caja, transacciones y monedas
    def __init__(self):
        self.gestor_caja = Gestor_Caja()
        self.gestor_transaccion = Gestor_Transaccion()
        self.gestor_monedas = Gestor_Monedas()

    # Realiza una transacción entre CLP y una moneda extranjera
    def realizar_transaccion(self, cod_caja, cod_moneda, monto_moneda_extranjera):
        # Validar que monto_moneda_extranjera tenga máximo 2 decimales
        if not re.match(r"^\d+(\.\d{1,2})?$", str(monto_moneda_extranjera)):
            raise ValueError("El monto debe ser un número positivo con hasta 2 decimales.")

        # Registrar la transacción
        estado = self.gestor_transaccion.registrar_transaccion(cod_caja, cod_moneda, monto_moneda_extranjera)
        if estado != 0:
            raise Exception("Error al registrar la transacción.")

        # Obtener el tipo de cambio
        tipo_cambio = self.obtener_tipo_cambio(cod_moneda)
        if tipo_cambio == 0:
            raise Exception("Error al obtener el tipo de cambio.")

        # Calcular el total en CLP
        total_clp = float(monto_moneda_extranjera) * tipo_cambio

        # Obtener el saldo CLP actual
        saldo_actual_clp = self.obtener_saldo_clp(cod_caja)
        if saldo_actual_clp < total_clp:
            raise Exception("Saldo insuficiente para realizar la transacción.")

        # Calcular el nuevo saldo restando el total de CLP
        nuevo_saldo_clp = saldo_actual_clp - total_clp

        # Actualizar el saldo de CLP
        estado = self.gestor_caja.actualizar_saldo_clp(cod_caja, nuevo_saldo_clp)
        if estado != 0:
            raise Exception("Error al actualizar el saldo CLP.")

        # Incrementar el saldo de la moneda extranjera
        estado = self.gestor_caja.actualizar_saldo_moneda(cod_caja, cod_moneda, float(monto_moneda_extranjera))
        if estado != 0:
            raise Exception("Error al actualizar el saldo de la moneda extranjera.")

    # Recupera la lista de cajas disponibles
    def recuperar_cajas(self):
        estado, cajas_dto = self.gestor_caja.caja_dao.recuperar_cajas()
        if estado != 0:
            raise Exception(f"Error al recuperar cajas: Código de error {estado}")
        return cajas_dto

    # Recupera la lista de monedas activas
    def recuperar_monedas(self):
        estado, monedas_dto = self.gestor_monedas.monedas_dao.recuperar_lista_monedas_activas()
        if estado != 0:
            raise Exception(f"Error al recuperar monedas: Código de error {estado}")
        return monedas_dto

    # Obtiene el saldo de CLP de una caja específica
    def obtener_saldo_clp(self, cod_caja):
        estado, saldo_dto = self.gestor_caja.caja_dao.recuperar_clp_caja(cod_caja)
        if estado == 0:
            return saldo_dto
        return 0.0

    # Obtiene el tipo de cambio de una moneda específica
    def obtener_tipo_cambio(self, cod_moneda):
        return self.gestor_monedas.obtener_tipo_cambio(cod_moneda)
