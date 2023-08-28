import tkinter as tk
import random

class GeneradorNumerosApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Generador de números")
        self.ventana.configure(bg="red") 
        
        self.numero1 = tk.IntVar()
        self.numero2 = tk.IntVar()
        self.numeroGenerado = tk.StringVar()
        
        self.etiquetaNumero1 = tk.Label(ventana, text="Número 1:", font=("Arial", 12))
        self.etiquetaNumero1.grid(row=0, column=0, padx=10, pady=5)
        
        self.etiquetaNumero2 = tk.Label(ventana, text="Número 2:", font=("Arial", 12))
        self.etiquetaNumero2.grid(row=1, column=0, padx=10, pady=5)
        
        self.etiquetaNumeroGenerado = tk.Label(ventana, text="Número Generado:", font=("Arial", 12))
        self.etiquetaNumeroGenerado.grid(row=2, column=0, padx=10, pady=5)
        
        self.spinBoxNumero1 = tk.Spinbox(ventana, from_=1, to=100, font=("Arial", 12), textvariable=self.numero1, width=15)
        self.spinBoxNumero1.grid(row=0, column=1, padx=5)
        
        self.spinBoxNumero2 = tk.Spinbox(ventana, from_=1, to=100, font=("Arial", 12), textvariable=self.numero2, width=15)
        self.spinBoxNumero2.grid(row=1, column=1, padx=5)
        
        self.lineEditNumeroGenerado = tk.Entry(ventana, textvariable=self.numeroGenerado, font=("Arial", 12), state="readonly", width=15)
        self.lineEditNumeroGenerado.grid(row=2, column=1, padx=5)
        
        self.botonGenerar = tk.Button(ventana, text="Generar", font=("Arial", 12), command=self.generar_numero)
        self.botonGenerar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def generar_numero(self):
        num1 = self.numero1.get()
        num2 = self.numero2.get()
        if num1 <= num2:
            numeroGenerado = random.randint(num1, num2)
            self.numeroGenerado.set(str(numeroGenerado))
        else:
            self.numeroGenerado.set("Error: Número 1 debe ser menor o igual a Número 2")

ventanaPrincipal = tk.Tk()
app = GeneradorNumerosApp(ventanaPrincipal)
ventanaPrincipal.mainloop()