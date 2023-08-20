import tkinter as tk
from tkinter import font
from tkinter import PhotoImage

# Definir quadrado_frame como variável global
quadrado_frame = None

def toggle_quadrado():
    if quadrado_frame.winfo_ismapped():
        quadrado_frame.pack_forget()  # Ocultar o quadrado
    else:
        quadrado_frame.pack(side="left", fill="y", padx=10)  # Mostrar o quadrado

def abrir_Menu():
    toggle_quadrado()  # Chamar a função toggle_quadrado

def jokgym():
    global quadrado_frame  # Definir a variável como global

    # Criação da home
    janela = tk.Tk()
    janela.title("JokGym")
    
    # Definir cor de fundo
    cor_de_fundo_janela = "orange"
    janela.configure(bg=cor_de_fundo_janela)

    # Tamanho
    largura = 1080
    altura = 720
    janela.geometry(f"{largura}x{altura}+100+100")  # Ajustar a posição da janela

    # Fonte de texto
    fonte_personalizada = font.Font(family="Helvetica", size=15, weight="bold")
    fonte_personalizada2 = font.Font(family="Helvetica", size=12, weight="bold")  # Definir a fonte aqui

    # Carregar imagem do ícone de perfil
    imagem_perfil = PhotoImage(file="Perfil.png")

    # Frase de boas-vindas e ícone
    frame = tk.Frame(janela, bg="orange")
    frame.pack(side="top", anchor="w", padx=20, pady=20)

    # Botão de Menu
    botao_perfil = tk.Button(frame, text="...", bg="orange", font=fonte_personalizada2, command=abrir_Menu)
    botao_perfil.pack(side="left", padx=10)

    label_icon = tk.Label(frame, image=imagem_perfil, bg="orange")
    label_icon.pack(side="left")

    # Frase de boas-vindas
    label = tk.Label(frame, text="Olá Joaquim, o que faremos hoje?", bg="orange", font=fonte_personalizada)
    label.pack(side="left", padx=10)

    # Quadrado na lateral da tela
    quadrado_frame = tk.Frame(janela, bg="blue", width=100)
    quadrado_frame.pack_forget()  # Ocultar o quadrado inicialmente

    def on_day_click(event, texto):
        label_dia = event.widget
        if label_dia.cget("text") != texto:
            label_dia.config(text=texto)
        else:
            label_dia.config(text=label_dia.dia_original)

    # Dias da semana
    frame_dias = tk.Frame(janela, bg="orange")
    frame_dias.pack(side="top", padx=10, pady=5)

    label_titulo = tk.Label(frame_dias, text="Treinos da semana", bg="orange", font=fonte_personalizada)
    label_titulo.pack(side="top", padx=10, pady=15)

    dias_textos = {
        "Domingo": "Descanso",
        "Segunda-feira": "Peito e Tríceps",
        "Terça-feira": "Costas e Bíceps",
        "Quarta-feira": "Pernas",
        "Quinta-feira": "Ombros",
        "Sexta-feira": "Abdômen",
        "Sábado": "Descanso"
    }

    dias_semana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]
    label_dias = []
    for dia in dias_semana:
        label_dia = tk.Label(frame_dias, text=dia, bg="orange", font=fonte_personalizada2)
        label_dia.pack(side="top", padx=10, pady=5)
        label_dia.dia_original = dia  # Armazena o dia original como atributo do label
        label_dia.bind("<Button-1>", lambda event, texto=dias_textos[dia]: on_day_click(event, texto))

        label_dias.append(label_dia)

    # Loop
    janela.mainloop()

jokgym()
