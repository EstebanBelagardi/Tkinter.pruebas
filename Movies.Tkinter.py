import tkinter as tk

class PeliculasApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Películas")
        
        self.peliculaActual = tk.StringVar()
        self.listaPeliculas = []
        
        self.etiquetaIngresar = tk.Label(ventana, text="Escribe el título de una película:", font=("Arial", 12))
        self.etiquetaIngresar.grid(row=0, column=0, padx=10)
        
        self.etiquetaPeliculas = tk.Label(ventana, text="Películas", font=("Arial", 12))
        self.etiquetaPeliculas.grid(row=0, column=1, padx=10, pady=5)
        
        self.lineEditPelicula = tk.Entry(ventana, textvariable=self.peliculaActual, font=("Arial", 12), width=20)
        self.lineEditPelicula.grid(row=1, column=0, padx=2)
        
        self.listWidgetPeliculas = tk.Listbox(ventana, font=("Arial", 12), width=30)
        self.listWidgetPeliculas.grid(row=1, column=1, padx=5)
        
        self.botonAñadir = tk.Button(ventana, text="Añadir", font=("Arial", 12), command=self.añadirPelicula)
        self.botonAñadir.grid(row=3, column=0, padx=10, pady=5)
        
    def añadirPelicula(self):
        pelicula = self.peliculaActual.get()
        if pelicula:
            self.listaPeliculas.append(pelicula)
            self.actualizarListWidget()

    def actualizarListWidget(self):
        self.listWidgetPeliculas.delete(0, tk.END)
        for pelicula in self.listaPeliculas:
            self.listWidgetPeliculas.insert(tk.END, pelicula)

ventanaPrincipal = tk.Tk()
app = PeliculasApp(ventanaPrincipal)
ventanaPrincipal.mainloop()