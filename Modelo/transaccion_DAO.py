class Transaccion_DAO:

    def __init__(self, conectorBD):
        self.conectorBD = conectorBD

    def obtener_moneda_mas_vendida(self):
        estado = self.conectorBD.activarConexion()

        if estado == 66:
            return estado, None

        sql = """
        SELECT 
            m.nom_moneda, 
            COUNT(*) AS cantidad_transacciones
        FROM 
            transaccion t
        JOIN 
            moneda m
        ON 
            t.cod_moneda = m.cod_moneda
        GROUP BY 
            m.nom_moneda
        ORDER BY 
            cantidad_transacciones DESC
        ;
        """
        
        estado, datos = self.conectorBD.ejecutarSelectAll(sql)

        moneda_mas_vendida_DTO = {}

        if estado == 0:
            for i in range(len(datos)):
                registro = {"moneda": datos[i][0], "trazada": datos[i][1]}
                moneda_mas_vendida_DTO[i] = registro

        self.conectorBD.desactivarConexion()
        return estado, moneda_mas_vendida_DTO