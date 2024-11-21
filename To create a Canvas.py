from tkinter import*
master =Tk()
w = Canvas(master,width =700 ,height =1000)

#create line

w.create_line(50 ,50,200,50,200,150,width = 4 ,fill="dark blue")

#create rectangle

w.create_rectangle(500,200,700,600,width=5,fill="dark red",outline="black")

#create oval

w.create_oval(100 ,100 ,400 ,300 , width =5 ,fill ="red" ,outline ="black")

#create some text

fnt=("times",40 ,"bold italic")
w.create_text(800 ,100 ,text = "WELCOME TO THE WORLD" , font =fnt ,fill="blue")

#create a polygon

points =[150,100,200,120,240,180,210,200,150,150,100,200]
w.create_polygon(points,outline="yellow",width=3)

#To add canvas to the oot window
w.pack()

mainloop()