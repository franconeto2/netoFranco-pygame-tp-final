import tkinter as tk
import auxiliar

def manejar_efectos_sonido() -> None:
    """
    Cambia el estado de los efectos de sonido.

    Parámetros:
        None

    Devuelve:
        None
    """
    try:
        auxiliar.sound_on = not auxiliar.sound_on
        nuevo_estado = "Encendido" if auxiliar.sound_on else "Apagado"
        efectos_sonido_btn.config(text=nuevo_estado)
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

def manejar_musica_fondo() -> None:
    """
    Cambia el estado de la música de fondo.

    Parámetros:
        None

    Devuelve:
        None
    """
    try:
        auxiliar.music_on = not auxiliar.music_on
        nuevo_estado = "Encendido" if auxiliar.music_on else "Apagado"
        musica_fondo_btn.config(text=nuevo_estado)
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

ventana = tk.Tk()
ventana.title("Configuración de Sonido")

efectos_sonido_lbl = tk.Label(ventana, text="Efectos de Sonido:")
efectos_sonido_lbl.pack()
efectos_sonido_btn = tk.Button(ventana, text="Encendido", command=manejar_efectos_sonido)
efectos_sonido_btn.pack()

musica_fondo_lbl = tk.Label(ventana, text="Música de Fondo:")
musica_fondo_lbl.pack()
musica_fondo_btn = tk.Button(ventana, text="Encendido", command=manejar_musica_fondo)
musica_fondo_btn.pack()

ventana.mainloop()
