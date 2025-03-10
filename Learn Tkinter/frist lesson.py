from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Maximus")
window.resizable(0,0)

icon = PhotoImage(file=r"D:\Python\Learn Tkinter\logo.png")
window.iconphoto(True,icon)
window.config(background="black")

window.mainloop() #place window on computer screen, listen for events
