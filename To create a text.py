from tkinter import*
master = Tk()
w= Canvas(master,width=700,height=1200)

#to create a text
fnt = ("times",20,"bold")

w.create_text(300,50,text = "WELCOME TO THE WORLD" , font =fnt ,fill="red")

w.pack()
mainloop()