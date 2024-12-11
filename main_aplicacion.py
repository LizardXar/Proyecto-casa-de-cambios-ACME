from Modelo.main import Modelo
from Vista.main import Vista
from Controlador.main import Controlador

def main():
    modelo = Modelo()
    vista = Vista()
    controlador = Controlador(modelo, vista)
    controlador.start()

if __name__ == "__main__":
    main()
