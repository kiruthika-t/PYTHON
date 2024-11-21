from tkinter import*
master = Tk()

w =Canvas(master,width =700,height =2000)

#create a rectangle
w.create_rectangle(1200,500,500,200,width=2,fill="red",outline ="dark red")

w.pack()

mainloop()