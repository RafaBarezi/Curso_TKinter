print("\nGerenciador de layout place\n")

from tkinter import *

# Tk é uma classe. Classes devem iniciar com maiúsculo:
janela = Tk() 

Lb = Label(janela, text = "conteúdo da janela")
Lb.place(x=500, y=260) 

janela.geometry("1200x520+0+0")
janela.mainloop()