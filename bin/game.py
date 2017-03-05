from tkinter import Tk, Label, BOTH, Frame
import threading


class Space:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Bullet(Label):
    def __init__(self, x, y, space):
        self.space = space
        self.bullet_timer = 0.01
        self.bullet_indicator = "'"
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
        self.life = 100
        self._observers = []
        self._bullet_count = 0

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

    def hit(self, object):
        pass

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
            callback(self._bullet_count)

    bullet_count = property(get_bullet_count, set_bullet_count)

    def bind_to(self, callback):
        self._observers.append(callback)


class DummyGame(Frame):
    def __init__(self, parent, space):
        Frame.__init__(self, parent)

        # Set game window arguments.
        self.parent = parent
        self.pack(fill=BOTH, expand=1)
        self.bullet_count = 0

        # Set space.
        self.space = space

        # Set space ship.
        self.space_ship = SpaceShip(space=self.space)
        self.space_ship.bind_to(self.set_title)
        self.space_ship.bullet_count = 3

        parent.bind('<Left>', self.space_ship.left_key)
        parent.bind('<Right>', self.space_ship.right_key)
        parent.bind('<Up>', self.space_ship.up_key)
        parent.bind('<Down>', self.space_ship.down_key)
        parent.bind('<space>', self.space_ship.space_key)

    def set_title(self, bullet_count=None):
        if bullet_count is not None:
            self.bullet_count = bullet_count
        self.parent.title("Dummy Space Ship - Bullet: " + str(self.bullet_count))


def main():
    space = Space(width=500, height=500)
    root = Tk()

    # Putting window to center of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    margin_x = int((screen_width - space.width) / 2)
    margin_y = int((screen_height - space.height) / 2)
    geometry = str(space.width) + "x" + str(space.height) + "+" + str(margin_x) + "+" + str(margin_y)
    root.geometry(geometry)
    app = DummyGame(parent=root, space=space)
    app.mainloop() 
    
if __name__ == '__main__':
    main()

