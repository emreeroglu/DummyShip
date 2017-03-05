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
        process = threading.Thread(target=self.place_bullet(x=x, y=y))
        process.start()

    def place_bullet(self, x, y):
        if y > 0:
            y -= 1
            self.place(x=x, y=y)
            process = threading.Timer(self.bullet_timer, self.place_bullet, [x, y])
            process.start()
        else:
            y += self.space.height
            self.place(x=x, y=y)
            process = threading.Timer(self.bullet_timer, self.place_bullet, [x, y])
            process.start()