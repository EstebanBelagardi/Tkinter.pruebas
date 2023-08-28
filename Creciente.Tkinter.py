import tkinter as tk

class ContCrecienteApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("ContCreciente")
        self.ventana.configure(bg="red") 
        
        self.contador = 0
        
        self.etiqueta = tk.Label(ventana, text="Contador", font=("Arial", 12))
        self.etiqueta.grid(row=0, column=0, padx=10)
        
        self.valorContador = tk.StringVar()
        self.valorContador.set(str(self.contador))
        
        self.lineEdit = tk.Entry(ventana, textvariable=self.valorContador, font=("Arial", 12), state="readonly", width=5)
        self.lineEdit.grid(row=0, column=1, padx=5)
        
        self.botonMas = tk.Button(ventana, text="+", font=("Arial", 12), command=self.incrementarContador, width=3)
        self.botonMas.grid(row=0, column=2, padx=10)

    def incrementarContador(self):
        self.contador += 1
        self.valorContador.set(str(self.contador))

ventanaPrincipal = tk.Tk()
app = ContCrecienteApp(ventanaPrincipal)
ventanaPrincipal.mainloop()