class Transaccion_DAO:

    # Inicializa la clase con un conector a la base de datos
    def __init__(self, conector_bd):
        self.conector_bd = conector_bd

    # Recupera las ganancias por moneda de las transacciones
    def recuperar_ganancias(self):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None

        sql = """
            SELECT 
            m.nom_moneda,
            ROUND(SUM(t.monto_transferido * m.tipo_cambio * 0.05), 2) AS ganancia_total,
            ROUND(SUM(t.monto_transferido * m.tipo_cambio), 2) AS monto_total
            FROM transaccion t
            JOIN moneda m ON t.cod_moneda = m.cod_moneda
            GROUP BY m.nom_moneda
            ORDER BY ganancia_total DESC;
            """
        estado, datos = self.conector_bd.ejecutarSelectAll(sql)
        
        lista_ganancias_dto = {}
        
        if estado == 0:
            for i in range(len(datos)):
                registro = {"moneda": datos[i][0], "ganancia": datos[i][1], "monto": datos[i][2]}
                lista_ganancias_dto[i] = registro

        self.conector_bd.desactivarConexion()
        return estado, lista_ganancias_dto
    
    # Obtiene la moneda más vendida
    def obtener_moneda_mas_vendida(self):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None

        sql = """
            SELECT m.nom_moneda, COUNT(*) AS cantidad_transacciones
            FROM transaccion t
            JOIN moneda m ON t.cod_moneda = m.cod_moneda
            GROUP BY m.nom_moneda
            ORDER BY cantidad_transacciones DESC;
            """
        
        estado, datos = self.conector_bd.ejecutarSelectAll(sql)

        lista_monedas_vendidas_dto = {}


        if estado == 0:
            for i in range(len(datos)):
                registro = {"moneda": datos[i][0], "trazada": datos[i][1]}
                lista_monedas_vendidas_dto[i] = registro

        self.conector_bd.desactivarConexion()
        return estado, lista_monedas_vendidas_dto
    
    def registrar_transaccion(self, cod_caja, cod_moneda, monto_clp):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado

        sql = f"""
            INSERT INTO transaccion (cod_caja, cod_moneda, monto_transferido, fecha_transaccion)
            VALUES ({cod_caja}, {cod_moneda}, {monto_clp}, NOW())
        """
        estado = self.conector_bd.ejecutarInsert(sql)
        self.conector_bd.desactivarConexion()
        return estado
