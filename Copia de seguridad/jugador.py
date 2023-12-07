import pygame
from objeto import Objeto
from bala import Bullet
from constantes import FPS
from auxiliar import load_image, play_sound

hero_walk1 = load_image("C:\\Users\\franc\\Downloads\\PIXEL ADVENTURE\\Recursos\\Main Characters\\Ninja Frog\\Run (32x32)2.png")
hero_walk2 = load_image("C:\\Users\\franc\\Downloads\\PIXEL ADVENTURE\\Recursos\\Main Characters\\Ninja Frog\\Run (32x32)3.png")
hero_jump = load_image("C:\\Users\\franc\\Downloads\\PIXEL ADVENTURE\\Recursos\\Main Characters\\Ninja Frog\\Jump (32x32)2.png")
hero_idle = load_image("C:\\Users\\franc\\Downloads\\PIXEL ADVENTURE\\Recursos\\Main Characters\\Ninja Frog\\Idle (32x32)2.png")
hero_images = {"run": [hero_walk1, hero_walk2],
               "jump": hero_jump,
               "idle": hero_idle}

jump_sound = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Mario Jump Sound Effect.mp3")
coin_sound = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Cash Register  Sound EffectHD.mp3")
sol_sound = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\TWINKLE Sound Effect.mp3")
trap_sound = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Crunch sound effect  No copyright.mp3")
hurt_sound = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Punch Sound Effect  Gaming SFX.mp3")
die_sound = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Fortnite Death Sound Effect No copyright.mp3")
fireball_sound = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Fire Whoosh Sound Effect Commercial.mp3")
computer_sound = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Y2meta.app - Windows XP Error Sound effect (128 kbps).mp3")
levelup_sound = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Milei Zurdos hijos de puta tiemblen la libertad avanza.mp3")
gameover_sound = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Lose sound effects.mp3")
juego_ganado_sound = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Celebracion en BUENOS AIRES ARGENTINA CAMPEN  Celebration in BUENOS AIRES ARGENTINA CHAMPION.mp3")

class Character(Objeto):

    def __init__(self, images):
        super().__init__(0, 0, images['idle'])

        self.image_idle_right = images['idle']
        self.image_idle_left = pygame.transform.flip(self.image_idle_right, 1, 0)
        self.images_run_right = images['run']
        self.images_run_left = [pygame.transform.flip(img, 1, 0) for img in self.images_run_right]
        self.image_jump_right = images['jump']
        self.image_jump_left = pygame.transform.flip(self.image_jump_right, 1, 0)

        self.running_images = self.images_run_right
        self.image_index = 0
        self.steps = 0

        self._speed = 5
        self._jump_power = 20

        self.vx = 0
        self.vy = 0
        self._facing_right = True
        self.on_ground = True

        self.score = 0
        self._lives = 3
        self._hearts = 3
        self._max_hearts = 3
        self.invincibility = 0

        self.nivel_actual = 1

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, valor):
        self._speed = valor

    @property
    def jump_power(self):
        return self._jump_power

    @jump_power.setter
    def jump_power(self, valor):
        self._jump_power = valor

    @property
    def facing_right(self):
        return self._facing_right

    @facing_right.setter
    def facing_right(self, valor):
        self._facing_right = valor

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, valor):
        self._lives = valor

    @property
    def hearts(self):
        return self._hearts

    @hearts.setter
    def hearts(self, valor):
        self._hearts = valor

    @property
    def max_hearts(self):
        return self._max_hearts

    @max_hearts.setter
    def max_hearts(self, valor):
        self._max_hearts = valor

    def shoot(self, bullets: pygame.sprite.Group, level) -> None:
        """
        Dispara una bala desde el personaje del juego.

        Parámetros:
            self: Instancia de la clase que representa al jugador.
            bullets: Grupo de balas en el juego representado por un objeto pygame.sprite.Group.
            level: Nivel actual del juego.

        Devuelve:
            None
        """
        try:
            play_sound(fireball_sound)
            direction = 1 if self._facing_right else -1
            bullet_img = load_image("C:\\Users\\franc\\Downloads\\faltano\\assets\\coins\\ball-of-fire-glowing-magma-sphere-fireball-large-sphere-of-red-energy-fantasy-game-spell-icon-generative-ai-png.png")
            bullet = Bullet(self.rect.centerx, self.rect.centery, direction, 10, bullet_img, self)
            level.bullets.add(bullet)
            level.active_sprites.add(bullet)
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def take_damage(self) -> None:
        """
        Hace que el jugador sufra daño.

        Parámetros:
            self: Instancia de la clase que representa al jugador.

        Devuelve:
            None
        """
        try:
            play_sound(hurt_sound)
            self._hearts -= 1
            self.invincibility = int(0.75 * FPS)
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def move_left(self) -> None:
        """
        Mueve al jugador hacia la izquierda.

        Parámetros:
            self: Instancia de la clase que representa al jugador.

        Devuelve:
            None
        """
        try:
            self.vx = -self._speed
            self._facing_right = False
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def move_right(self) -> None:
        """
        Mueve al jugador hacia la derecha.

        Parámetros:
            self: Instancia de la clase que representa al jugador.

        Devuelve:
            None
        """
        try:
            self.vx = self._speed
            self._facing_right = True
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    stop = lambda self: setattr(self, 'vx', 0)

    def jump(self, blocks: pygame.sprite.Group) -> None:
        """
        Hace que el jugador realice un salto.

        Parámetros:
            self: Instancia de la clase que representa al jugador.
            blocks: Grupo de bloques en el juego representado por un objeto pygame.sprite.Group.

        Devuelve:
            None
        """
        try:
            self.rect.y += 1

            hit_list = pygame.sprite.spritecollide(self, blocks, False)

            if len(hit_list) > 0:
                self.vy = -1 * self._jump_power
                play_sound(jump_sound)
                self.rect.y -= 1
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def check_world_boundaries(self, level) -> None:
        """
        Verifica los límites del mundo para el jugador y ajusta su posición si es necesario.

        Parámetros:
            self: Instancia de la clase que representa al jugador.
            level: Nivel actual del juego.

        Devuelve:
            None
        """
        try:
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > level.width:
                self.rect.right = level.width
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def move_and_process_blocks(self, blocks: pygame.sprite.Group) -> None:
        """
        Mueve al jugador y procesa las colisiones con los bloques en el juego.

        Parámetros:
            self: Instancia de la clase que representa al jugador.
            blocks: Grupo de bloques en el juego representado por un objeto pygame.sprite.Group.

        Devuelve:
            None
        """
        try:
            self.rect.x += self.vx
            hit_list = pygame.sprite.spritecollide(self, blocks, False)

            for block in hit_list:
                if self.vx > 0:
                    self.rect.right = block.rect.left
                    self.vx = 0
                elif self.vx < 0:
                    self.rect.left = block.rect.right
                    self.vx = 0

            self.on_ground = False
            self.rect.y += self.vy + 1
            hit_list = pygame.sprite.spritecollide(self, blocks, False)

            for block in hit_list:
                if self.vy > 0:
                    self.rect.bottom = block.rect.top
                    self.vy = 0
                    self.on_ground = True
                elif self.vy < 0:
                    self.rect.top = block.rect.bottom
                    self.vy = 0
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def process_coins(self, coins: pygame.sprite.Group) -> None:
        """
        Procesa las colisiones entre el jugador y las monedas, actualizando la puntuación.

        Parámetros:
            self: Instancia de la clase que representa al jugador.
            coins: Grupo de monedas en el juego representado por un objeto pygame.sprite.Group.

        Devuelve:
            None
        """
        try:
            hit_list = pygame.sprite.spritecollide(self, coins, True)

            for coin in hit_list:
                play_sound(coin_sound)
                self.score += coin.value
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def process_soles(self, soles: pygame.sprite.Group) -> None:
        """
        Procesa las colisiones entre el jugador y los soles, actualizando la puntuación.

        Parámetros:
            self: Instancia de la clase que representa al personaje del juego.
            soles: Grupo de soles en el juego representado por un objeto pygame.sprite.Group.

        Devuelve:
            None
        """
        try:
            hit_list = pygame.sprite.spritecollide(self, soles, True)

            for sol in hit_list:
                play_sound(sol_sound)
                self.score += sol.value
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def process_enemies(self, enemies: pygame.sprite.Group) -> None:
        """
        Procesa las colisiones entre el jugador y los enemigos, disminuyendo los corazones del jugador si no se encuentra en un estado de invencibilidad.

        Parámetros:
            self: Instancia de la clase que representa al jugador.
            enemies: Grupo de enemigos en el juego representado por un objeto pygame.sprite.Group.

        Devuelve:
            None
        """
        try:
            hit_list = pygame.sprite.spritecollide(self, enemies, False)

            if len(hit_list) > 0 and self.invincibility == 0:
                play_sound(hurt_sound)
                self._hearts -= 1
                self.invincibility = int(0.75 * FPS)
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def process_traps(self, traps: pygame.sprite.Group) -> None:
        """
        Procesa las colisiones entre el jugador y las trampas, aplicando el efecto de la trampa y reproduciendo un sonido.

        Parámetros:
            self: Instancia de la clase que representa al jugador.
            traps: Grupo de trampas en el juego representado por un objeto pygame.sprite.Group.

        Devuelve:
            None
        """
        try:
            hit_list = pygame.sprite.spritecollide(self, traps, True)

            for i in hit_list:
                play_sound(trap_sound)
                i.apply(self)
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def check_flag(self, level) -> None:
        """
        Verifica si el personaje ha alcanzado la bandera al final del nivel y realiza las acciones correspondientes.

        Parámetros:
            self: Instancia de la clase que representa al personaje del juego.
            level: Nivel actual del juego.

        Devuelve:
            None
        """
        try:
            hit_list = pygame.sprite.spritecollide(self, level.flag, False)

            if len(hit_list) > 0:
                level.completed = True
                self.nivel_actual += 1
                if self.nivel_actual == 4:
                    play_sound(juego_ganado_sound)
                else:
                    play_sound(levelup_sound)
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def set_image(self) -> None:
        """
        Establece la imagen del jugador en función de su estado y movimiento actual.

        Parámetros:
            self: Instancia de la clase que representa al jugador.

        Devuelve:
            None
        """
        try:
            if self.on_ground:
                if self.vx != 0:
                    if self._facing_right:
                        self.running_images = self.images_run_right
                    else:
                        self.running_images = self.images_run_left

                    self.steps = (self.steps + 1) % 5

                    if self.steps == 0:
                        self.image_index = (self.image_index + 1) % len(self.running_images)
                        self.image = self.running_images[self.image_index]
                else:
                    if self._facing_right:
                        self.image = self.image_idle_right
                    else:
                        self.image = self.image_idle_left
            else:
                if self._facing_right:
                    self.image = self.image_jump_right
                else:
                    self.image = self.image_jump_left
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def die(self) -> None:
        """
        Realiza las acciones correspondientes cuando el personaje muere, como disminuir sus vidas y reproducir sonidos.

        Parámetros:
            self: Instancia de la clase que representa al personaje del juego.

        Devuelve:
            None
        """
        try:
            self._lives -= 1

            if self._lives > 0:
                play_sound(die_sound)
            else:
                play_sound(gameover_sound)
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def respawn(self, level) -> None:
        """
        Respawn del jugador en el nivel actual, restableciendo su posición, corazones, invencibilidad y dirección.

        Parámetros:
            self: Instancia de la clase que representa al jugador.
            level: Nivel actual del juego.

        Devuelve:
            None
        """
        try:
            self.rect.x = level.start_x
            self.rect.y = level.start_y
            self._hearts = self._max_hearts
            self.invincibility = 0
            self._facing_right = True
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def update(self, level) -> None:
        """
        Actualiza el jugador en función del nivel actual, procesando colisiones, gravedad, movimiento, límites del mundo y estableciendo la imagen.

        Parámetros:
            self: Instancia de la clase que representa al jugador.
            level: Nivel actual del juego.

        Devuelve:
            None
        """
        try:
            self.process_enemies(level.enemies)
            self.apply_gravity(level)
            self.move_and_process_blocks(level.blocks)
            self.check_world_boundaries(level)
            self.set_image()

            if self._hearts > 0:
                self.process_coins(level.coins)
                self.process_soles(level.soles)
                self.process_traps(level.powerups)
                self.check_flag(level)

                if self.invincibility > 0:
                    self.invincibility -= 1
            else:
                self.die()
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
