print("\nEntrada e processamento de dados\n")

from tkinter import *

janela = Tk()

def bt_click():
    print("Clicou no botão")

    # Usamos o isnumeric para confirmar se a variável se trata de um número:

    if(str(edit1.get()).isnumeric() and str(edit2.get()).isnumeric()): 
        num1 = int(edit1.get())
        num2 = int(edit2.get())
        lb["text"] = num1+num2
    else:
        lb["text"] = " Valores informados inválidos"

edit1 = Entry(janela, width=20)
edit1.place(x=450, y=150)
edit2 = Entry(janela, width=20)
edit2.place(x=450, y=180)

bt = Button(janela, text="SOMA", width=16, command=bt_click)
bt.place(x=450, y=230)

lb = Label(janela, text="Resultado")
lb.place(x=490, y=270)

janela.geometry("1200x700+0+0")
janela.mainloop()