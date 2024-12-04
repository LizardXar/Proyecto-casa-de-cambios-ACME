class Caja_DAO:
    def __init__(self, conectorBD):
        self.conectorBD = conectorBD
    
    def recuperar_cajas(self):
        estado = self.conectorBD.activarConexion()

        if estado == 66:
            return estado, None
        
        sql = """SELECT c.cod_caja, e.nombre AS nombre_empleado, CASE WHEN c.estado = 1 THEN 'activo' WHEN c.estado = 2 THEN 'inactivo' END AS estado 
        FROM caja c JOIN empleado e ON c.empleado_cod_empleado = e.cod_empleado;"""

        estado, datos = self.conectorBD.ejecutarSelectAll(sql)

        listaCajas_DTO = {}

        if estado == 0:
            for i in range(0, len(datos)):
                registro = {"codigo":datos[i][0], "empleado":datos[i][1], "estado":datos[i][2]}
                listaCajas_DTO[i] = registro
        
        self.conectorBD.desactivarConexion()

        return estado, listaCajas_DTO
    
    def recuperar_saldo_caja(self, codigo):
        estado = self.conectorBD.activarConexion()

        if estado == 66:
            return estado, None
        
        sql = f"""
                SELECT m.nom_moneda, s.disponibilidad
                FROM saldo_caja s
                JOIN moneda m ON s.cod_moneda = m.cod_moneda
                WHERE s.cod_caja = {codigo};
                """

        estado, datos = self.conectorBD.ejecutarSelectAll(sql)

        listaSaldos_DTO = {}

        if estado == 0:
            for i in range(0, len(datos)):
                registro = {"moneda":datos[i][0], "saldo":datos[i][1]}
                listaSaldos_DTO[i] = registro
        
        self.conectorBD.desactivarConexion()

        return estado, listaSaldos_DTO