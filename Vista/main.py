from .root import Root
from .ventana_home_ejecutivo import HomeViewEjecutivo
from .ventana_lista_monedas_autorizadas import ListViewActivo
from .ventana_lista_monedas_todas import ListViewTodas
from .ventana_lista_cajas import ListViewCajas
from .ventana_lista_saldo_caja import ListViewSaldoCaja
from .ventana_login import LoginView
from .ventana_home_gerente import HomeViewGerente

class View:
    
    def __init__(self):
        self.root = Root()
        self.frames = {}

        self._add_frame(HomeViewGerente, "homeGerente")
        self._add_frame(HomeViewEjecutivo, "homeEjecutivo")
        self._add_frame(ListViewActivo, "listActive")
        self._add_frame(ListViewTodas, "listAll")
        self._add_frame(ListViewCajas, "listAllCajas")
        self._add_frame(ListViewSaldoCaja, "listAllSaldos")
        self._add_frame(LoginView, "login")

    def _add_frame(self, Frame, name):
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self):
        self.root.mainloop()
        
    def stop_mainloop(self):
         self.root.destroy()