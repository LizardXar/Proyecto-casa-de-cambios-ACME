from .root import Root
from .ventana_home_ejecutivo import VistaInicioEjecutivo
from .ventana_lista_monedas_autorizadas import VistaListaActivos
from .ventana_lista_monedas_todas import VistaListaTodas
from .ventana_lista_cajas import VistaListaCajas
from .ventana_lista_saldo_caja import VistaListaSaldoCaja
from .ventana_login import VistaLogin
from .ventana_home_gerente import VistaInicioGerente
from .ventana_lista_ganancias import VistaListaGanancias
from .ventana_monedas_trazadas import VistaListaMonedasTrazadas
from .ventana_home_ejecutivo import VistaInicioEjecutivo
from .ventana_home_cajero import VistaInicioCajero
from .ventana_realizar_transaccion import VistaTransaccion
from .ventana_modificar_tipo_de_cambios import VistaTipoDeCambio
from .ventana_registrar_disponibilidad import VistaRegistrarDisponibilidadPesos


class Vista:
    
    def __init__(self):
        self.root = Root()
        self.frames = {}

        self._add_frame(VistaInicioGerente, "inicioGerente")
        self._add_frame(VistaInicioEjecutivo, "inicioEjecutivo")
        self._add_frame(VistaListaActivos, "listaActivos")
        self._add_frame(VistaListaTodas, "listaTodos")
        self._add_frame(VistaListaCajas, "listaTodasCajas")
        self._add_frame(VistaListaSaldoCaja, "listaTodosSaldos")
        self._add_frame(VistaListaGanancias, "listaGanancias")
        self._add_frame(VistaLogin, "login")
        self._add_frame(VistaListaMonedasTrazadas, "listaMonedasTrazadas")
        self._add_frame(VistaInicioCajero, "inicioCajero")
        self._add_frame(VistaTransaccion, "realizarTransaccion")
        self._add_frame(VistaTipoDeCambio, "modificarTipoCambio")
        self._add_frame(VistaRegistrarDisponibilidadPesos, "registrarDisponibilidadPesos")
        
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
