from .monedas_DTO import Monedas_DTO

class Monedas_DAO:

    def __init__(self):
        self.lista_monedas = {
            1: Monedas_DTO(1, "USD", 1.0, "Activo"),
            2: Monedas_DTO(2, "EUR", 0.85, "Activo"),
            3: Monedas_DTO(3, "JPY", 110.5, "Inactivo")
        }

    def leer_monedas(self):
        lista_DTO = self.lista_monedas
        return lista_DTO
