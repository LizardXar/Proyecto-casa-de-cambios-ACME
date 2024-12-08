from .gestor_monedas import Gestor_Monedas
from .gestor_caja import Gestor_Caja
from .gestor_usuarios import Gestor_Usuarios

class Model:
    def __init__(self):
        self.gestor_monedas = Gestor_Monedas()
        self.gestor_caja = Gestor_Caja()
        self.gestor_usuarios = Gestor_Usuarios()