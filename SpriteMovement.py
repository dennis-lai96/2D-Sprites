from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time
class Sprite:
    def __init__(self, canvas, x, y):
        self.sprite_idle = ['Sprites/idle/0.png','Sprites/idle/1.png',
                              'Sprites/idle/2.png','Sprites/idle/3.png',
                              'Sprites/idle/4.png','Sprites/idle/5.png',
                              'Sprites/idle/6.png','Sprites/idle/7.png',
                              'Sprites/idle/8.png','Sprites/idle/9.png',
                              'Sprites/idle/10.png','Sprites/idle/11.png']

        self.sprite_left = ['Sprites/walk_W/0.png', 'Sprites/walk_W/1.png',
                            'Sprites/walk_W/2.png', 'Sprites/walk_W/3.png']

        self.sprite_right = ['Sprites/walk_E/0.png', 'Sprites/walk_E/1.png',
                            'Sprites/walk_E/2.png', 'Sprites/walk_E/3.png']

        self.sprite_north = ['Sprites/walk_N/0.png', 'Sprites/walk_N/1.png',
                             'Sprites/walk_N/2.png', 'Sprites/walk_N/3.png']

        self.sprite_south = ['Sprites/walk_S/0.png', 'Sprites/walk_S/1.png',
                             'Sprites/walk_S/2.png', 'Sprites/walk_S/3.png']

        self.x = 0
        self.y = 0
        self.canvas = canvas
        self.images = [ImageTk.PhotoImage(Image.open(img)) for img in self.sprite_idle]
        self.frame = 0
        self.id = canvas.create_image(x,y,image=self.images[self.frame])
        self.changeInX= 0
        self.changeInY= 0
        self.state = 'idle' #initializes the state to idle when the sprite is created

    def update(self):
        print(self.x,self.y)
        if self.changeInX==0 and self.changeInY==0:
            self.state='idle'
        elif self.changeInX<0:
            self.state ='left'
        elif self.changeInX > 0:
            self.state = 'right'
        elif self.changeInY < 0:
            self.state = 'up'
        elif self.changeInY > 0:
            self.state = 'down'

        #print(self.changeInY,self.changeInX)

        if self.state=='idle':
            self.images = [ImageTk.PhotoImage(Image.open(img)) for img in self.sprite_idle]
            self.frame = (self.frame+1)%len(self.images)
            self.canvas.itemconfig(self.id, image=self.images[self.frame])
        elif self.state == 'left':
            self.images = [ImageTk.PhotoImage(Image.open(img)) for img in self.sprite_left]
            self.frame = (self.frame+1)%len(self.images)
            self.canvas.itemconfig(self.id, image=self.images[self.frame])
        elif self.state == 'right':
            self.images = [ImageTk.PhotoImage(Image.open(img)) for img in self.sprite_right]
            self.frame = (self.frame+1)%len(self.images)
            self.canvas.itemconfig(self.id, image=self.images[self.frame])
        elif self.state == 'up':
            print("state")
            self.images = [ImageTk.PhotoImage(Image.open(img)) for img in self.sprite_north]
            self.frame = (self.frame+1)%len(self.images)
            self.canvas.itemconfig(self.id, image=self.images[self.frame])
        elif self.state == 'down':
            self.images = [ImageTk.PhotoImage(Image.open(img)) for img in self.sprite_south]
            self.frame = (self.frame+1)%len(self.images)
            self.canvas.itemconfig(self.id, image=self.images[self.frame])



    def move_left(self):
        self.changeInY = 0
        self.changeInX = -50
        if self.x >= 50:
            self.x = self.x + self.changeInX
            self.canvas.move(self.id, self.changeInX, self.changeInY)

    def move_right(self):
        self.changeInY = 0
        self.changeInX = 50
        if self.x <= 550:
            self.x = self.x + self.changeInX
            self.canvas.move(self.id, self.changeInX, self.changeInY)

    def move_up(self):
        self.changeInX = 0
        self.changeInY =-50
        if self.y >=50:
            self.y = self.y + self.changeInY
            self.canvas.move(self.id, self.changeInX, self.changeInY)

    def move_down(self):
        self.changeInX = 0
        self.changeInY = 50
        if self.y <=350:
            self.y = self.y + self.changeInY
            self.canvas.move(self.id, self.changeInX,self.changeInY)

    def stop(self):
        self.changeInX=0
        self.changeInY=0


root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

background_image= Image.open('Sprites/CATTO.jpg')
background_map=ImageTk.PhotoImage(background_image)
canvas.create_image(0,0,image=background_map,anchor="nw")



sprite = Sprite(canvas, 100, 100,)

#Assigning keybinds
def keyPress(event):
    if event.keysym == 'w':
        sprite.move_up()
    elif event.keysym == 's':
        sprite.move_down()
    elif event.keysym == 'a':
        sprite.move_left()
    elif event.keysym == 'd':
        sprite.move_right()

def keyRelease(event):
    sprite.stop()

canvas.bind_all('<KeyPress>', keyPress)
canvas.bind_all('<KeyRelease>', keyRelease)




#Gameloop
while True:

    sprite.update()
    canvas.update()
    time.sleep(0.005)

root.mainloop()















