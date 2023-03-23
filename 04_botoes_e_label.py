print("\nBotões e labels\n")

from tkinter import *

def bt_click(): 
    print("bt_click")
    # Quando clicamos no botão a propriedade do label é alterada para exibir a informação. Este é o label do click:
    lb["text"] = "O botão foi clicado !"    
    lb.place(x=463, y=350) 

janela = Tk()
janela.title("Janela principal")
janela["bg"] = "blue"
janela.geometry("1200x700+0+0")

bt = Button(janela, width = 20, text= "Conteúdo do botão", command= bt_click)
bt.place(x=450, y=200)

lb = Label(janela, text= "Label")
lb.place(x=510, y=250)

janela.mainloop()