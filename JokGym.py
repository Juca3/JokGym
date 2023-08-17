import tkinter as tk
from tkinter import font

def jokgym():
    #Criação da home
    janela = tk.Tk()
    janela.title("JokGym")
    
    #Definir cor de fundo
    cor_de_fundo_janela = "orange"
    janela.configure(bg=cor_de_fundo_janela)

    #Tamanho
    largura = 1080
    altura = 720
    janela.geometry(f"{largura}x{altura}")

    #Fonte de texto
    fonte_personalizada = font.Font(family="Helvetica", size=12, weight="bold")

    #Frase de bem vindo
    label = tk.Label(janela, text="Olá Joaquim, o que faremos hoje?", bg="orange", font=fonte_personalizada)
    label.pack()

    #Loop
    janela.mainloop()

jokgym()