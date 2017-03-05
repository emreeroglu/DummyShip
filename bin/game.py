from tkinter import Tk, Label, BOTH, Frame
import threading


class Space:
    def __init__(self):
        self.max_width = 500
        self.max_height = 500


class Bullet(Label):
    def __init__(self, x, y, space):
        self.space = space
        self.bullet_timer = 0.01
        self.bullet_indicator = "."
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
            y += self.space.max_height
            self.place(x=x, y=y)
            process = threading.Timer(self.bullet_timer, self.place_bullet, [x, y])
            process.start()


class SpaceShip(Label):
    def __init__(self, space):
        self.ship_indicator = ","
        Label.__init__(self, text=self.ship_indicator)
        # initial coordinates
        self.space = space
        self.x = space.max_width/2
        self.y = space.max_height/2
        self.pack()
        self.place_ship()
        self.life = 100
        self.bullet_count = 3

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
        if self.x > self.space.max_width:
            self.x -= self.space.max_width
        if self.x < 0:
            self.x += self.space.max_width
        if self.y > self.space.max_height:
            self.y -= self.space.max_height
        if self.y < 0:
            self.y += self.space.max_height
        self.place(x=self.x, y=self.y)

    def shoot(self):
        if self.bullet_count > 0:
            Bullet(x=self.x, y=self.y, space=self.space)
            self.bullet_count -= 1


class DummyGame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        # Set space ship.
        self.space = Space()
        self.space_ship = SpaceShip(space=self.space)
        parent.bind('<Left>', self.space_ship.left_key)
        parent.bind('<Right>', self.space_ship.right_key)
        parent.bind('<Up>', self.space_ship.up_key)
        parent.bind('<Down>', self.space_ship.down_key)
        parent.bind('<space>', self.space_ship.space_key)

        # Set game window arguments.
        self.parent = parent
        self.pack(fill=BOTH, expand=1)
        self.set_title()

    def set_title(self):
        self.parent.title("Dummy Ship Game")



            

def main():
    root = Tk()
    root.geometry("500x500+300+300")
    app = DummyGame(parent=root)
    app.mainloop() 
    
if __name__ == '__main__':
    main()
    

