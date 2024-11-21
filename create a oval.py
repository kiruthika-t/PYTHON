from tkinter import*
master = Tk()
w =Canvas(master, width =700 ,height =1000)

#create a oval
w.create_oval(200,200,700,700,width = 5 ,fill="dark blue", outline = "blue")

w.pack()

mainloop()