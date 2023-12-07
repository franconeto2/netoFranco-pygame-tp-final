import pygame
import random
from enemigo import Enemy
from bala import Bullet
from auxiliar import load_image, play_sound
from constantes import FPS

conejo_img1 = load_image("C:\\Users\\franc\\Downloads\\PIXEL ADVENTURE\\Recursos\\Enemies\\Bunny\\Run (34x44)2.png")
conejo_img2 = load_image("C:\\Users\\franc\\Downloads\\PIXEL ADVENTURE\\Recursos\\Enemies\\Bunny\\Idle (34x44)2.png")
conejo_images = [conejo_img1, conejo_img2]

hurt_sound = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Punch Sound Effect  Gaming SFX.mp3")
energy_sound =  pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Y2meta.app - Power-Up - Sound Effect (HD) (128 kbps).mp3")
enemigo_muerto = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Y2meta.app - CS_GO Zeus Sound (128 kbps).mp3")

class Conejo(Enemy):
    def __init__(self, x, y, images):
        super().__init__(x, y, images)

        self._start_x = x
        self._start_y = y
        if random.random() >= 0.5:
            self.start_vx = -2
        else:
            self.start_vx = 2
        self._start_vy = 0

        self.vx = self.start_vx
        self.vy = self._start_vy
        self._health = 4

    @property
    def start_x(self):
        return self._start_x

    @start_x.setter
    def start_x(self, valor):
        self._start_x = valor

    @property
    def start_y(self):
        return self._start_y

    @start_y.setter
    def start_y(self, valor):
        self._start_y = valor

    @property
    def start_vy(self):
        return self._start_vy

    @start_vy.setter
    def start_vy(self, valor):
        self._start_vy = valor

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, valor):
        self._health = valor

    def take_damage(self, damage: int, player) -> None:
        """
        Gestiona el daño recibido por el conejo.

        Parámetros:
            self: Instancia de la clase que representa al conejo
            damage: Daño recibido.
            player: Instancia de la clase que representa al jugador.

        Devuelve:
            None
        """
        try:
            self._health -= damage
            play_sound(hurt_sound)
            self.invincibility = int(0.75 * FPS)
            if self._health <= 0:
                play_sound(enemigo_muerto)
                self.kill()
                player.score += 2
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def shoot(self, level) -> None:
        """
        Hace que el conejo dispare.

        Parámetros:
            self: Instancia de la clase que representa al conejo.
            level: Nivel actual del juego.

        Devuelve:
            None
        """
        try:
            play_sound(energy_sound)
            direction = 1 if self.facing_right else -1
            bullet_img = load_image("C:\\Users\\franc\\Downloads\\faltano\\assets\\coins\\Bola_de_almas.png")
            bullet = Bullet(self.rect.centerx, self.rect.centery, direction, 14, bullet_img, self)
            level.bullets.add(bullet)
            level.active_sprites.add(bullet)
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def update(self, level, hero) -> None:
        """
        Actualiza el estado del conejo.

        Parámetros:
            self: Instancia de la clase que representa al conejo.
            level: Nivel actual del juego.
            hero: Instancia de la clase que representa al jugador.

        Devuelve:
            None
        """
        try:
            super().update(level, hero)
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
