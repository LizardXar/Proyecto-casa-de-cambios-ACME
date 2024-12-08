from tkinter import Frame, Label, Button, Listbox, END

class ListViewGanancias(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Lista de Ganancias")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.listaGanancias = Listbox(self)
        self.listaGanancias.grid(row=1, column=0, padx=(0, 30), sticky="e")
        
        self.return_btn = Button(self, text="Retornar al menú")
        self.return_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    def listar_ganancias(self, lista_DTO): 
        self.listaGanancias.delete(0, END)
        for i, ganancia in lista_DTO.items():
            self.listaGanancias.insert(i, f"{ganancia['moneda']} - {ganancia['ganancia']}")
