from tkinter import BOTH, Frame

from SpaceShip import SpaceShip


class DummySpaceGame(Frame):
    def __init__(self, parent, space):
        Frame.__init__(self, parent)

        # Set game window arguments.
        self.parent = parent
        self.pack(fill=BOTH, expand=1)
        self.bullet_count = 0
        self.life = 0

        # Set space.
        self.space = space

        # Set space ship.
        self.space_ship = SpaceShip(space=self.space)
        self.space_ship.bind_to(self.set_title)
        self.space_ship.bullet_count = 3
        self.space_ship.set_life(100)

        parent.bind('<Left>', self.space_ship.left_key)
        parent.bind('<Right>', self.space_ship.right_key)
        parent.bind('<Up>', self.space_ship.up_key)
        parent.bind('<Down>', self.space_ship.down_key)
        parent.bind('<space>', self.space_ship.space_key)

    def set_title(self, bullet_count=None, life=None):
        if bullet_count is not None:
            self.bullet_count = bullet_count
        if life is not None:
            self.life = life
            if life <= 0:
                self.parent.title("Dummy Space Ship - Game Over")
        if self.life > 0:
            self.parent.title("Dummy Space Ship - Bullet: " + str(self.bullet_count) + " Life: " + str(self.life))
