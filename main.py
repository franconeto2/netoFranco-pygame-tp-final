import pygame
import sys
from nivel import Level
from jugador import Character, hero_images
from constantes import WIDTH, HEIGHT, TITLE, WHITE, JUMP, LEFT, RIGHT, TRANSPARENT, FPS, BLACK
from auxiliar import play_music, play_sound
import seleccionar_nivel
import sonido

pygame.init()

niveles = ["C:\\Users\\franc\\Downloads\\faltano\\levels\\nivel1.json",
          "C:\\Users\\franc\\Downloads\\faltano\\levels\\nivel2.json",
          "C:\\Users\\franc\\Downloads\\faltano\\levels\\nivel3.json"]

fuente = pygame.font.Font("C:\\Users\\franc\\Downloads\\faltano\\fonts\\times.ttf", 32)
fuente_negrita = pygame.font.Font("C:\\Users\\franc\\Downloads\\faltano\\fonts\\timesbd.ttf", 64)
fuente_negrita_inclinada = pygame.font.Font("C:\\Users\\franc\\Downloads\\faltano\\fonts\\timesbi.ttf", 72)

sonido_salto = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Mario Jump Sound Effect.mp3")
sonido_bitcoin = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Cash Register  Sound EffectHD.mp3")
sonido_sol = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\TWINKLE Sound Effect.mp3")
sonido_fruta = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Crunch sound effect  No copyright.mp3")
sonido_danio_recibido = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Punch Sound Effect  Gaming SFX.mp3")
sonido_muerte = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Fortnite Death Sound Effect No copyright.mp3")
sonido_enemigo_muerto = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Y2meta.app - CS_GO Zeus Sound (128 kbps).mp3")
sonido_bola_fuego = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Fire Whoosh Sound Effect Commercial.mp3")
sonido_compu = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Y2meta.app - Windows XP Error Sound effect (128 kbps).mp3")
sonido_comer =  pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Y2meta.app - Power-Up - Sound Effect (HD) (128 kbps).mp3")
sonido_nivel_pasado = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Milei Zurdos hijos de puta tiemblen la libertad avanza.mp3")
sonido_gameover = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Lose sound effects.mp3")
sonido_juego_ganado = pygame.mixer.Sound("C:\\Users\\franc\\Downloads\\faltano\\sounds\\Celebracion en BUENOS AIRES ARGENTINA CAMPEN  Celebration in BUENOS AIRES ARGENTINA CHAMPION.mp3")

class Game():

    SELECCION_NIVEL = 0
    INICIO = 1
    JUGANDO = 2
    PAUSADO = 3
    NIVEL_PASADO = 4
    GAME_OVER = 5
    JUEGO_GANADO = 6

    def __init__(self):
        self._ventana = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)
        self._reloj = pygame.time.Clock()
        self._terminar = False

        self.reset()

        self._tiempo_restante = 60
        self._tiempo_anterior = pygame.time.get_ticks()

    @property
    def ventana(self):
        return self._ventana

    @ventana.setter
    def ventana(self, valor):
        self._ventana = valor

    @property
    def reloj(self):
        return self._reloj

    @property
    def terminar(self):
        return self._terminar

    @property
    def tiempo_restante(self):
        return self._tiempo_restante

    @tiempo_restante.setter
    def tiempo_restante(self, valor):
        self._tiempo_restante = valor

    @property
    def tiempo_anterior(self):
        return self._tiempo_anterior

    def pausa(self) -> None:
        """
        Pausa el juego y pausa la música de fondo.

        Parámetros:
            self: Instancia de la clase Game.

        Devuelve:
            None
        """
        try:
            self.estado = Game.PAUSADO
            pygame.mixer.music.pause()
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def reanudar(self) -> None:
        """
        Reanuda el juego y reanuda la música de fondo.

        Parámetros:
            self: Instancia de la clase Game.

        Devuelve:
            None
        """
        try:
            self.estado = Game.JUGANDO
            pygame.mixer.music.unpause()
            self._tiempo_anterior = pygame.time.get_ticks()
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
    def iniciar(self) -> None:
        """
        Inicia un nuevo nivel del juego.

        Parámetros:
            self: Instancia de la clase Game.

        Devuelve:
            None
        """
        try:
            self.nivel = Level(niveles[self.nivel_actual])
            self.nivel.reset()
            self.jugador.respawn(self.nivel)
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def avanzar(self) -> None:
        """
        Avanza al siguiente nivel del juego.

        Parámetros:
            self: Instancia de la clase Game.

        Devuelve:
            Nne
        """
        try:
            self.nivel_actual += 1
            self.tiempo_restante = 60
            self.iniciar()
            self.estado = Game.INICIO
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def reset(self) -> None:
        """
        Reinicia el juego al estado inicial.

        Parámetros:
            self: Instancia de la clase Game.

        Devuelve:
            None
        """
        try:
            self.jugador = Character(hero_images)
            self.nivel_actual = 0
            self.iniciar()
            self.estado = Game.SELECCION_NIVEL
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def mostrar_mensaje(self, superficie: pygame.Surface, texto_principal: str, texto_secundario: str) -> None:
        """
        Muestra un mensaje en la superficie especificada.

        Parámetros:
            self: Instancia de la clase Game.
            superficie: Superficie de pygame donde se mostrará el mensaje.
            texto_principal: Texto principal del mensaje.
            texto_secundario: Texto secundario del mensaje.

        Devuelve:
            None
        """
        try:
            linea1 = fuente_negrita.render(texto_principal, 1, BLACK)
            linea2 = fuente.render(texto_secundario, 1, BLACK)

            caja_texto_ancho = max(linea1.get_width(), linea2.get_width())
            caja__texto_altura = linea1.get_height() + linea2.get_height()

            # Esquina superior izquierda de la caja
            caja_texto_x = (WIDTH - caja_texto_ancho) // 2
            caja_texto_y = (HEIGHT - caja__texto_altura) // 2

            pygame.draw.rect(superficie, WHITE, (caja_texto_x, caja_texto_y, caja_texto_ancho, caja__texto_altura))

            x1 = caja_texto_x
            y1 = caja_texto_y

            x2 = caja_texto_x
            y2 = y1 + linea1.get_height()

            superficie.blit(linea1, (x1, y1))
            superficie.blit(linea2, (x2, y2))
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def mostrar_info(self, superficie: pygame.Surface) -> None:
        """
        Muestra la información del juego en la superficie especificada.

        Parámetros:
            self: Instancia de la clase Game.
            superficie: Superficie de pygame donde se mostrará la información.

        Devuelve:
            None
        """
        try:
            texto_corazones = fuente.render(f"Corazones: {str(self.jugador.hearts)}/4", 1, WHITE)
            texto_vidas = fuente.render("Vidas: " + str(self.jugador.lives), 1, WHITE)
            texto_puntuacion = fuente.render("Puntuación: " + str(self.jugador.score), 1, WHITE)
            tiempo_text = fuente.render("Tiempo restante: " + str(int(self.tiempo_restante)), 1, WHITE)

            if not self.jugador.nivel_actual == 4:
                texto_nivel = fuente.render("Nivel: " + str(self.jugador.nivel_actual), 1, WHITE)
            else:
                texto_nivel = fuente.render("Juego Completado" , 1, WHITE)

            superficie.blit(texto_puntuacion, (WIDTH - texto_puntuacion.get_width() - 32, 32))
            superficie.blit(texto_corazones, (32, 32))
            superficie.blit(texto_vidas, (32, 64))
            superficie.blit(texto_nivel, (32, 96))
            superficie.blit(tiempo_text, (32, 128))
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def procesar_eventos(self) -> None:
        """
        Procesa los eventos del juego, como teclas presionadas o eventos de salida.

        Parámetros:
            self: Instancia de la clase Game.

        Devuelve:
            None
        """
        try:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self._terminar = True

                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        if self.estado == Game.JUGANDO:
                            self.pausa()
                        elif self.estado == Game.PAUSADO:
                            self.reanudar()
                    if evento.key == pygame.K_p:
                            self.jugador.shoot(self.nivel.bullets, self.nivel)
                    if self.estado == Game.SELECCION_NIVEL or self.estado == Game.INICIO:
                        self.estado = Game.JUGANDO
                        play_music()

                    elif self.estado == Game.JUGANDO:
                        if evento.key == JUMP:
                            self.jugador.jump(self.nivel.blocks)

                    elif self.estado == Game.PAUSADO:
                        pass

                    elif self.estado == Game.NIVEL_PASADO:
                        self.avanzar()

            tecla_presionada = pygame.key.get_pressed()

            if self.estado == Game.JUGANDO:
                if tecla_presionada[LEFT]:
                    self.jugador.move_left()
                elif tecla_presionada[RIGHT]:
                    self.jugador.move_right()
                else:
                    self.jugador.stop()
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def update(self) -> None:
        """
        Actualiza el estado del juego y los objetos en el mismo.

        Parámetros:
            self: Instancia de la clase Game.

        Devuelve:
            None
        """
        try:
            for bala in self.nivel.bullets:
                if bala.shooter != self.jugador:
                    if pygame.sprite.collide_rect(self.jugador, bala):
                        self.jugador.take_damage()
                        bala.kill()
                enemigos_daniados = pygame.sprite.spritecollide(bala, self.nivel.enemies, False)
                for enemigo in enemigos_daniados:
                    if self.jugador == bala.shooter:
                        enemigo.take_damage(bala.damage, self.jugador)
                        bala.kill()

            if self.estado == Game.JUGANDO:
                tiempo_actual = pygame.time.get_ticks()
                delta_tiempo = tiempo_actual - self._tiempo_anterior
                self._tiempo_anterior = tiempo_actual
                self.tiempo_restante -= delta_tiempo / 1000

                self.jugador.update(self.nivel)
                self.nivel.enemies.update(self.nivel, self.jugador)
                for bala in self.nivel.bullets:
                    bala.update()

            if self.nivel.completed:
                if self.nivel_actual < len(niveles) - 1:
                    self.estado = Game.NIVEL_PASADO
                else:
                    self.estado = Game.JUEGO_GANADO
                pygame.mixer.music.stop()

            elif self.estado != Game.GAME_OVER and (self.tiempo_restante <= 0 or self.jugador.lives == 0):
                self.estado = Game.GAME_OVER
                pygame.mixer.music.stop()
                play_sound(sonido_gameover)

            elif self.jugador.hearts == 0:
                self.nivel.reset()
                self.jugador.respawn(self.nivel)
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def calcular_desplazamiento_horizontal(self) -> (int, int):
        """
        Calcula el desplazamiento horizontal de la cámara en el juego.

        Parámetros:
            self: Instancia de la clase Game.

        Devuelve:
            int, int: Coordenadas de desplazamiento horizontal (x) y vertical (y).
        """
        try:
            x = -1 * self.jugador.rect.centerx + WIDTH / 2

            if self.jugador.rect.centerx < WIDTH / 2:
                x = 0
            elif self.jugador.rect.centerx > self.nivel.width - WIDTH / 2:
                x = -1 * self.nivel.width + WIDTH

            return x, 0
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def draw(self) -> None:
        """
        Dibuja los elementos del juego en la ventana.

        Parámetros:
            self: Instancia de la clase Game.

        Devuelve:
            None
        """
        try:
            desplazamiento_x, desplazamiento_y = self.calcular_desplazamiento_horizontal()

            self.nivel.active_layer.fill(TRANSPARENT)
            self.nivel.active_sprites.draw(self.nivel.active_layer)

            if self.jugador.invincibility % 3 < 2:
                self.nivel.active_layer.blit(self.jugador.image, [self.jugador.rect.x, self.jugador.rect.y])

            self.ventana.blit(self.nivel.background_layer, [desplazamiento_x, desplazamiento_y])
            self.ventana.blit(self.nivel.scenery_layer, [desplazamiento_x, desplazamiento_y])
            self.ventana.blit(self.nivel.inactive_layer, [desplazamiento_x, desplazamiento_y])
            self.ventana.blit(self.nivel.active_layer, [desplazamiento_x, desplazamiento_y])

            self.mostrar_info(self.ventana)

            if self.estado == Game.PAUSADO:
                self.mostrar_mensaje(self.ventana, "Juego Pausado", "Tomate un descanso y apretá 'ESCAPE' cuando estés listo.")
            elif self.estado == Game.NIVEL_PASADO:
                self.mostrar_mensaje(self.ventana, "Completaste este nivel", "Apretá cualquier tecla para seguir.")
            elif self.estado == Game.JUEGO_GANADO:
                self.mostrar_mensaje(self.ventana, "¡Ganaste!", "")
            elif self.estado == Game.GAME_OVER:
                self.mostrar_mensaje(self.ventana, "Juego Terminado", "")

            pygame.display.flip()
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

    def bucle_principal(self) -> None:
        """
        Bucle principal del juego que controla la lógica del juego y su renderizado.

        Parámetros:
            self: Instancia de la clase Game.

        Devuelve:
            None
        """
        try:
            while not self._terminar:
                self.procesar_eventos()
                self.update()
                self.draw()
                self._reloj.tick(FPS)
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

if __name__ == "__main__":
    game = Game()
    game.nivel_actual = seleccionar_nivel.nivel_seleccionado - 1
    game.iniciar()
    game.bucle_principal()
    pygame.quit()
    sys.exit()
