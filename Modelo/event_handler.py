class ModeloObservable:
    
    # Inicializa la clase con un diccionario para almacenar los event listeners
    def __init__(self):
        self._event_listeners = {}

    # Añade un event listener para un evento específico
    def add_event_listener(self, event, fn):
        try:
            self._event_listeners[event].append(fn)
        except KeyError:
            self._event_listeners[event] = [fn]

        return lambda: self._event_listeners[event].remove(fn)

    # Dispara un evento específico y ejecuta todos los event listeners asociados
    def trigger_event(self, event):
        if event not in self._event_listeners.keys():
            return

        for func in self._event_listeners[event]:
            func(self)
