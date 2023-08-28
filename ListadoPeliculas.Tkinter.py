import tkinter as tk

class PeliculasApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Listado de Películas")
        self.ventana.configure(bg="red")  
        
        self.pelicula_actual = tk.StringVar()
        self.lista_peliculas = []
        
        self.etiqueta_ingresar = tk.Label(ventana, text="¿Qué película desea agregar al listado?:", font=("Arial", 15), bg="red", fg="white")
        self.etiqueta_ingresar.grid(row=0, column=0, padx=12, pady=30)
        
        self.etiqueta_peliculas = tk.Label(ventana, text="Agenda de Películas por ver", font=("Arial", 12), bg="red", fg="white")
        self.etiqueta_peliculas.grid(row=0, column=1, padx=30, pady=5)
        
        self.lineEdit_pelicula = tk.Entry(ventana, textvariable=self.pelicula_actual, font=("Arial", 12), width=20)
        self.lineEdit_pelicula.grid(row=1, column=0, padx=2)
        
        self.listWidget_peliculas = tk.Listbox(ventana, font=("Arial", 12), width=30)
        self.listWidget_peliculas.grid(row=1, column=1, padx=30)
        
        self.boton_anadir = tk.Button(ventana, text="Añadir", font=("Arial", 12), command=self.añadir_pelicula, bg="white", fg="red")
        self.boton_anadir.grid(row=3, column=0, padx=10, pady=30)

    def añadir_pelicula(self):
        pelicula = self.pelicula_actual.get()
        if pelicula:
            self.lista_peliculas.append(pelicula)
            self.actualizar_list_widget()

    def actualizar_list_widget(self):
        self.listWidget_peliculas.delete(0, tk.END)
        for pelicula in self.lista_peliculas:
            self.listWidget_peliculas.insert(tk.END, pelicula)

def main():
    ventana_principal = tk.Tk()
    ventana_principal.configure(bg="red")  # Color de fondo rojo
    app = PeliculasApp(ventana_principal)
    ventana_principal.mainloop()

if __name__ == "__main__":
    main()
