import tkinter as tk

def change_color(color):
    C.itemconfig(arc, fill=color)

top = tk.Tk()
top.title("Color Changer")

frame = tk.Frame(top)
frame.pack()

C = tk.Canvas(frame, bg="blue", height=250, width=300)
C.pack()

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

color_frame = tk.Frame(frame)
color_frame.pack()

def change_color_red():
    change_color("red")

def change_color_brown():
    change_color("brown")

def change_color_blue():
    change_color("blue")

def change_color_black():
    change_color("black")

redbutton = tk.Button(color_frame, text="Red", fg="red", command=change_color_red)
redbutton.pack(side=tk.LEFT)

greenbutton = tk.Button(color_frame, text="Brown", fg="brown", command=change_color_brown)
greenbutton.pack(side=tk.LEFT)

bluebutton = tk.Button(color_frame, text="Blue", fg="blue", command=change_color_blue)
bluebutton.pack(side=tk.LEFT)

blackbutton = tk.Button(color_frame, text="Black", fg="black", command=change_color_black)
blackbutton.pack(side=tk.LEFT)

top.mainloop()
