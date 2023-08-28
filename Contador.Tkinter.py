import tkinter as tk

class ContadorApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Contador")
        
        self.contadorActual = 0
        
        self.etiqueta_contador = tk.Label(ventana, text="Contador:", font=("Arial", 12))
        self.etiqueta_contador.grid(row=0, column=0, padx=10)
        
        self.valor_contador = tk.StringVar()
        self.valor_contador.set(str(self.contadorActual))
        
        self.lineEdit_contador = tk.Entry(ventana, textvariable=self.valor_contador, font=("Arial", 12), state="readonly", width=5)
        self.lineEdit_contador.grid(row=0, column=1, padx=5)
        
        self.boton_incrementar = tk.Button(ventana, text="Aumentar", font=("Arial", 12), command=self.incrementar_contador)
        self.boton_incrementar.grid(row=0, column=2, padx=10, pady=10)
        
        self.boton_restar = tk.Button(ventana, text="Reducir", font=("Arial", 12), command=self.restar_contador)
        self.boton_restar.grid(row=0, column=3, padx=10, pady=10)
        
        self.boton_reset = tk.Button(ventana, text="Limpiar", font=("Arial", 12), command=self.reset_contador)
        self.boton_reset.grid(row=0, column=4, padx=10, pady=10)

    def incrementar_contador(self):
        self.contadorActual += 1
        self.valor_contador.set(str(self.contadorActual))

    def restar_contador(self):
        self.contadorActual -= 1
        self.valor_contador.set(str(self.contadorActual))
        
    def reset_contador(self):
        self.contadorActual = 0
        self.valor_contador.set(str(self.contadorActual))

ventana_principal = tk.Tk()
app = ContadorApp(ventana_principal)
ventana_principal.mainloop()