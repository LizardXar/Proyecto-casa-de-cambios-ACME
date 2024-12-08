from .event_handler import ObservableModel
from .usuarios_DAO import Usuarios_DAO
from .conectorBD import ConectorBD

class Gestor_Usuarios(ObservableModel):

    def __init__(self):
        super().__init__()
        self.conectorBD = ConectorBD(hostdb="localhost", userdb="root", passwordb="", basedatosdb="casa_ACME")
        self.usuario_DAO = Usuarios_DAO(self.conectorBD)
        self.current_user = None

    def login(self, datos_DTO):
        estado, lista_DTO = self.usuario_DAO.buscar_user(datos_DTO)

        if estado == 0 and lista_DTO:
            self.current_user = lista_DTO["nombre"]

            if lista_DTO["cod_tipo_empleado"] == 1:
                self.trigger_event("ingreso_ejecutivo")
            elif lista_DTO["cod_tipo_empleado"] == 2:
                self.trigger_event("ingreso_gerente")

    def saludo_usuario(self):
        return self.current_user
    
    def logout(self):
        self.trigger_event("salida_sistema")