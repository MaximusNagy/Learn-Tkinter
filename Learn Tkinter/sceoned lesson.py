from tkinter import *

# lable = an area widget that holds text and/or an image within a window

Window = Tk()

photo = PhotoImage(file="D:\Python\Learn Tkinter\logo.png")

label =Label(Window,text="Hello",
             font=('Arial',40,'bold'), 
             fg='green',bg='black',
             relief=RAISED,
             bd=10,
             padx=20,
             pady=20)
label.pack()
# label.place(x=0,y=0)


Window.mainloop()