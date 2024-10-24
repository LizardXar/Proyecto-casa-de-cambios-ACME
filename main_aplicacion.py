from Modelo.main import Model
from Vista.main import View
from Controlador.main import Controller

def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start()

if __name__ == "__main__":
    main()