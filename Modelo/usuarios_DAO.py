class Usuarios_DAO:

    # Inicializa la clase con un conector a la base de datos
    def __init__(self, conector_bd):
        self.conector_bd = conector_bd

    # Busca un usuario en la base de datos utilizando los datos proporcionados
    def buscar_usuario(self, datos_dto):
        correo = datos_dto['correo']
        clave = datos_dto['clave']
        
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None
        
        sql = f"""
                SELECT nombre, cod_tipo_empleado, cod_empleado
                FROM empleado
                WHERE correo = '{correo}' AND clave = '{clave}';
            """
        estado, datos = self.conector_bd.ejecutarSelectAll(sql)

        if estado == 0 and datos:
            registro = {"cod_tipo_empleado": datos[0][1], "nombre": datos[0][0], "cod_empleado": datos[0][2]}
            self.conector_bd.desactivarConexion()
            return estado, registro

        self.conector_bd.desactivarConexion()
        return estado, None
