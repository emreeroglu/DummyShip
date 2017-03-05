from tkinter import Label
import threading


class Bullet(Label):
    def __init__(self, x, y, space):
        self.space = space
        self.bullet_timer = 0.01
        self.bullet_indicator = "'"
        self.damage = -100
        Label.__init__(self, text=self.bullet_indicator)
        self.pack()
        self._x = x
        self._y = y
        self._observers = []

    def start(self):
        process = threading.Thread(target=self.place_bullet)
        process.start()

    def place_bullet(self):
        if self._y > 0:
            self.set_y(-1)
            self.place(x=self._x, y=self._y)
            process = threading.Timer(self.bullet_timer, self.place_bullet, [])
            process.start()
        else:
            self.set_y(self.space.height)
            self.place(x=self._x, y=self._y)
            process = threading.Timer(self.bullet_timer, self.place_bullet, [])
            process.start()

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y += value
        for callback in self._observers:
            callback(x=self._x, y=self._y, thing=self)

    y = property(get_y, set_y)

    def bind_to(self, callback):
        self._observers.append(callback)

