import pygame
import random
from objeto import Objeto
from bala import Bullet
from auxiliar import load_image, play_sound
from constantes import FPS, WIDTH

pygame.mixer.pre_init()
pygame.init()

hurt_sound = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Punch Sound Effect  Gaming SFX.mp3")

class Enemy(Objeto):
    def __init__(self, x, y, images):
        super().__init__(x, y, images[0])

        self.images_left = images
        self.images_right = [pygame.transform.flip(img, 1, 0) for img in images]
        self.current_images = self.images_left
        self.image_index = 0
        self.steps = 0
        self._facing_right = False

    @property
    def facing_right(self):
        return self._facing_right

    @facing_right.setter
    def facing_right(self, valor):
        self._facing_right = valor

    def shoot(self, level) -> None:
        """
        Hace que el enemigo dispare una bala.

        Parámetros:
            self: Instancia de la clase que representa al enemigo.
            level: Nivel actual del juego.

        Devuelve:
            None
        """
        try:
            direction = 1 if self._facing_right else -1
            bullet_img = load_image("C:\\Users\\franc\\Downloads\\faltano\\assets\\coins\\Bola_de_almas.png")
            bullet = Bullet(self.rect.centerx, self.rect.centery, direction, 10, bullet_img, self)
            level.bullets.add(bullet)
            level.active_sprites.add(bullet)
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def reverse(self) -> None:
        """
        Invierte la dirección del enemigo y actualiza su imagen correspondiente.

        Parámetros:
            self: Instancia de la clase que representa al enemigo.

        Devuelve:
            None
        """
        try:
            self.vx *= -1

            if self.vx < 0:
                self.current_images = self.images_left
                self._facing_right = False
            else:
                self.current_images = self.images_right
                self._facing_right = True

            self.image = self.current_images[self.image_index]
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def check_world_boundaries(self, level) -> None:
        """
        Verifica si el enemigo ha alcanzado los límites del mundo del nivel y realiza acciones en consecuencia.

        Parámetros:
            self: Instancia de la clase que representa al enemigo.
            level: Nivel actual del juego.

        Devuelve:
            None
        """
        try:
            if self.rect.left < 0:
                self.rect.left = 0
                self.reverse()
            elif self.rect.right > level.width:
                self.rect.right = level.width
                self.reverse()
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def move_and_process_blocks(self, blocks: pygame.sprite.Group) -> None:
        """
        Mueve al enemigo y procesa las colisiones con los bloques del juego.

        Parámetros:
            self: Instancia de la clase que representa al enemigo.
            blocks: Grupo de sprites que representa los bloques del juego.

        Devuelve:
            None
        """
        try:
            self.rect.x += self.vx
            if self.vx < 0:
                self.current_images = self.images_left
                self._facing_right = False
            else:
                self.current_images = self.images_right
                self._facing_right = True

            self.image = self.current_images[self.image_index]
            hit_list = pygame.sprite.spritecollide(self, blocks, False)

            for block in hit_list:
                if self.vx > 0:
                    self.rect.right = block.rect.left
                    self.reverse()
                elif self.vx < 0:
                    self.rect.left = block.rect.right
                    self.reverse()

            self.rect.y += self.vy
            hit_list = pygame.sprite.spritecollide(self, blocks, False)

            for block in hit_list:
                if self.vy > 0:
                    self.rect.bottom = block.rect.top
                    self.vy = 0
                elif self.vy < 0:
                    self.rect.top = block.rect.bottom
                    self.vy = 0
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def set_images(self) -> None:
        """
        Establece las imágenes del enemigo.

        Parámetros:
            self: Instancia de la clase que representa al enemigo.

        Devuelve:
            None
        """
        try:
            if self.steps == 0:
                self.image = self.current_images[self.image_index]
                self.image_index = (self.image_index + 1) % len(self.current_images)

            self.steps = (self.steps + 1) % 20
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    is_near = lambda self, hero: abs(self.rect.x - hero.rect.x) < 2 * WIDTH

    def update(self, level, hero) -> None:
        """
        Actualiza el estado del enemigo.

        Parámetros:
            self: Instancia de la clase que representa al enemigo.
            level: Nivel actual del juego.
            hero: Instancia de la clase que representa al jugador.

        Devuelve:
            None
        """
        try:
            self.apply_gravity(level)
            self.move_and_process_blocks(level.blocks)
            self.check_world_boundaries(level)
            self.set_images()
            if random.random() < 0.01:
                self.shoot(level)
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def reset(self) -> None:
        """
        Restablece los valores iniciales del enemigo.

        Parámetros:
            self: Instancia de la clase que representa al enemigo.

        Devuelve:
            None
        """
        try:
            self.rect.x = self.start_x
            self.rect.y = self.start_y
            self.vx = self.start_vx
            self.vy = self.start_vy
            self.current_images = self.images_left
            self.image = self.current_images[0]
            self.steps = 0
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
