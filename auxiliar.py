import pygame
from constantes import GRID_SIZE

sound_on = True
music_on = True

def load_image(file_path: str, width=GRID_SIZE, height=GRID_SIZE) -> pygame.Surface:
    """
    Carga una imagen y la acomoda a un tamaño específico.

    Parámetros:
        file_path: Ruta del archivo de imagen.
        width: Ancho deseado de la imagen (por defecto es GRID_SIZE).
        height: Altura deseada de la imagen (por defecto es GRID_SIZE).

    Devuelve:
        pygame.Surface: Superficie de la imagen cargada y acomodada.
    """
    try:
        img = pygame.image.load(file_path)
        img = pygame.transform.scale(img, (width, height))

        return img
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

def play_sound(sound, loops=0, maxtime=0, fade_ms=0) -> None:
    """
    Reproduce un sonido en el juego.

    Parámetros:
        sound: Objeto de sonido a reproducir.
        loops: Número de repeticiones del sonido (por defecto es 0).
        maxtime: Duración máxima del sonido en milisegundos (por defecto es 0).
        fade_ms: Tiempo en milisegundos para desvanecer el sonido (por defecto es 0).

    Devuelve:
        None
    """
    try:
        if sound_on:
            sound.play(loops, maxtime, fade_ms)
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

def play_music() -> None:
    """
    Reproduce la música de fondo en el juego.

    Parámetros:
        None

    Devuelve:
        None
    """
    try:
        if music_on:
            pygame.mixer.music.play(-1)
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
