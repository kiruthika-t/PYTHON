from tkinter import*

w=Canvas(width=700,height=1200)

points = [20,50,30,50,60,100,80,70,90,100,110,120,130,500]

w.create_polygon(points ,fill ="red" ,outline = "dark blue",width = 3)

w.pack()

mainloop()
