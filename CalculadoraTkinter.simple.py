import tkinter as tk

class CalculadoraApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.configure(bg="blue")  # Cambiar el color de fondo a azul
        
        self.primerNumero = tk.StringVar()
        self.segundoNumero = tk.StringVar()
        self.resultado = tk.StringVar()
        
        self.etiquetaPrimerNum = tk.Label(ventana, text="Primer número:", font=("Arial", 15))
        self.etiquetaPrimerNum.grid(row=0, column=0, padx=10, pady=5)
        
        self.etiquetaSegundoNum = tk.Label(ventana, text="Segundo número:", font=("Arial", 15))
        self.etiquetaSegundoNum.grid(row=1, column=0, padx=10, pady=5)
        
        self.etiquetaResultado = tk.Label(ventana, text="Resultado:", font=("Arial", 15))
        self.etiquetaResultado.grid(row=2, column=0, padx=10, pady=5)
        
        self.lineEditPrimerNum = tk.Entry(ventana, textvariable=self.primerNumero, font=("Arial", 15), width=15)
        self.lineEditPrimerNum.grid(row=0, column=1, padx=5)
        
        self.lineEditSegundoNum = tk.Entry(ventana, textvariable=self.segundoNumero, font=("Arial", 15), width=15)
        self.lineEditSegundoNum.grid(row=1, column=1, padx=5)
        
        self.lineEditResultado = tk.Entry(ventana, textvariable=self.resultado, font=("Arial", 15), state="readonly", width=15)
        self.lineEditResultado.grid(row=2, column=1, padx=5)
        
        self.botonSumar = tk.Button(ventana, text="+", font=("Arial", 15), command=self.sumar, width=15)
        self.botonSumar.grid(row=3, column=0, padx=10, pady=5,)
        
        self.botonRestar = tk.Button(ventana, text="-", font=("Arial", 15), command=self.restar, width=15)
        self.botonRestar.grid(row=3, column=1, padx=10, pady=5, columnspan=2)
        
        self.botonMultiplicar = tk.Button(ventana, text="*", font=("Arial", 15), command=self.multiplicar, width=15)
        self.botonMultiplicar.grid(row=4, column=0, padx=10, pady=5)
        
        self.botonDividir = tk.Button(ventana, text="/", font=("Arial", 15), command=self.dividir, width=15)
        self.botonDividir.grid(row=4, column=1, padx=10, pady=5, columnspan=2)
        
        self.botonPorcentaje = tk.Button(ventana, text="%", font=("Arial", 15), command=self.porcentaje, width=15)
        self.botonPorcentaje.grid(row=5, column=0, padx=10, pady=5)
        
        self.botonClear = tk.Button(ventana, text="Limpiar", font=("Arial", 15), command=self.reset, width=15)
        self.botonClear.grid(row=5, column=1, padx=10, pady=5, columnspan=2)

    def sumar(self):
        try:
            resultado = float(self.primerNumero.get()) + float(self.segundoNumero.get())
            self.resultado.set(str(resultado))
        except:
            self.resultado.set("Error")

    def restar(self):
        try:
            resultado = float(self.primerNumero.get()) - float(self.segundoNumero.get())
            self.resultado.set(str(resultado))
        except:
            self.resultado.set("Error")
        
    def multiplicar(self):
        try:
            resultado = float(self.primerNumero.get()) * float(self.segundoNumero.get())
            self.resultado.set(str(resultado))
        except:
            self.resultado.set("Error")
            
    def dividir(self):
        try:
            resultado = float(self.primerNumero.get()) / float(self.segundoNumero.get())
            self.resultado.set(str(resultado))
        except ZeroDivisionError:
            self.resultado.set("Error: División por cero")
        except:
            self.resultado.set("Error")
    
    def porcentaje(self):
        try:
            resultado = (float(self.primerNumero.get()) / 100) * float(self.segundoNumero.get())
            self.resultado.set(str(resultado))
        except:
            self.resultado.set("Error")

    def reset(self):
        self.primerNumero.set("")
        self.segundoNumero.set("")
        self.resultado.set("")

ventanaPrincipal = tk.Tk()
app = CalculadoraApp(ventanaPrincipal)
ventanaPrincipal.mainloop()