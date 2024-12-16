class Monedas_DAO:

    # Inicializa la clase con un conector a la base de datos
    def __init__(self, conector_bd):
        self.conector_bd = conector_bd

    # Recupera la lista de todas las monedas
    def recuperar_lista_monedas(self):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None
        
        sql = """SELECT cod_moneda, nom_moneda, tipo_cambio 
                 FROM moneda 
                 WHERE cod_moneda NOT IN 
                 (SELECT cod_moneda FROM moneda WHERE nom_moneda = 'CLP') 
                 ORDER BY cod_moneda"""
        estado, datos_dto = self.conector_bd.ejecutarSelectAll(sql)

        lista_monedas_dto = {}

        if estado == 0:
            for i in range(len(datos_dto)):
                registro_dto = {"codigo": datos_dto[i][0], "nombre": datos_dto[i][1], "tipo": datos_dto[i][2]}
                lista_monedas_dto[i] = registro_dto

        self.conector_bd.desactivarConexion()
        return estado, lista_monedas_dto
    
    # Recupera la lista de monedas activas
    def recuperar_lista_monedas_activas(self):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None
        
        sql = """SELECT cod_moneda, nom_moneda, tipo_cambio, estado 
                 FROM moneda 
                 WHERE estado = 1 
                 AND cod_moneda NOT IN 
                 (SELECT cod_moneda FROM moneda WHERE nom_moneda = 'CLP') 
                 ORDER BY cod_moneda;
              """
        estado, datos_dto = self.conector_bd.ejecutarSelectAll(sql)

        lista_monedas_dto = {}

        if estado == 0:
            for i in range(len(datos_dto)):
                registro_dto = {"codigo": datos_dto[i][0], "nombre": datos_dto[i][1], "tipo": datos_dto[i][2], "estado": datos_dto[i][3]}
                lista_monedas_dto[i] = registro_dto

        self.conector_bd.desactivarConexion()
        return estado, lista_monedas_dto

    # Modifica el tipo de cambio de una moneda
    def modificar_tipo_de_cambio(self, cod_moneda, nuevo_tipo_cambio):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado
        
        sql = f"UPDATE moneda SET tipo_cambio = '{nuevo_tipo_cambio}' WHERE cod_moneda = '{cod_moneda}';"
        estado = self.conector_bd.ejecutarUpdate(sql)

        self.conector_bd.desactivarConexion()
        return estado

    # Obtiene el tipo de cambio de una moneda específica
    def obtener_tipo_cambio(self, cod_moneda):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None
        
        sql = f"SELECT tipo_cambio FROM moneda WHERE cod_moneda = {cod_moneda}"
        estado, datos_dto = self.conector_bd.ejecutarSelectOne(sql)

        if estado == 0 and datos_dto:
            self.conector_bd.desactivarConexion()
            return estado, float(datos_dto[0])
        
        self.conector_bd.desactivarConexion()
        return estado, None

    # Recupera la información de una moneda específica
    def recuperar_una_moneda(self, cod_moneda):
        estado = self.conector_bd.activarConexion()
        if estado == 66:
            return estado, None
        
        sql = f"""SELECT cod_moneda, nom_moneda, tipo_cambio 
                  FROM moneda 
                  WHERE cod_moneda = {cod_moneda}"""
        estado, datos_dto = self.conector_bd.ejecutarSelectOne(sql)

        if estado == 0 and datos_dto:
            self.conector_bd.desactivarConexion()
            return estado, {"codigo": datos_dto[0], "nombre": datos_dto[1], "tipo": datos_dto[2]}
        
        self.conector_bd.desactivarConexion()
        return estado, None
