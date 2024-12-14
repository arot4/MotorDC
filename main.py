from tkinter import Tk , Label, Canvas, messagebox  
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("800x600")
ventana.title("GUI Dirección de Motor DC")
ventana.iconbitmap("img/motor.ico")
titulo = Label(ventana, text="Control Motor DC", font=("Arial", 20, "bold"))
titulo.pack()

ventana.mainloop()