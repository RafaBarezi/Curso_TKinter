print("\nHello world tkinter\n")

# importando tkinter:
from tkinter import * 

# Tk atribui uma instância de tk:
janela = Tk() 
janela.title("Janela principal")
# gerenciador layout pack:
Label(janela, text = "Hello world!").pack() 
# Para fazer a aplicação ser executada:
janela.mainloop() 