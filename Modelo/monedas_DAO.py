class Monedas_DAO:

    def __init__(self, conectorBD):
        self.conectorBD = conectorBD

    def recuperar_listaMonedas(self):
        estado = self.conectorBD.activarConexion()

        if estado == 66:
            return estado, None
        
        sql = "SELECT cod_moneda, nom_moneda, tipo_cambio FROM monedas order by cod_moneda"
        estado, datos = self.conectorBD.ejecutarSelectAll(sql)

        listaMonedas_DTO = {}

        if estado == 0:
            for i in range(0, len(datos)):
                registro = {"codigo": datos[i][0], "nombre": datos[i][1], "tipo": datos[i][2]}
                listaMonedas_DTO[i] = registro

        self.conectorBD.desactivarConexion()

        return estado, listaMonedas_DTO
    
    def recuperar_listaMonedas_activas(self):
        estado = self.conectorBD.activarConexion()

        if estado == 66:
            return estado, None
        
        sql = "SELECT cod_moneda, nom_moneda, tipo_cambio FROM monedas where estado = 1 order by cod_moneda"
        estado, datos = self.conectorBD.ejecutarSelectAll(sql)

        listaMonedas_DTO = {}

        if estado == 0:
            for i in range(0, len(datos)):
                registro = {"codigo": datos[i][0], "nombre": datos[i][1], "tipo": datos[i][2]}
                listaMonedas_DTO[i] = registro

        self.conectorBD.desactivarConexion()

        return estado, listaMonedas_DTO
