from tkinter import *

root = Tk()


canvas = Canvas(root, width=800, height=500)
canvas.pack()

square = canvas.create_rectangle(50, 50, 50, 50, fill="red")


root.mainloop()
