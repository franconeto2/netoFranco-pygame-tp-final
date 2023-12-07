from objeto import Objeto
from auxiliar import load_image

block_images = {"BL": load_image("C:\\Users\\franc\\Downloads\\PIXEL ADVENTURE\\Recursos\\Terrain\\Terrain (16x16)2.png")}

class Block(Objeto):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)
