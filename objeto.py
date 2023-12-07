import pygame

class Objeto(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.vy = 0
        self.vx = 0

    def apply_gravity(self, level) -> None:
        """
        Aplica la gravedad al objeto.

        Parámetros:
            self: Instancia de la clase que representa al objeto.
            level: Nivel actual del juego.

        Devuelve:
            None
        """
        try:
            self.vy += level.gravity
            self.vy = min(self.vy, level.terminal_velocity)
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
