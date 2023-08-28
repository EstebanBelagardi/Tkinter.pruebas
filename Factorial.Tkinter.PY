import tkinter as tk
import math

class FactorialApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Factorial")
        
        self.n = 1
        self.factorialActual = 1
        
        self.etiqueta_n = tk.Label(ventana, text="n:", font=("Arial", 15))
        self.etiqueta_n.grid(row=0, column=0, padx=10)
        
        self.etiquetaFactorial = tk.Label(ventana, text="Factorial (n):", font=("Arial", 15))
        self.etiquetaFactorial.grid(row=1, column=0, padx=10, pady=5)
        
        self.valor_n = tk.StringVar()
        self.valor_n.set(str(self.n))
        
        self.lineEdit_n = tk.Entry(ventana, textvariable=self.valor_n, font=("Arial", 15), state="readonly", width=5)
        self.lineEdit_n.grid(row=0, column=1, padx=5)
        
        self.valorFactorial = tk.StringVar()
        self.valorFactorial.set(str(self.factorialActual))
        
        self.lineEditFactorial = tk.Entry(ventana, textvariable=self.valorFactorial, font=("Arial", 15), state="readonly", width=15)
        self.lineEditFactorial.grid(row=1, column=1, padx=5, pady=5)
        
        self.botonSiguiente = tk.Button(ventana, text="Siguiente", font=("Arial", 15), command=self.calcularSiguiente)
        self.botonSiguiente.grid(row=2, column=0, columnspan=2, pady=10)

    def calcularSiguiente(self):
        self.n += 1
        self.factorialActual = math.factorial(self.n)
        
        self.valor_n.set(str(self.n))
        self.valorFactorial.set(str(self.factorialActual))

ventanaPrincipal = tk.Tk()
app = FactorialApp(ventanaPrincipal)
ventanaPrincipal.mainloop()