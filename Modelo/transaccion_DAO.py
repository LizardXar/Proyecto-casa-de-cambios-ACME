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
            ROUND(SUM(t.monto_transferido * m.tipo_cambio * 0.05),2) AS ganancia_total,
            ROUND(SUM(t.monto_transferido * m.tipo_cambio), 2) as monto_total
            FROM transaccion t
            JOIN moneda m ON t.cod_moneda = m.cod_moneda
            GROUP BY m.nom_moneda
            ORDER BY ganancia_total DESC;
            """
        estado, datos = self.conectorBD.ejecutarSelectAll(sql)
        
        listaGanancias_DTO = {}
        
        if estado == 0:
            for i in range(len(datos)):
                registro = {"moneda": datos[i][0], "ganancia": datos[i][1], "monto":datos[i][2]}
                listaGanancias_DTO[i] = registro

        self.conectorBD.desactivarConexion()
        return estado, listaGanancias_DTO
    
    def obtener_moneda_mas_vendida(self):
        estado = self.conectorBD.activarConexion()
        if estado == 66:
            return estado, None

        sql = """
            SELECT m.nom_moneda, COUNT(*) AS cantidad_transacciones
            FROM transaccion t
            JOIN moneda m ON t.cod_moneda = m.cod_moneda
            GROUP BY m.nom_moneda
            ORDER BY cantidad_transacciones DESC;
            """
        
        estado, datos = self.conectorBD.ejecutarSelectAll(sql)

        listaMonedasVendidas_DTO = {}

        if estado == 0:
            for i in range(len(datos)):
                registro = {"moneda": datos[i][0], "trazada": datos[i][1]}
                listaMonedasVendidas_DTO[i] = registro

        self.conectorBD.desactivarConexion()
        return estado, listaMonedasVendidas_DTO