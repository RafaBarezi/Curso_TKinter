print("\nCódigo mínimo\n")

# import tkinter
# janela = tkinter.Tk # teria o mesmo efeito das linhas abaixo:

import tkinter as tk 

# tk retorna a instância da janela principal:
janela = tk.Tk() 
janela.title("Janela principal")
# bg de background. Usamos para definir a cor de fundo
# Podemos definir assim também: janela["background"] = "white":
janela["bg"] = "blue"   
# largura x altura + distância da esquerda + distância do topo / Distância da margem da tela (wxh+l+t):
janela.geometry("1200x550+0+0")
# janela principal, fica em um laço de repetição infinito para detectar as modificações na janela e disparar os efeitos:
janela.mainloop() 