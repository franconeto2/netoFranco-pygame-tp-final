from objeto import Objeto
from jugador import Character
from auxiliar import load_image

trap_img = load_image("C:\\Users\\franc\\Downloads\\faltano\\assets\\items\\trap.png")

class Trampa(Objeto):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def apply(self, character: Character) -> None:
        """
        Aplica el efecto de la trampa al jugador.

        Parámetros:
            self: Instancia de la clase que representa la trampa.
            character: Instancia de la clase que representa al jugador.

        Devuelve:
            None
        """
        try:
            character.score -= 1
            character.take_damage()
            if character.hearts <= 0:
                character.die()
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
