from objeto import Objeto
from auxiliar import load_image

flag_img = load_image("C:\\Users\\franc\\Downloads\\PIXEL ADVENTURE\\Recursos\\Items\\Checkpoints\\End\\End (Pressed) (64x64)2.png")
flagpole_img = load_image("C:\\Users\\franc\\Downloads\\PIXEL ADVENTURE\\Recursos\\Items\\Checkpoints\\Checkpoint\\Checkpoint (No Flag)2.png")

class Flag(Objeto):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
