from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time
class Sprite:
    def __init__(self, canvas, x, y, images):
        self.canvas = canvas
        self.images = [ImageTk.PhotoImage(Image.open(img)) for img in images]
        self.frame = 0
        self.id = canvas.create_image(x,y,image=self.images[self.frame])

    def update(self):
        self.frame = (self.frame+1)%len(self.images)
        self.canvas.itemconfig(self.id, image=self.images[self.frame])

    def move_left(self):
        self.canvas.move(self.id, -10, 0)

    def move_right(self):
        self.canvas.move(self.id, 10, 0)

    def move_up(self):
        self.canvas.move(self.id, 0, -10)

    def move_down(self):
        self.canvas.move(self.id, 0, 10)


root = tk.Tk()
canvas = tk.Canvas(root, width=4000, height=4000)
canvas.pack()

sprite_images = ['Sprites/idle/0.png','Sprites/idle/1.png',
                 'Sprites/idle/2.png','Sprites/idle/3.png',
                 'Sprites/idle/4.png','Sprites/idle/5.png',
                 'Sprites/idle/6.png','Sprites/idle/7.png',
                 'Sprites/idle/8.png','Sprites/idle/9.png',
                 'Sprites/idle/10.png','Sprites/idle/11.png']

sprite = Sprite(canvas, 100, 100, sprite_images)

def handle_key(event):
    if event.keysym == 'Up':
        sprite.move_up()
        print("up")
    elif event.keysym == 'Down':
        sprite.move_down()
    elif event.keysym == 'Left':
        sprite.move_left()
    elif event.keysym == 'Right':
        sprite.move_right()

canvas.bind_all('<KeyPress>', handle_key)
while True:
    sprite.update()
    canvas.update()
    time.sleep(0.0005)





root.mainloop()















