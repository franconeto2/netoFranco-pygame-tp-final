import tkinter as tk

nivel_seleccionado = None

def iniciar_nivel(nivel) -> None:
    """
    Inicia un nivel específico en el juego.

    Parámetros:
        nivel: Nivel que se desea iniciar.

    Devuelve:
        None
    """
    try:
        global nivel_seleccionado
        nivel_seleccionado = nivel
        ventana.quit()
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

ventana = tk.Tk()
ventana.title("Selección de Nivel")

iniciar_nivel_1 = lambda: iniciar_nivel(1)

iniciar_nivel_2 = lambda: iniciar_nivel(2)

iniciar_nivel_3 = lambda: iniciar_nivel(3)

nivel1_btn = tk.Button(ventana, text="Nivel 1", command=iniciar_nivel_1)
nivel1_btn.pack()

nivel2_btn = tk.Button(ventana, text="Nivel 2", command=iniciar_nivel_2)
nivel2_btn.pack()

nivel3_btn = tk.Button(ventana, text="Nivel 3", command=iniciar_nivel_3)
nivel3_btn.pack()

ventana.mainloop()
