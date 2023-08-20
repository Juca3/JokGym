import tkinter as tk
from tkinter import font
from tkinter import PhotoImage

def jokgym():
    # Criação da home
    janela = tk.Tk()
    janela.title("JokGym")
    
    # Definir cor de fundo
    cor_de_fundo_janela = "orange"
    janela.configure(bg=cor_de_fundo_janela)

    # Tamanho
    largura = 1080
    altura = 720
    janela.geometry(f"{largura}x{altura}")

    # Fonte de texto
    fonte_personalizada = font.Font(family="Helvetica", size=15, weight="bold")

    # Fonte de texto
    fonte_personalizada2 = font.Font(family="Helvetica", size=12, weight="bold")

    # Carregar imagem do ícone de perfil
    imagem_perfil = PhotoImage(file="Perfil.png")

    # Frase de boas-vindas e ícone
    frame = tk.Frame(janela, bg="orange")
    frame.pack(side="top", anchor="w", padx=20, pady=20)

    label_icon = tk.Label(frame, image=imagem_perfil, bg="orange")
    label_icon.pack(side="left")

    # Frase de boas-vindas
    label = tk.Label(frame, text="Olá Joaquim, o que faremos hoje?", bg="orange", font=fonte_personalizada)
    label.pack(side="left", padx=10)

    def on_day_click(event, texto):
        label_dia = event.widget
        if label_dia.cget("text") != texto:
            label_dia.config(text=texto)
        else:
            label_dia.config(text=label_dia.dia_original)

    # Dias da semana
    frame = tk.Frame(janela, bg="orange")
    frame.pack(side="top", padx=10, pady=5)

    label_titulo = tk.Label(frame, text="Treinos da semana", bg="orange", font=fonte_personalizada)
    label_titulo.pack(side="top", padx=10, pady=15)

    dias_textos = {
        "Domingo": "Texto para Domingo",
        "Segunda-feira": "Texto para Segunda-feira",
        "Terça-feira": "Texto para Terça-feira",
        "Quarta-feira": "Texto para Quarta-feira",
        "Quinta-feira": "Texto para Quinta-feira",
        "Sexta-feira": "Texto para Sexta-feira",
        "Sábado": "Texto para Sábado"
    }

    dias_semana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]
    label_dias = []
    for dia in dias_semana:
        label_dia = tk.Label(frame, text=dia, bg="orange", font=fonte_personalizada2)
        label_dia.pack(side="top", padx=10, pady=5)
        label_dia.dia_original = dia  # Armazena o dia original como atributo do label
        label_dia.bind("<Button-1>", lambda event, texto=dias_textos[dia]: on_day_click(event, texto))

        label_dias.append(label_dia)

    # Loop
    janela.mainloop()

jokgym()
