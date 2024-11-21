from tkinter import*

master =Tk()

w=Canvas(master,width =700 ,height=1200)

w.create_arc(100,100,400,300,width = 3,start =270,extent=180,outline ="dark blue",style ="arc")

w.pack()

mainloop()