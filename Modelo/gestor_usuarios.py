from .event_handler import ModeloObservable
from .usuarios_DAO import Usuarios_DAO
from .conectorBD import ConectorBD

class Gestor_Usuarios(ModeloObservable):

    def __init__(self):
        # Llama al constructor de la clase padre ObservableModel
        super().__init__()
        # Inicializa el conector a la base de datos
        self.conectorBD = ConectorBD(hostdb="localhost", userdb="root", passwordb="", basedatosdb="casa_ACME")
        # Crea una instancia de Usuarios_DAO con el conector de base de datos
        self.usuario_DAO = Usuarios_DAO(self.conectorBD)
        # Variable para almacenar el usuario actual
        self.current_user = None

    def login(self, datos_DTO):
        # Utiliza el método buscar_user de Usuarios_DAO para buscar el usuario
        estado, lista_DTO = self.usuario_DAO.buscar_usuario(datos_DTO)

        # Si la búsqueda fue exitosa y se encontró el usuario
        if estado == 0 and lista_DTO:
            # Asigna el nombre del usuario actual
            self.current_user = lista_DTO["nombre"]

            # Dependiendo del tipo de empleado, dispara un evento diferente
            if lista_DTO["cod_tipo_empleado"] == 1:
                self.trigger_event("ingreso_ejecutivo")
            elif lista_DTO["cod_tipo_empleado"] == 2:
                self.trigger_event("ingreso_gerente")

    def saludo_usuario(self):
        # Retorna el nombre del usuario actual
        return self.current_user
    
    def cerrar_sesion(self):
        # Dispara un evento de salida del sistema
        self.trigger_event("salida_sistema")
