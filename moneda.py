from objeto import Objeto
from auxiliar import load_image

coin_img = load_image("C:\\Users\\franc\\Downloads\\faltano\\assets\\coins\\bitcoin-logo-bitcoin-icon-transparent-free-png.png")

class Coin(Objeto):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

        self.value = 3

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, valor):
        self._value = valor
