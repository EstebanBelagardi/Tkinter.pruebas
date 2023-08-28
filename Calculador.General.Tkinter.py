import tkinter as tk

def click_numero(numero):
    entrada.insert(tk.END, numero)

def click_operador(operador):
    entrada.insert(tk.END, operador)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def borrar():
    entrada.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Calculadora Simple")

entrada = tk.Entry(ventana, font=("Arial", 20), borderwidth=5)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

tk.Button(ventana, text="7", command=lambda: click_numero("7"),
          font=("Arial", 15), padx=20, pady=20, borderwidth=3).grid(row=1, column=0)
tk.Button(ventana, text="8", command=lambda: click_numero("8"),
          font=("Arial", 15), padx=20, pady=20, borderwidth=3).grid(row=1, column=1)
tk.Button(ventana, text="9", command=lambda: click_numero("9"),
          font=("Arial", 15), padx=20, pady=20, borderwidth=3).grid(row=1, column=2)
tk.Button(ventana, text="/", command=lambda: click_operador("/"),
          font=("Arial", 15), padx=20, pady=20, borderwidth=3).grid(row=1, column=3)

tk.Button(ventana, text="4", command=lambda: click_numero("4"),
          font=("Arial", 15), padx=20, pady=20, borderwidth=3).grid(row=2, column=0)
tk.Button(ventana, text="5", command=lambda: click_numero("5"),
          font=("Arial", 15), padx=20, pady=20, borderwidth=3).grid(row=2, column=1)
tk.Button(ventana, text="6", command=lambda: click_numero("6"),
          font=("Arial", 15), padx=20, pady=20, borderwidth=3).grid(row=2, column=2)
tk.Button(ventana, text="*", command=lambda: click_operador("*"),
          font=("Arial", 15), padx=20, pady=20, borderwidth=3).grid(row=2, column=3)

tk.Button(ventana, text="1", command=lambda: click_numero("1"),
          font=("Arial", 15), padx=20, pady=20, borderwidth=3).grid(row=3, column=0)
tk.Button(ventana, text="2", command=lambda: click_numero("2"),
          font=("Arial", 15), padx=20, pady=20, borderwidth=3).grid(row=3, column=1)
tk.Button(ventana, text="3", command=lambda: click_numero("3"),
          font=("Arial", 15), padx=20, pady=20, borderwidth=3).grid(row=3, column=2)
tk.Button(ventana, text="-", command=lambda: click_operador("-"),
          font=("Arial", 15), padx=20, pady=20, borderwidth=3).grid(row=3, column=3)

tk.Button(ventana, text="0", command=lambda: click_numero("0"),
          font=("Arial", 15), padx=20, pady=20, borderwidth=3).grid(row=4, column=1)
tk.Button(ventana, text="C", command=borrar,
          font=("Arial", 15), padx=20, pady=20, borderwidth=3).grid(row=4, column=0)
tk.Button(ventana, text="=", command=calcular,
          font=("Arial", 15), padx=20, pady=20, borderwidth=3).grid(row=4, column=2)
tk.Button(ventana, text="+", command=lambda: click_operador("+"),
          font=("Arial", 15), padx=20, pady=20, borderwidth=3).grid(row=4, column=3)

ventana.mainloop()