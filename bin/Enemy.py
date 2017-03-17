from tkinter import Label
from random import randint


class Enemy(Label):
    def __init__(self, space):
        self.space = space
        self.enemy_indicator = "*"
        self.life = 100
        Label.__init__(self, text=self.enemy_indicator)
        self.pack()
        self.x = randint(0, self.space.width)
        self.y = randint(0, self.space.height)
        self.x = self.x//10 * 10
        self.y = self.y//10 * 10
        self.place(x=self.x, y=self.y)

    def hit(self, thing):
        if self.x == thing._x and self.y == thing._y:
            self.life += thing.damage
            thing.hit()
            if self.life <= 0:
                self.destroy()

