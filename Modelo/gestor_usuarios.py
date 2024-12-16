from .event_handler import ModeloObservable
from .usuarios_DAO import Usuarios_DAO
from .conectorBD import ConectorBD

class Gestor_Usuarios(ModeloObservable):

    # Inicializa la clase con el modelo Observable y el conector a la base de datos
    def __init__(self):
        super().__init__()
        self.conectorBD = ConectorBD()
        self.usuario_DAO = Usuarios_DAO(self.conectorBD)
        self.current_user = None  # Variable para almacenar el nombre del usuario actual
        self.current_user_id = None  # Variable para almacenar el ID del usuario actual

    # Realiza el inicio de sesión y establece el usuario actual
    def login(self, datos_dto):
        estado, lista_dto = self.usuario_DAO.buscar_usuario(datos_dto)

        if estado == 0 and lista_dto:  # Si la búsqueda fue exitosa
            self.current_user = lista_dto["nombre"]
            self.current_user_id = lista_dto["cod_tipo_empleado"]

            if lista_dto["cod_tipo_empleado"] == 1:  # Ejecutivo
                self.trigger_event("ingreso_ejecutivo")

            elif lista_dto["cod_tipo_empleado"] == 2:  # Gerente
                self.trigger_event("ingreso_gerente")
                
            elif lista_dto["cod_tipo_empleado"] == 4:  # Cajero
                self.current_user_id = lista_dto["cod_empleado"]
                self.trigger_event("ingreso_cajero")

    # Retorna el nombre del usuario actual
    def saludo_usuario(self):
        return self.current_user
    
    # Retorna el código del empleado actual
    def retornar_cod_empleado(self):
        return self.current_user_id
    
    # Cierra la sesión actual y dispara el evento de salida del sistema
    def cerrar_sesion(self):
        self.trigger_event("salida_sistema")
