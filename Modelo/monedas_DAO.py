class Monedas_DAO:

    # Inicializa la clase con un conector a la base de datos
    def __init__(self, conector_bd):
        self.conector_bd = conector_bd

    # Recupera la lista de todas las monedas
    def recuperar_lista_monedas(self):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None
        
        sql = "SELECT cod_moneda, nom_moneda, tipo_cambio FROM moneda ORDER BY cod_moneda"
        estado, datos = self.conector_bd.ejecutarSelectAll(sql)

        lista_monedas_dto = {}

        if estado == 0:
            for i in range(len(datos)):
                registro = {"codigo": datos[i][0], "nombre": datos[i][1], "tipo": datos[i][2]}
                lista_monedas_dto[i] = registro

        self.conector_bd.desactivarConexion()
        return estado, lista_monedas_dto
    
    # Recupera la lista de monedas activas
    def recuperar_lista_monedas_activas(self):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None
        
        sql = "SELECT cod_moneda, nom_moneda, tipo_cambio, estado FROM moneda WHERE estado = 1 ORDER BY cod_moneda"
        estado, datos = self.conector_bd.ejecutarSelectAll(sql)

        lista_monedas_dto = {}

        if estado == 0:
            for i in range(len(datos)):
                registro = {"codigo": datos[i][0], "nombre": datos[i][1], "tipo": datos[i][2], "estado": datos[i][3]}
                lista_monedas_dto[i] = registro

        self.conector_bd.desactivarConexion()
        return estado, lista_monedas_dto

    # Modificar el tipo de cambio de una moneda
    def modificar_tipo_de_cambio(self, cod_moneda, nuevo_tipo_cambio):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None
        
        sql = f"UPDATE moneda SET tipo_cambio = '{nuevo_tipo_cambio}' WHERE cod_moneda = '{cod_moneda}';"
        estado = self.conector_bd.ejecutarUpdate(sql)

        if estado == 0:
            self.conector_bd.desactivarConexion()
            return estado
        return estado

    def obtener_tipo_cambio(self, cod_moneda):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None
        
        sql = f"SELECT tipo_cambio FROM moneda WHERE cod_moneda = {cod_moneda}"
        estado, datos = self.conector_bd.ejecutarSelectOne(sql)

        if estado == 0 and datos:
            return estado, float(datos[0])

    def recuperar_una_moneda(self, cod_moneda):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None
        
        sql = f"""select cod_moneda, nom_moneda, tipo_cambio 
                from moneda WHERE cod_moneda = {cod_moneda}"""
        estado, datos = self.conector_bd.ejecutarSelectOne(sql)

        if estado == 0 and datos:
            return estado, {"codigo": datos[0], "nombre": datos[1], "tipo": datos[2]}
