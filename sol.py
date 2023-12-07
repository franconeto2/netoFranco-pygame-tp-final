from objeto import Objeto
from auxiliar import load_image

sol_img = load_image("C:\\Users\\franc\\Downloads\\faltano\\assets\\coins\\pngtree-the-bright-and-colorful-star-png-image_13322861.png")

class Sol(Objeto):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

        self._value = 1

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, valor):
        self._value = valor
