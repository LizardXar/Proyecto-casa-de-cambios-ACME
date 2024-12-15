from .gestor_caja import Gestor_Caja
from .gestor_transaccion import Gestor_Transaccion
from .gestor_monedas import Gestor_Monedas

class RepositorioTransacciones:
    def __init__(self):
        self.gestor_caja = Gestor_Caja()
        self.gestor_transaccion = Gestor_Transaccion()
        self.gestor_monedas = Gestor_Monedas()

    def realizar_transaccion(self, cod_caja, cod_moneda, monto_clp):
        """
        Realiza una transacción, actualizando el saldo en CLP y en la moneda extranjera.
        """
        # Registrar la transacción
        estado = self.gestor_transaccion.registrar_transaccion(cod_caja, cod_moneda, monto_clp)
        if estado != 0:
            raise Exception("Error al registrar la transacción.")

        # Obtener el tipo de cambio
        tipo_cambio = self.obtener_tipo_cambio(cod_moneda)
        if tipo_cambio == 0:
            raise Exception("Error al obtener el tipo de cambio.")

        # Calcular el total en CLP y la cantidad en moneda extranjera
        total_clp = monto_clp * tipo_cambio

        # Actualizar el saldo de CLP
        estado = self.gestor_caja.actualizar_saldo_clp(cod_caja, total_clp)
        if estado != 0:
            raise Exception("Error al actualizar el saldo CLP.")

        # Incrementar el saldo de la moneda extranjera
        estado = self.gestor_caja.actualizar_saldo_moneda(cod_caja, cod_moneda, monto_clp)
        if estado != 0:
            raise Exception("Error al actualizar el saldo de la moneda extranjera.")


    def recuperar_cajas(self):
        estado, cajas = self.gestor_caja.caja_dao.recuperar_cajas()
        if estado != 0:
            raise Exception(f"Error al recuperar cajas: Código de error {estado}")
        return cajas

    def recuperar_monedas(self):
        estado, monedas = self.gestor_monedas.monedas_dao.recuperar_lista_monedas_activas()
        if estado != 0:
            raise Exception(f"Error al recuperar monedas: Código de error {estado}")
        return monedas

    def obtener_saldo_clp(self, cod_caja):
        estado, saldo = self.gestor_caja.caja_dao.recuperar_clp_caja(cod_caja)
        if estado == 0:
            return saldo
        return 0.0
    
    def obtener_tipo_cambio(self, cod_moneda):
        return self.gestor_monedas.obtener_tipo_cambio(cod_moneda)
