class Transaccion_DAO:

    def __init__(self, conectorBD):
        self.conectorBD = conectorBD

    def recuperar_ganancias(self):
        estado = self.conectorBD.activarConexion()
        if estado == 66:
            return estado, None

        sql = """
                SELECT 
                m.nom_moneda,
                SUM(t.monto_transferido * m.tipo_cambio * 0.05) AS ganancia_total
                FROM transaccion t
                JOIN moneda m ON t.cod_moneda = m.cod_moneda
                GROUP BY m.nom_moneda
                ORDER BY ganancia_total DESC;
            """
        estado, datos = self.conectorBD.ejecutarSelectAll(sql)
        
        listaGanancias_DTO = {}
        
        if estado == 0:
            for i in range(len(datos)):
                registro = {"moneda": datos[i][0], "ganancia": datos[i][1]}
                listaGanancias_DTO[i] = registro

        self.conectorBD.desactivarConexion()
        return estado, listaGanancias_DTO