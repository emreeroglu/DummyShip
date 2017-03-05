from tkinter import Tk

from DummySpaceGame import DummySpaceGame
from Space import Space


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
    app = DummySpaceGame(parent=root, space=space)
    app.mainloop() 


if __name__ == '__main__':
    main()

