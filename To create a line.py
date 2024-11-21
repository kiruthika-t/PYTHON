from tkinter import*
master = Tk()
canvas_width = 80
canvas_height = 40
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()
y = int(canvas_height / 2)
w.create_line(20, 20, canvas_width, y, fill="dark blue")
mainloop() 