from tkinter import Label
import threading
from random import randint

from Bullet import Bullet
from Enemy import Enemy


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
        self._bullets = set()
        self._enemies = set()
        self._bullet_count = 0
        self._life = 0
        self.enemy_generator()

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
            bullet = Bullet(x=self.x, y=self.y, space=self.space)
            bullet.bind_to(self.hit)
            for enemy in self._enemies:
                bullet.bind_to(enemy.hit)
            bullet.start()
            self._bullets.add(bullet)
            self.bullet_count = -1

    def get_bullet_count(self):
        return self._bullet_count

    def set_bullet_count(self, value):
        self._bullet_count += value
        for callback in self._observers:
            callback(bullet_count=self._bullet_count)

    bullet_count = property(get_bullet_count, set_bullet_count)

    def hit(self, thing):
        if self.x == thing._x and self.y == thing._y:
            self.set_life(thing.damage)
            thing.hit()
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

    def enemy_generator(self):
        self.generate_enemy()
        process = threading.Timer(randint(0, 5), self.enemy_generator, [])
        process.start()

    def generate_enemy(self):
        enemy = Enemy(self.space)
        self._enemies.add(enemy)
        for bullet in self._bullets:
            bullet.bind_to(enemy.hit)

