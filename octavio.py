import pygame
import random
from enemigo import Enemy
from bala import Bullet
from auxiliar import load_image, play_sound
from constantes import FPS

octavio_img = load_image("C:\\Users\\franc\\Downloads\\faltano\\assets\\enemies\\octavio.png")
octavio_image = [octavio_img]

hurt_sound = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Punch Sound Effect  Gaming SFX.mp3")
computer_sound = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Y2meta.app - Windows XP Error Sound effect (128 kbps).mp3")
enemigo_muerto = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Y2meta.app - CS_GO Zeus Sound (128 kbps).mp3")

class Octavio(Enemy):
    def __init__(self, x, y, images):
        super().__init__(x, y, images)

        self.start_x = x
        self.start_y = y
        self.start_vx = -1
        self.start_vy = 0

        self.vx = self.start_vx
        self.vy = self.start_vy
        self.health = 100

    def take_damage(self, damage: int, player) -> None:
        """
        Gestiona el daño recibido por Octavio.

        Parámetros:
            self: Instancia de la clase que representa a Octavio.
            damage: Daño recibido.
            player: Instancia de la clase que representa al jugador.

        Devuelve:
            None
        """
        try:
            self.health -= damage
            play_sound(hurt_sound)
            self.invincibility = int(0.75 * FPS)
            if self.health <= 0:
                play_sound(enemigo_muerto)
                self.kill()
                player.score += 2
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    jump = lambda self: setattr(self, 'vy', -15)

    change_acceleration = lambda self: setattr(self, 'vy', 15)

    def shoot(self, level) -> None:
        """
        Hace que Octavio dispare.

        Parámetros:
            self: Instancia de la clase que representa a Octavio.
            level: Nivel actual del juego.

        Devuelve:
            None
        """
        try:
            play_sound(computer_sound)
            direction = 1 if self.facing_right else -1
            bullet_img = load_image("C:\\Users\\franc\\Downloads\\faltano\\assets\\coins\\monitor-black-log.png")
            bullet = Bullet(self.rect.centerx, self.rect.centery, direction, 14, bullet_img, self)
            level.bullets.add(bullet)
            level.active_sprites.add(bullet)
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def update(self, level, player) -> None:
        """
        Actualiza el estado de Octavio.

        Parámetros:
            self: Instancia de la clase que representa a Octavio.
            level: Nivel actual del juego.
            player: Instancia de la clase que representa al jugador.

        Devuelve:
            None
        """
        try:
            super().update(level, player)

            if random.random() < 0.1:
                self.jump()
            if random.random() < 0.1:
                self.change_acceleration()
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
