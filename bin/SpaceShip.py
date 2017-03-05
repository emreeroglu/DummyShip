from tkinter import Label
from Bullet import Bullet


class SpaceShip(Label):
    def __init__(self, space):
        self.ship_indicator = "."
        Label.__init__(self, text=self.ship_indicator)
        # initial coordinates
        self.space = space
        self.x = space.width/2
        self.y = space.height/2
        self.pack()
        self.place_ship()
        self._observers = []
        self._bullet_count = 0
        self._life = 0

    def left_key(self, event):
        self.x -= 10
        self.place_ship()

    def right_key(self, event):
        self.x += 10
        self.place_ship()

    def up_key(self, event):
        self.y -= 10
        self.place_ship()

    def down_key(self, event):
        self.y += 10
        self.place_ship()

    def space_key(self, event):
        self.shoot()

    def place_ship(self):
        if self.x > self.space.width:
            self.x -= self.space.width
        if self.x < 0:
            self.x += self.space.width
        if self.y > self.space.height:
            self.y -= self.space.height
        if self.y < 0:
            self.y += self.space.height
        self.place(x=self.x, y=self.y)

    def shoot(self):
        if self.bullet_count > 0:
            Bullet(x=self.x, y=self.y, space=self.space)
            self.bullet_count = -1

    def get_bullet_count(self):
        return self._bullet_count

    def set_bullet_count(self, value):
        self._bullet_count += value
        for callback in self._observers:
            callback(bullet_count=self._bullet_count)

    bullet_count = property(get_bullet_count, set_bullet_count)

    def hit(self, object):
        self._life = object.damage
        if self._life <= 0:
            self.destroy()

    def get_life(self):
        return self._life

    def set_life(self, value):
        self._life += value
        for callback in self._observers:
            callback(life=self._life)

    life = property(get_life, set_life)

    def bind_to(self, callback):
        self._observers.append(callback)