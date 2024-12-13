class Caja_DAO:

    # Inicializa la clase con un conector a la base de datos
    def __init__(self, conector_bd):
        self.conector_bd = conector_bd
    
    # Recupera la lista de cajas con el estado y el empleado asignado
    def recuperar_cajas(self):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None
        
        sql = """SELECT c.cod_caja, e.nombre AS nombre_empleado, CASE WHEN c.estado = 1 THEN 'activo' WHEN c.estado = 2 THEN 'inactivo' END AS estado 
        FROM caja c JOIN empleado e ON c.empleado_cod_empleado = e.cod_empleado;"""
        estado, datos = self.conector_bd.ejecutarSelectAll(sql)

        lista_cajas_dto = {}

        if estado == 0:
            for i in range(len(datos)):
                registro = {"codigo": datos[i][0], "empleado": datos[i][1], "estado": datos[i][2]}
                lista_cajas_dto[i] = registro
        
        self.conector_bd.desactivarConexion()
        return estado, lista_cajas_dto
    
    # Recupera el saldo de una caja específica
    def recuperar_saldo_caja(self, codigo):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None
        
        sql = f"""
                SELECT m.nom_moneda, s.disponibilidad
                FROM saldo_caja s
                JOIN moneda m ON s.cod_moneda = m.cod_moneda
                WHERE s.cod_caja = {codigo};
                """
        estado, datos = self.conector_bd.ejecutarSelectAll(sql)

        lista_saldos_dto = {}

        if estado == 0:
            for i in range(len(datos)):
                registro = {"moneda": datos[i][0], "saldo": datos[i][1]}
                lista_saldos_dto[i] = registro
        
        self.conector_bd.desactivarConexion()
        return estado, lista_saldos_dto
