from objeto import Objeto
from jugador import Character
from auxiliar import load_image

heart_img = load_image("C:\\Users\\franc\\Downloads\\PIXEL ADVENTURE\\Recursos\\Items\\Fruits\\Cherries2.png")

class Heart(Objeto):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def apply(self, character: Character) -> None:
        """
        Aplica el efecto de un corazón al jugador.

        Parámetros:
            character: Instancia de la clase Character a la que se le aplicará el efecto del corazón.

        Devuelve:
            None
        """
        try:
            character.hearts += 1
            character.score += 2
            character.hearts = max(character.hearts, character.max_hearts)
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
