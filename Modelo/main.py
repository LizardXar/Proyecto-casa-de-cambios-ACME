from .gestor_monedas import Gestor_Monedas
from .gestor_caja import Gestor_Caja
from .gestor_usuarios import Gestor_Usuarios
from .gestor_transaccion import Gestor_Transaccion
from .repositorio_transacciones import RepositorioTransacciones

class Modelo:
    def __init__(self):
        self.gestor_monedas = Gestor_Monedas()
        self.gestor_caja = Gestor_Caja()
        self.gestor_usuarios = Gestor_Usuarios()
        self.gestor_transaccion = Gestor_Transaccion()
        self.repositorio_transacciones = RepositorioTransacciones()