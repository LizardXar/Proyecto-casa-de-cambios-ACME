from tkinter import Frame, Label, Button, Listbox, END

class ListViewActivo(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Lista de Monedas Autorizadas")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.listaMonedas = Listbox(self)
        self.listaMonedas.grid(row=1, column=0, padx=(0, 30), sticky="e")
        
        self.return_btn = Button(self, text="Retornar menu")
        self.return_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")
 
        
    def listar_monedas_autorizadas(self, lista_DTO): 
        self.listaMonedas.delete(0, END)
        for i, moneda in lista_DTO[1].items():
            self.listaMonedas.insert(i, f"{moneda['codigo']} - {moneda['nombre']} - {moneda['tipo']}")


