from .root import Root
from .ventana_home import HomeView
from .ventana_lista_monedas_autorizadas import ListViewActivo
from .ventana_lista_monedas_todas import ListViewTodas

class View:
    
    def __init__(self):
        self.root = Root()
        self.frames = {}

        self._add_frame(HomeView, "home")
        self._add_frame(ListViewActivo, "listActive")
        self._add_frame(ListViewTodas, "listAll")

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