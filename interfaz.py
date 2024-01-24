import tkinter as tk
from tkinter import Text, Scrollbar, INSERT
import analizador_lexico as AL

def analizar():
    entrada = entrada_texto.get("1.0", "end-1c")
    resultados_texto.delete("1.0", "end")
    
    AL.a.clear()  # Limpiar la lista de resultados
    AL.analisis(entrada)

    for resultado in AL.a:
        resultados_texto.insert(INSERT, resultado + "\n")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Analizador Léxico")
ventana.geometry("700x600")
ventana.config(bg='#F5D7BC')  # Color de fondo estilo pastel
ventana.resizable(False, False)

# Crear y posicionar elementos en la ventana
frame_principal = tk.Frame(ventana, width=680, height=580, bg='#FFC3A0')  # Color de fondo estilo pastel
frame_principal.place(x=10, y=10)

label_titulo = tk.Label(frame_principal, width=20, height=1, bg='#FFC3A0', fg='#6D214F', font=("Arial Black", 28), text="Analizador Léxico")
label_titulo.place(x=80, y=1)

label_entrada = tk.Label(frame_principal, width=20, height=2, text="Cadena a analizar", bg='#FFC3A0', fg='#6D214F')  # Colores pastel
label_entrada.grid(sticky="w")
label_entrada.place(x=20, y=70)

entrada_texto = Text(frame_principal, width=56, height=7, font=("Arial", 12))
entrada_texto.place(x=20, y=100)
scroll_entrada = Scrollbar(frame_principal, command=entrada_texto.yview, bg='#C39BD3')  # Color de fondo estilo pastel
scroll_entrada.grid(sticky="nsew")
scroll_entrada.place(in_=entrada_texto, relx=1, relheight=1, bordermode="outside")
entrada_texto.config(yscrollcommand=scroll_entrada.set)

label_resultado = tk.Label(frame_principal, width=10, height=1, text="Resultado: ", font=("Arial", 12), bg='#FFC3A0', fg='#6D214F')  # Colores pastel
label_resultado.grid(sticky="e")
label_resultado.place(x=20, y=270)

resultados_texto = Text(frame_principal, width=56, height=9, font=("Arial", 12))
resultados_texto.place(x=20, y=300)
scroll_resultados = Scrollbar(frame_principal, command=resultados_texto.yview, bg='#C39BD3')  # Color de fondo estilo pastel
scroll_resultados.grid(sticky="nsew")
scroll_resultados.place(in_=resultados_texto, relx=1, relheight=1, bordermode="outside")
resultados_texto.config(yscrollcommand=scroll_resultados.set)
resultados_texto.config(state="normal")

boton_analizar = tk.Button(frame_principal, text="Analizar", font=("Arial", 12), bg='#6D214F', fg='#F5D7BC', command=analizar)  # Colores pastel
boton_analizar.place(x=280, y=530, width=100, height=30)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
