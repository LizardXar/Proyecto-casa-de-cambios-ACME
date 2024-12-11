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
