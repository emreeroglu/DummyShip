from tkinter import Tk, Label, BOTH, Frame
import threading
import time

max_width=500
max_height=500
bullet_timer=0.01

class DummyGame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        parent.bind('<Left>', self.left_key)
        parent.bind('<Right>', self.right_key)
        parent.bind('<Up>', self.up_key)
        parent.bind('<Down>', self.down_key)
        parent.bind('<space>', self.space_key)
        self.parent = parent
        self.parent.title("Dummy Ship Game")
        self.pack(fill=BOTH, expand=1)
        # initial max_widthcoordinates
        self.x=max_width/2
        self.y=max_height/2
        self.create_widgets()
        

    def create_widgets(self):
        self.ship = Label(self, text="O")
        self.ship.pack()
        self.place_ship()

    def left_key(self, event):
        self.x=self.x-10
        self.place_ship()

    def right_key(self, event):
        self.x=self.x+10
        self.place_ship()
        
    def up_key(self, event):
        self.y=self.y-10
        self.place_ship()

    def down_key(self, event):
        self.y=self.y+10
        self.place_ship()
         
    def space_key(self, event):
        print("Spaceeee")
        self.shoot()
        
    def place_ship(self):
        if self.x > max_width:
            self.x=self.x-max_width
        if self.x < 0:
            self.x=self.x+max_width
        if self.y > max_height:
            self.y=self.y-max_height
        if self.y < 0:
            self.y=self.y+max_height
        self.ship.place(x=self.x,y=self.y)
        
    def shoot(self):
        self.bullet = Label(self, text="i")
        self.bullet.pack()
        Process = threading.Thread(target=self.place_bullet(bullet=self.bullet, x=self.x, y=self.y))
        Process.start()
        
    
    def place_bullet(self, bullet, x, y):
        if y>20:
           print("x: ", x)
           print("y: ", y)
           y=y-1
           bullet.place(x=x, y=y)
           Process = threading.Timer(bullet_timer, self.place_bullet, [bullet, x, y])
           Process.start()
        else:
            pass
            bullet.destroy()
            

def main():
    root = Tk()
    root.geometry("500x500+300+300")
    app = DummyGame(parent=root)
    app.mainloop() 
    
if __name__=='__main__':
    main()
    

