from tkinter import *

ventana = Tk()

ventana.geometry("800x500")

ventana.resizable(0,0)

ventana.config(bg="black")

frame_red= Frame(ventana)
frame_red.config(bg="red3", width=780, height=480)
frame_red.place(x=10, y=10)

frame_white= Frame(ventana)
frame_white.config(bg="white", width=100, height=480)
frame_white.place (x=220 , y=10)

frame_white2= Frame(ventana)
frame_white2.config(bg="white", width=780, height=100)
frame_white2.place (x=10 , y=200)

frame_blue= Frame(ventana)
frame_blue.config(bg="blue4", width=70, height=480)
frame_blue.place (x=235 , y=10)

frame_blue2= Frame(ventana)
frame_blue2.config(bg="blue4", width=780, height=70)
frame_blue2.place (x=10 , y=215)

ventana.mainloop()