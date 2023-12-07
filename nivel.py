import pygame
import json
import random
from terreno_y_plataformas import Block, block_images
from octavio import Octavio, octavio_image
from pajaro import Pajaro, pajaro_images
from conejo import Conejo, conejo_images
from moneda import Coin, coin_img
from sol import Sol, sol_img
from trampa import Trampa, trap_img
from corazon import Heart, heart_img
from bandera import Flag, flag_img, flagpole_img
from constantes import GRID_SIZE, HEIGHT

class Level():

    def __init__(self, file_path):
        self.starting_blocks = []
        self.starting_enemies = []
        self.starting_coins = []
        self.starting_soles = []
        self.starting_powerups = []
        self.starting_flag = []

        self.bullets = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.soles = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.flag = pygame.sprite.Group()

        self.active_sprites = pygame.sprite.Group()
        self.inactive_sprites = pygame.sprite.Group()

        with open(file_path, 'r') as f:
            data = f.read()

        map_data = json.loads(data)

        max_width = map_data["width"]
        max_height = map_data["height"]

        if map_data['name'] == 'Nivel 1':
            for _ in range(5):
                x = random.randint(0, max_width - 10)
                y = random.randint(0, max_height - 10)
                map_data["pajaros"].append([x, y])

        if map_data['name'] == 'Nivel 2':
            for _ in range(5):
                x = random.randint(0, max_width - 10)
                y = random.randint(0, max_height - 10)
                map_data["conejos"].append([x, y])

        self.width = map_data['width'] * GRID_SIZE
        self.height = map_data['height'] * GRID_SIZE

        self.start_x = map_data['start'][0] * GRID_SIZE
        self.start_y = map_data['start'][1] * GRID_SIZE

        for item in map_data['blocks']:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE
            img = block_images[item[2]]
            self.starting_blocks.append(Block(x, y, img))

        for item in map_data['conejos']:
            x, y = item[0] * GRID_SIZE, 0
            self.starting_enemies.append(Conejo(x, y, conejo_images))

        for item in map_data['octavios']:
            x, y = item[0] * GRID_SIZE, 0
            self.starting_enemies.append(Octavio(x, y, octavio_image))

        for item in map_data['pajaros']:
            x, y = item[0] * GRID_SIZE, 0
            self.starting_enemies.append(Pajaro(x, y, pajaro_images))

        for item in map_data['coins']:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE
            self.starting_coins.append(Coin(x, y, coin_img))

        for item in map_data['soles']:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE
            self.starting_soles.append(Sol(x, y, sol_img))

        for item in map_data['traps']:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE
            self.starting_powerups.append(Trampa(x, y, trap_img))

        for item in map_data['hearts']:
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE
            self.starting_powerups.append(Heart(x, y, heart_img))

        for i, item in enumerate(map_data['flag']):
            x, y = item[0] * GRID_SIZE, item[1] * GRID_SIZE

            if i == 0:
                img = flag_img
            else:
                img = flagpole_img

            self.starting_flag.append(Flag(x, y, img))

        self.background_layer = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        self.scenery_layer = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        self.inactive_layer = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        self.active_layer = pygame.Surface([self.width, self.height], pygame.SRCALPHA)

        if map_data['background-img'] != "":
            background_img = pygame.image.load(map_data['background-img'])

            if map_data['background-fill-y']:
                h = background_img.get_height()
                w = int(background_img.get_width() * HEIGHT / h)
                background_img = pygame.transform.scale(background_img, (w, HEIGHT))

            if "top" in map_data['background-position']:
                start_y = 0

            if map_data['background-repeat-x']:
                for x in range(0, self.width, background_img.get_width()):
                    self.background_layer.blit(background_img, [x, start_y])
            else:
                self.background_layer.blit(background_img, [0, start_y])

        if map_data['scenery-img'] != "":
            scenery_img = pygame.image.load(map_data['scenery-img'])

            if map_data['scenery-fill-y']:
                h = scenery_img.get_height()
                w = int(scenery_img.get_width() * HEIGHT / h)
                scenery_img = pygame.transform.scale(scenery_img, (w, HEIGHT))

            if map_data['scenery-repeat-x']:
                for x in range(0, self.width, scenery_img.get_width()):
                    self.scenery_layer.blit(scenery_img, [x, start_y])
            else:
                self.scenery_layer.blit(scenery_img, [0, start_y])

        pygame.mixer.music.load(map_data['music'])

        self.gravity = map_data['gravity']
        self.terminal_velocity = map_data['terminal-velocity']

        self.completed = False

        self.blocks.add(self.starting_blocks)
        self.enemies.add(self.starting_enemies)
        self.coins.add(self.starting_coins)
        self.soles.add(self.starting_soles)
        self.powerups.add(self.starting_powerups)
        self.flag.add(self.starting_flag)

        self.active_sprites.add(self.coins, self.soles, self.enemies, self.powerups)
        self.inactive_sprites.add(self.blocks, self.flag)

        self.inactive_sprites.draw(self.inactive_layer)

    def reset(self) -> None:
        """
        Reinicia el nivel del juego, restaurando los elementos iniciales y reiniciando los enemigos.

        Parámetros:
            self: Instancia de la clase que representa el nivel del juego.

        Devuelve:
            None
        """
        try:
            self.enemies.add(self.starting_enemies)
            self.coins.add(self.starting_coins)
            self.soles.add(self.starting_soles)
            self.powerups.add(self.starting_powerups)

            self.active_sprites.add(self.coins, self.soles, self.enemies, self.powerups)

            for enemy in self.enemies:
                enemy.reset()
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
