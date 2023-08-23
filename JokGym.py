import tkinter as tk
from tkinter import font
from tkinter import PhotoImage

def abrir_Menu(janela):
    for widget in janela.winfo_children():
        widget.pack_forget()

    nova_tela = tk.Frame(janela, bg="beige")
    nova_tela.pack(fill="both", expand=True)

    centro_frame = tk.Frame(nova_tela, bg="beige")
    centro_frame.place(relx=0.5, rely=0.5, anchor="center")

    fonte_botao = font.Font(size=15, weight="bold")
    botao1 = tk.Button(centro_frame, text="Home", font=fonte_botao, width=20, height=3, command=lambda: home(janela))
    botao2 = tk.Button(centro_frame, text="Perfil", font=fonte_botao, width=20, height=3, command=lambda: perfil(janela))
    botao3 = tk.Button(centro_frame, text="Relatório", font=fonte_botao, width=20, height=3, command=lambda: relatorio(janela))

    botao1.pack(pady=10)
    botao2.pack(pady=10)
    botao3.pack(pady=10)

def home(janela):
    for widget in janela.winfo_children():
        widget.destroy()

    janela.update()

    # Definir cor de fundo
    cor_de_fundo_janela = "orange"
    janela.configure(bg=cor_de_fundo_janela)

    largura = 1080
    altura = 720
    janela.geometry(f"{largura}x{altura}+100+100")

    fonte_personalizada = font.Font(family="Helvetica", size=15, weight="bold")
    fonte_personalizada2 = font.Font(family="Helvetica", size=12, weight="bold")

    # Carregar imagem do ícone de perfil
    imagem_perfil = PhotoImage(file="Perfil.png")

    frame = tk.Frame(janela, bg="orange")
    frame.pack(side="top", anchor="w", padx=20, pady=20)

    botao_perfil = tk.Button(frame, text="...", bg="orange", font=fonte_personalizada2, command=lambda: abrir_Menu(janela))
    botao_perfil.pack(side="left", padx=10)

    label_icon = tk.Label(frame, image=imagem_perfil, bg="orange")
    label_icon.image = imagem_perfil  # Mantenha uma referência global para a imagem
    label_icon.pack(side="left")

    label = tk.Label(frame, text="Olá Joaquim, o que faremos hoje?", bg="orange", font=fonte_personalizada)
    label.pack(side="left", padx=10)

    quadrado_frame = tk.Frame(janela, bg="beige", width=100, height=altura)
    quadrado_frame.pack_forget()

    def on_day_click(event, texto):
        label_dia = event.widget
        if label_dia.cget("text") != texto:
            label_dia.config(text=texto)
        else:
            label_dia.config(text=label_dia.dia_original)

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
        label_dia.dia_original = dia
        label_dia.bind("<Button-1>", lambda event, texto=dias_textos[dia]: on_day_click(event, texto))

        label_dias.append(label_dia)

def perfil(janela):
    for widget in janela.winfo_children():
        widget.destroy()

    janela.update()

    # Definir cor de fundo
    cor_de_fundo_janela = "orange"
    janela.configure(bg=cor_de_fundo_janela)

    largura = 1080
    altura = 720
    janela.geometry(f"{largura}x{altura}+100+100")

    fonte_personalizada = font.Font(family="Helvetica", size=15, weight="bold")
    fonte_personalizada2 = font.Font(family="Helvetica", size=12, weight="bold")

    # Carregar imagem do ícone de perfil
    imagem_perfil = PhotoImage(file="Perfil.png")

    frame = tk.Frame(janela, bg="orange")
    frame.pack(side="top", anchor="w", padx=20, pady=20)

    botao_perfil = tk.Button(frame, text="...", bg="orange", font=fonte_personalizada2, command=lambda: abrir_Menu(janela))
    botao_perfil.pack(side="left", padx=10)

    label_icon = tk.Label(frame, image=imagem_perfil, bg="orange")
    label_icon.image = imagem_perfil  # Mantenha uma referência global para a imagem
    label_icon.pack(side="top")

    label = tk.Label(frame, text="Olá Joaquim, o que faremos hoje?", bg="orange", font=fonte_personalizada)
    label.pack(side="top", padx=10)

    quadrado_frame = tk.Frame(janela, bg="beige", width=100, height=altura)
    quadrado_frame.pack_forget()

def relatorio(janela):
    for widget in janela.winfo_children():
        widget.destroy()

    janela.update()

    # Definir cor de fundo
    cor_de_fundo_janela = "orange"
    janela.configure(bg=cor_de_fundo_janela)

    largura = 1080
    altura = 720
    janela.geometry(f"{largura}x{altura}+100+100")

    fonte_personalizada = font.Font(family="Helvetica", size=15, weight="bold")
    fonte_personalizada2 = font.Font(family="Helvetica", size=12, weight="bold")

    # Carregar imagem do ícone de perfil
    imagem_perfil = PhotoImage(file="Perfil.png")

    frame = tk.Frame(janela, bg="orange")
    frame.pack(side="top", anchor="w", padx=20, pady=20)

    botao_perfil = tk.Button(frame, text="...", bg="orange", font=fonte_personalizada2, command=lambda: abrir_Menu(janela))
    botao_perfil.pack(side="left", padx=10)

    label_icon = tk.Label(frame, image=imagem_perfil, bg="orange")
    label_icon.image = imagem_perfil  # Mantenha uma referência global para a imagem
    label_icon.pack(side="top")

    label = tk.Label(frame, text="Olá Joaquim, o que faremos hoje?", bg="orange", font=fonte_personalizada)
    label.pack(side="top", padx=10)

    quadrado_frame = tk.Frame(janela, bg="beige", width=100, height=altura)
    quadrado_frame.pack_forget()

def jokgym():
    global altura

    janela = tk.Tk()
    janela.title("JokGym")

    cor_de_fundo_janela = "orange"
    janela.configure(bg=cor_de_fundo_janela)

    largura = 1080
    altura = 720
    janela.geometry(f"{largura}x{altura}+100+100")

    fonte_personalizada = font.Font(family="Helvetica", size=15, weight="bold")
    fonte_personalizada2 = font.Font(family="Helvetica", size=12, weight="bold")

    imagem_perfil = PhotoImage(file="Perfil.png")

    frame = tk.Frame(janela, bg="orange")
    frame.pack(side="top", anchor="w", padx=20, pady=20)

    botao_perfil = tk.Button(frame, text="...", bg="orange", font=fonte_personalizada2, command=lambda: abrir_Menu(janela))
    botao_perfil.pack(side="left", padx=10)

    label_icon = tk.Label(frame, image=imagem_perfil, bg="orange")
    label_icon.pack(side="left")

    label = tk.Label(frame, text="Olá Joaquim, o que faremos hoje?", bg="orange", font=fonte_personalizada)
    label.pack(side="left", padx=10)

    quadrado_frame = tk.Frame(janela, bg="beige", width=100, height=altura)
    quadrado_frame.pack_forget()

    def on_day_click(event, texto):
        label_dia = event.widget
        if label_dia.cget("text") != texto:
            label_dia.config(text=texto)
        else:
            label_dia.config(text=label_dia.dia_original)

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
        label_dia.dia_original = dia
        label_dia.bind("<Button-1>", lambda event, texto=dias_textos[dia]: on_day_click(event, texto))

        label_dias.append(label_dia)

    janela.mainloop()

jokgym()
