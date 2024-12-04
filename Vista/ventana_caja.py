from tkinter import Frame, Label, Button, Listbox, END

class ListViewSaldoCaja(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text=f"Saldo de la caja ")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.listaSaldo = Listbox(self)
        self.listaSaldo.grid(row=1, column=0, padx=(0, 30), sticky="e")
        
        self.return_btn = Button(self, text="Retornar")
        self.return_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")
 
        
    def listar_saldo(self, lista_DTO): 
        self.listaSaldo.delete(0, END)
        for i, saldo in lista_DTO[1].items():
            self.listaSaldo.insert(i, f"{saldo['moneda']} - {saldo['saldo']}")