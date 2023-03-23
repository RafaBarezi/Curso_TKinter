print("\nExtraindo valores do widget entry\n")

from tkinter import *

def bt_onclick():
    # O que eu digitar na entrada vai aparecer no prompt:
    print(edit.get())

janela = Tk()
janela.title("Janela principal")
janela["bg"] = "black"

# Entry é o componente que nos permite informar entradas de valores:
edit = Entry(janela, width=16, background="grey")
edit.place(x=480, y=150)

bt = Button(janela, width=16, text="O botão aparece aqui", command=bt_onclick)
bt.place(x=470, y=250)

lb = Label(janela, text="Este é o label")
lb.place(x=490, y=350)

janela.geometry("1200x700+0+0")
janela.mainloop()
