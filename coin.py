from GameObject_class import GameObject


class Coin(GameObject):
    def __init__(self, group, animations, cords):
        super().__init__(group, animations, (35, 35), cords, (180, 200))
