class Usuarios_DAO:

    def __init__(self, conectorBD):
        self.conectorBD = conectorBD

    def buscar_user(self, data_DTO):
        correo = data_DTO['correo']
        clave = data_DTO['clave']
        
        estado = self.conectorBD.activarConexion()

        if estado == 66:
            return estado, None
        
        sql = f"""
                SELECT nombre, cod_tipo_empleado
                FROM empleado
                WHERE correo = '{correo}' and clave = '{clave}';
            """

        estado, datos = self.conectorBD.ejecutarSelectAll(sql)

        if estado == 0 and datos:
            registro = {"cod_tipo_empleado": datos[0][1], "nombre": datos[0][0]}
            self.conectorBD.desactivarConexion()
            return estado, registro

        self.conectorBD.desactivarConexion()
        return estado, None
