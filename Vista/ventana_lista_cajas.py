from tkinter import Frame, Label, Button, Listbox, END

class ListViewCajas(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Lista de Cajas")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.listaCajas = Listbox(self)
        self.listaCajas.grid(row=1, column=0, padx=(0, 30), sticky="e")

        self.ver_saldo_btn = Button(self, text="Ver saldo de caja")
        self.ver_saldo_btn.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        self.return_btn = Button(self, text="Retornar menu")
        self.return_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")
 
        
    def listar_cajas(self, lista_DTO): 
        self.listaCajas.delete(0, END)
        for i, caja in lista_DTO[1].items():
            self.listaCajas.insert(i, f"{caja['codigo']} - {caja['empleado']} - {caja['estado']}")

    def obtener_cod_caja_seleccionado(self):
        # Obtener el item seleccionado en el Listbox
        seleccion = self.listaCajas.curselection()
        if seleccion:
            item = self.listaCajas.get(seleccion[0])
            cod_caja = item.split()[0]
            return cod_caja
        return None
