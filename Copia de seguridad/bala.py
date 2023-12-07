from objeto import Objeto
from constantes import WIDTH

class Bullet(Objeto):
    def __init__(self, x, y, direction, speed, image, shooter):
        super().__init__(x, y, image)
        self.vx = speed * direction
        self._damage = 1
        self.shooter = shooter

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, valor):
        self._damage = valor

    def update(self) -> None:
        """
        Actualiza el estado de la bala.

        Parámetros:
            self: Instancia de la clase que representa a la bala.

        Devuelve:
            None
        """
        try:
            self.rect.x += self.vx

            if self.rect.right < 0 or self.rect.left > WIDTH:
                self.kill()
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
