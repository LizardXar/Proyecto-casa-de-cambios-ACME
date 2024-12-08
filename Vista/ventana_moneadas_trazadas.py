from tkinter import Frame, Label, Button, Listbox, END

class ListViewMonedasTrazadas(Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Lista de Monedas Más Trazadas", font=("Arial", 14))
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.listaMonedasTrazadas = Listbox(self, width=50, height=10)
        self.listaMonedasTrazadas.grid(row=1, column=0, padx=(0, 30), pady=10, sticky="e")

        # Botones
        self.return_btn = Button(self, text="Retornar menú")
        self.return_btn.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    def listar_monedas(self, lista_monedas):
        self.listaMonedasTrazadas.delete(0, END)
        for i, moneda in lista_monedas[1].items():
            self.listaMonedasTrazadas.insert(END, f" {moneda['moneda']} - {moneda['trazada']}")    

   