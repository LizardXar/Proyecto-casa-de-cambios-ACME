class Caja_DAO:
    
    # Inicializa la clase con un conector a la base de datos
    def __init__(self, conector_bd):
        self.conector_bd = conector_bd
    
    # Recupera la lista de cajas con el estado y el empleado asignado
    def recuperar_cajas(self):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None

        sql = """SELECT c.cod_caja, e.nombre AS nombre_empleado, 
                 CASE WHEN c.estado = 1 THEN 'activo' 
                      WHEN c.estado = 2 THEN 'inactivo' END AS estado 
                 FROM caja c 
                 JOIN empleado e ON c.empleado_cod_empleado = e.cod_empleado;"""
        estado, datos_dto = self.conector_bd.ejecutarSelectAll(sql)

        lista_cajas_dto = {}
        if estado == 0:
            for i in range(len(datos_dto)):
                registro_dto = {"codigo": datos_dto[i][0], "empleado": datos_dto[i][1], "estado": datos_dto[i][2]}
                lista_cajas_dto[i] = registro_dto

        self.conector_bd.desactivarConexion()
        return estado, lista_cajas_dto

    # Recupera el saldo de una caja específica sin incluir CLP
    def recuperar_saldo_caja(self, codigo):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None

        sql = f"""
                SELECT m.nom_moneda, s.disponibilidad
                FROM saldo_caja s
                JOIN moneda m ON s.cod_moneda = m.cod_moneda
                WHERE s.cod_caja = {codigo} 
                AND m.cod_moneda NOT IN 
                (SELECT cod_moneda FROM moneda WHERE nom_moneda = 'CLP');
                """
        estado, datos_dto = self.conector_bd.ejecutarSelectAll(sql)

        lista_saldos_dto = {}
        if estado == 0:
            for i in range(len(datos_dto)):
                registro_dto = {"moneda": datos_dto[i][0], "saldo": datos_dto[i][1]}
                lista_saldos_dto[i] = registro_dto

        self.conector_bd.desactivarConexion()
        return estado, lista_saldos_dto

    # Recupera el saldo de CLP de una caja específica
    def recuperar_clp_caja(self, codigo):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None

        sql = f"""
            SELECT s.disponibilidad
            FROM saldo_caja s
            JOIN moneda m ON s.cod_moneda = m.cod_moneda
            WHERE s.cod_caja = {codigo} 
            AND m.nom_moneda = 'CLP';
        """
        estado, datos_dto = self.conector_bd.ejecutarSelectOne(sql)

        if estado == 0 and datos_dto:
            self.conector_bd.desactivarConexion()
            return estado, float(datos_dto[0])

        self.conector_bd.desactivarConexion()
        return estado, 0.0

    # Actualiza el saldo de CLP de una caja específica
    def actualizar_saldo_clp(self, cod_caja, monto):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado

        sql = f"""
            UPDATE saldo_caja 
            SET disponibilidad = {monto}
            WHERE cod_caja = {cod_caja} 
            AND cod_moneda = (SELECT cod_moneda FROM moneda WHERE nom_moneda = 'CLP');
        """
        estado = self.conector_bd.ejecutarUpdate(sql)
        self.conector_bd.desactivarConexion()
        return estado

    # Incrementa el saldo de una moneda específica en una caja
    def actualizar_saldo_moneda(self, cod_caja, cod_moneda, cantidad):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado

        sql = f"""
            UPDATE saldo_caja 
            SET disponibilidad = disponibilidad + {cantidad}
            WHERE cod_caja = {cod_caja} 
            AND cod_moneda = {cod_moneda};
        """
        estado = self.conector_bd.ejecutarUpdate(sql)
        self.conector_bd.desactivarConexion()
        return estado

    # Obtiene el código de la caja asociada a un empleado
    def obtener_caja_de_empleado(self, cod_empleado):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None

        sql = f"""
            SELECT cod_caja 
            FROM caja 
            WHERE empleado_cod_empleado = {cod_empleado};
        """
        estado, datos_dto = self.conector_bd.ejecutarSelectOne(sql)

        if estado == 0 and datos_dto:
            return estado, datos_dto[0]

        return estado, None
