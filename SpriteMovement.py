from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title('Sprite Movement')
root.geometry("800x600")

w=600
h=400
x=w/2
y=h/2

my_canvas = Canvas(root,width=w,height=h,bg="white")
my_canvas.pack(pady=20)

img = PhotoImage(file="Sprites/idle/0.png")
my_image= my_canvas.create_image(200,150, anchor=NW,image = img)

def left(event):
    x = -10
    y= 0
    my_canvas.move(my_image,x,y)
def right(event):
    x = 10
    y= 0
    my_canvas.move(my_image,x,y)
def up(event):
    x = 0
    y= -10
    my_canvas.move(my_image,x,y)
def down(event):
    x = 0
    y= 10
    my_canvas.move(my_image,x,y)


root.bind("<a>", left)
root.bind("<d>", right)
root.bind("<w>", up)
root.bind("<s>",down)






root.mainloop()



