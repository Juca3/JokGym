import datetime
import functools
import tkinter as tk
from tkinter import font
from tkinter import PhotoImage

def salvar_anotacoes(texto):
    with open("anotacoes.txt", "w") as arquivo:
        arquivo.write(texto)

def carregar_anotacoes():
    try:
        with open("anotacoes.txt", "r") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return ""

def mostrar_relogio(label_relogio):
    agora = datetime.datetime.now()
    hora_atual = agora.strftime("%H:%M:%S")
    label_relogio.config(text=f"Relógio: {hora_atual}")
    label_relogio.after(1000, lambda: mostrar_relogio(label_relogio))

def abrir_Menu(janela):
    for widget in janela.winfo_children():
        widget.pack_forget()

    largura = 1360
    altura = 768
    nova_tela = tk.Frame(janela, bg="beige", width=largura, height=altura)
    nova_tela.pack(fill="both", expand=True)

    centro_frame = tk.Frame(nova_tela, bg="beige")
    centro_frame.place(relx=0.5, rely=0.5, anchor="center")

    fonte_botao = font.Font(size=15, weight="bold")
    botao1 = tk.Button(centro_frame, text="Home", font=fonte_botao, width=20, height=3, command=functools.partial(home, janela))
    botao2 = tk.Button(centro_frame, text="Perfil", font=fonte_botao, width=20, height=3, command=functools.partial(perfil, janela))
    botao3 = tk.Button(centro_frame, text="Relatório", font=fonte_botao, width=20, height=3, command=functools.partial(relatorio, janela))
    
    botao1.pack(pady=10)
    botao2.pack(pady=10)
    botao3.pack(pady=10)

# 3 Telas

def home(janela):
    for widget in janela.winfo_children():
        widget.destroy()

    janela.update()

    cor_de_fundo_janela = "orange"
    janela.configure(bg=cor_de_fundo_janela)

    cor_de_fundo_janela = "orange"
    janela.configure(bg=cor_de_fundo_janela)

    # Largura e altura máximas para evitar que a janela cresça demais
    largura_maxima = 1360
    altura_maxima = 768
    janela.maxsize(width=largura_maxima, height=altura_maxima)

    fonte_personalizada = font.Font(family="Helvetica", size=15, weight="bold")
    fonte_personalizada2 = font.Font(family="Helvetica", size=12, weight="bold")

    imagem_perfil = PhotoImage(file="Perfil.png")

    # Lateral Esquerda (Coluna 1)
    frame_col1 = tk.Frame(janela, bg="orange")
    frame_col1.pack(side="left", fill="both", expand=True)

    # Menu, Foto de Perfil e Título (Linha 1)
    frame_col1_linha1 = tk.Frame(frame_col1, bg="orange")
    frame_col1_linha1.pack(padx=20, pady=20)

    botao_perfil = tk.Button(frame_col1_linha1, text="...", bg="orange", font=fonte_personalizada2, command=lambda: abrir_Menu(janela))
    botao_perfil.pack(side="left", padx=10, pady=10)

    label_icon = tk.Label(frame_col1_linha1, image=imagem_perfil, bg="orange")
    label_icon.pack(side="left")

    label = tk.Label(frame_col1_linha1, text="Olá Joaquim, o que faremos hoje?", bg="orange", font=fonte_personalizada)
    label.pack(side="left", padx=10, pady=10)

    # Caixa de Texto e Título (Linha 2)
    frame_col1_linha2 = tk.Frame(frame_col1, bg="orange")
    frame_col1_linha2.pack(padx=20, pady=20)

    label_titulo2 = tk.Label(frame_col1_linha2, text="Anotações", bg="orange", font=fonte_personalizada)
    label_titulo2.pack(side="top", padx=10, pady=5)

    texto_anotacoes = carregar_anotacoes()

    caixa_texto = tk.Text(frame_col1_linha2, bg="black", fg="white", font=fonte_personalizada, width=45, height=12)
    caixa_texto.insert("1.0", texto_anotacoes)
    caixa_texto.pack(side="top", padx=10, pady=5)

    # Lateral Direita (Coluna 2)
    frame_col2 = tk.Frame(janela, bg="orange")
    frame_col2.pack(side="right", fill="both", expand=True, pady=50)  # Adicione o pady aqui

    # Horário (Linha 1)
    frame_col2_linha1 = tk.Frame(frame_col2, bg="orange")
    frame_col2_linha1.pack(padx=20, pady=20)

    label_horario = tk.Label(frame_col2_linha1, text=" ", bg="orange", font=fonte_personalizada2)
    label_horario.pack()

    # Label para exibir o relógio
    label_relogio = tk.Label(frame_col2_linha1, text="", bg="orange", font=fonte_personalizada2)
    label_relogio.pack()

    # Atualizar o relógio a cada segundo
    mostrar_relogio(label_relogio)

    def on_day_click(event, texto):
        label_dia = event.widget
        if label_dia.cget("text") != texto:
            label_dia.config(text=texto)
        else:
            label_dia.config(text=label_dia.dia_original)

    # Dias da Semana e Título (Linha 2)
    frame_col2_linha2 = tk.Frame(frame_col2, bg="orange")
    frame_col2_linha2.pack(padx=20, pady=30)

    label_titulo3 = tk.Label(frame_col2_linha2, text="Treinos da Semana", bg="orange", font=fonte_personalizada)
    label_titulo3.pack(side="top", padx=15, pady=10)

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
    for dia in dias_semana:
        label_dia = tk.Label(frame_col2_linha2, text=dia, bg="orange", font=fonte_personalizada2)
        label_dia.pack(side="top", padx=15, pady=5)
        label_dia.dia_original = dia
        label_dia.bind("<Button-1>", functools.partial(on_day_click, texto=dias_textos[dia]))

    # Botões (Linha 3)
    frame_col2_linha3 = tk.Frame(frame_col2, bg="orange")
    frame_col2_linha3.pack(padx=20, pady=20)

    # Título
    label_titulo_opcoes = tk.Label(frame_col2_linha3, text="Opções de Treino", bg="orange", font=fonte_personalizada)
    label_titulo_opcoes.pack(side="top", padx=10, pady=5)

    botao1 = tk.Button(frame_col2_linha3, text="Treinos da Semana", bg="orange", font=fonte_personalizada2, command=lambda: treino_semana(janela))
    botao1.pack(side="left", padx=10, pady=10)

    botao2 = tk.Button(frame_col2_linha3, text="Treino Livre", bg="orange", font=fonte_personalizada2, command=lambda: treino_livre(janela))
    botao2.pack(side="left", padx=10, pady=10)

    def fechar_janela():
        texto = caixa_texto.get("1.0", tk.END)
        salvar_anotacoes(texto)
        janela.destroy()

    janela.protocol("WM_DELETE_WINDOW", fechar_janela)

    janela.mainloop()

def perfil(janela):
    for widget in janela.winfo_children():
        widget.destroy()

    janela.update()

    # Definir cor de fundo
    cor_de_fundo_janela = "orange"
    janela.configure(bg=cor_de_fundo_janela)

    largura = 1360
    altura = 768
    janela.geometry(f"{largura}x{altura}+100+100")

    fonte_personalizada = font.Font(family="Helvetica", size=15, weight="bold")
    fonte_personalizada2 = font.Font(family="Helvetica", size=12, weight="bold")

    frame = tk.Frame(janela, bg="orange")
    frame.pack(side="top", anchor="w", padx=20, pady=20)

    botao_perfil = tk.Button(frame, text="...", bg="orange", font=fonte_personalizada2, command=lambda: abrir_Menu(janela))
    botao_perfil.pack(side="left", padx=10)

    label = tk.Label(frame, text="Perfil", bg="orange", font=fonte_personalizada)
    label.pack(side="top", padx=10)

    quadrado_frame = tk.Frame(janela, bg="beige", width=100, height=altura)
    quadrado_frame.pack_forget()

    def fechar_janela():
        janela.destroy()

    janela.protocol("WM_DELETE_WINDOW", fechar_janela)

def relatorio(janela):
    for widget in janela.winfo_children():
        widget.destroy()

    janela.update()

    # Definir cor de fundo
    cor_de_fundo_janela = "orange"
    janela.configure(bg=cor_de_fundo_janela)

    largura = 1360
    altura = 768
    janela.geometry(f"{largura}x{altura}+100+100")

    fonte_personalizada = font.Font(family="Helvetica", size=15, weight="bold")
    fonte_personalizada2 = font.Font(family="Helvetica", size=12, weight="bold")

    frame = tk.Frame(janela, bg="orange")
    frame.pack(side="top", anchor="w", padx=20, pady=20)

    botao_perfil = tk.Button(frame, text="...", bg="orange", font=fonte_personalizada2, command=lambda: abrir_Menu(janela))
    botao_perfil.pack(side="left", padx=10)

    label = tk.Label(frame, text="Relatório", bg="orange", font=fonte_personalizada)
    label.pack(side="top", padx=10)

    quadrado_frame = tk.Frame(janela, bg="beige", width=100, height=altura)
    quadrado_frame.pack_forget()

    def fechar_janela():
        janela.destroy()

    janela.protocol("WM_DELETE_WINDOW", fechar_janela)

# Treino da Semana

def treino_semana(janela):
    for widget in janela.winfo_children():
        widget.destroy()

    janela.update()

    # Definir cor de fundo
    cor_de_fundo_janela = "orange"
    janela.configure(bg=cor_de_fundo_janela)

    largura = 1360
    altura = 768
    janela.geometry(f"{largura}x{altura}+100+100")

    fonte_personalizada = font.Font(family="Helvetica", size=15, weight="bold")
    fonte_personalizada2 = font.Font(family="Helvetica", size=12, weight="bold")

    frame = tk.Frame(janela, bg="orange")
    frame.pack(side="top", anchor="w", padx=20, pady=20)

    botao_treino_semana = tk.Button(frame, text="Voltar", bg="orange", font=fonte_personalizada2, command=lambda: home(janela))
    botao_treino_semana.pack(side="left", padx=10)

    label = tk.Label(frame, text="Treinos da Semana", bg="orange", font=fonte_personalizada)
    label.pack(side="top", padx=10)

    # Criar um novo frame para os botões no meio da tela
    frame_botoes = tk.Frame(janela, bg="orange")
    frame_botoes.pack(fill="both", expand=True)

    # Lista de dias da semana
    dias_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

    # Encontrar o tamanho máximo dos dias da semana para definir como tamanho mínimo dos botões
    tamanho_maximo = max(len(dia) for dia in dias_semana)

    # Criar botões com o mesmo tamanho mínimo
    for dia in dias_semana:
        botao_dia = tk.Button(frame_botoes, bg="orange", text=dia, font=fonte_personalizada2, width=tamanho_maximo)
        botao_dia.config(command=lambda dia=dia: mostrar_treino_dia(dia))  # Atualiza o texto do label com os detalhes do treino
        botao_dia.pack(pady=10)

    # Criar um Label para exibir os detalhes do treino
    global label_detalhes
    label_detalhes = tk.Label(janela, text="", bg="orange", font=fonte_personalizada)
    label_detalhes.pack(padx=20, pady=20)

    def fechar_janela():
        janela.destroy()

    janela.protocol("WM_DELETE_WINDOW", fechar_janela)

def obter_detalhes_treino(dia):

    detalhes_treinos = {
    "Domingo": "Descanso",
    "Segunda": "Treino de peito e tríceps",
    "Terça": "Treino de costas e bíceps",
    "Quarta": "Treino de pernas",
    "Quinta": "Treino de ombros",
    "Sexta": "Treino de abdômen",
    "Sábado": "Descanso"
    }

    return detalhes_treinos.get(dia, "Treino não definido para este dia")

def mostrar_treino_dia(dia):
    global label_detalhes
    for widget in janela.winfo_children():
        widget.destroy()

    janela.update()

    detalhes = obter_detalhes_treino(dia)

    # Definir cor de fundo
    cor_de_fundo_janela = "orange"
    janela.configure(bg=cor_de_fundo_janela)

    largura = 1360
    altura = 768
    janela.geometry(f"{largura}x{altura}+100+100")

    fonte_personalizada = font.Font(family="Helvetica", size=15, weight="bold")
    fonte_personalizada2 = font.Font(family="Helvetica", size=12, weight="bold")

    frame = tk.Frame(janela, bg="orange")
    frame.pack(side="top", anchor="w", padx=20, pady=20)

    botao_perfil = tk.Button(frame, text="Voltar", bg="orange", font=fonte_personalizada2, command=lambda: treino_semana(janela))
    botao_perfil.pack(side="left", padx=10)

    label = tk.Label(frame, text=f"Detalhes do treino para {dia}: {detalhes}", bg="orange", font=fonte_personalizada)
    label.pack(side="right", anchor="center", fill="both", expand=True)

    quadrado_frame = tk.Frame(janela, bg="beige", width=100, height=altura)
    quadrado_frame.pack_forget()

    def fechar_janela():
        janela.destroy()

    janela.protocol("WM_DELETE_WINDOW", fechar_janela)

# Treino Livre

def treino_livre(janela):
    for widget in janela.winfo_children():
        widget.destroy()

    janela.update()

    # Definir cor de fundo
    cor_de_fundo_janela = "orange"
    janela.configure(bg=cor_de_fundo_janela)

    largura = 1360
    altura = 768
    janela.geometry(f"{largura}x{altura}+100+100")

    fonte_personalizada = font.Font(family="Helvetica", size=15, weight="bold")
    fonte_personalizada2 = font.Font(family="Helvetica", size=12, weight="bold")

    frame = tk.Frame(janela, bg="orange")
    frame.pack(side="top", anchor="w", padx=20, pady=20)

    botao_treino_livre = tk.Button(frame, text="Voltar", bg="orange", font=fonte_personalizada2, command=lambda: home(janela))
    botao_treino_livre.pack(side="left", padx=10)

    label = tk.Label(frame, text="Treino Livre", bg="orange", font=fonte_personalizada)
    label.pack(side="top", padx=10)

    # Criar um novo frame para os botões no meio da tela
    frame_botoes = tk.Frame(janela, bg="orange")
    frame_botoes.pack(fill="both", expand=True)

    # Lista de dias da semana
    grupo_muscular = ["Peito", "Costas", "Tríceps", "Bíceps", "Antebraços", "Abdômen", "Oblíquos", "Perna"]

    # Encontrar o tamanho máximo dos dias da semana para definir como tamanho mínimo dos botões
    tamanho_maximo = max(len(musculo) for musculo in grupo_muscular)

    # Criar botões com o mesmo tamanho mínimo
    for musculo in grupo_muscular:
        botao_dia = tk.Button(frame_botoes, bg="orange", text=musculo, font=fonte_personalizada2, width=tamanho_maximo)
        botao_dia.config(command=lambda musculo=musculo: mostrar_treino_livre(musculo))  # Atualiza o texto do label com os detalhes do treino
        botao_dia.pack(pady=10)

    # Criar um Label para exibir os detalhes do treino
    global label_detalhes
    label_detalhes = tk.Label(janela, text="", bg="orange", font=fonte_personalizada)
    label_detalhes.pack(padx=20, pady=20)

    def fechar_janela():
        janela.destroy()

    janela.protocol("WM_DELETE_WINDOW", fechar_janela)

def mostrar_treino_livre(musculo):
    global label_detalhes
    for widget in janela.winfo_children():
        widget.destroy()

    janela.update()

    musculo = (musculo)

    # Definir cor de fundo
    cor_de_fundo_janela = "orange"
    janela.configure(bg=cor_de_fundo_janela)

    largura = 1360
    altura = 768
    janela.geometry(f"{largura}x{altura}+100+100")

    fonte_personalizada = font.Font(family="Helvetica", size=15, weight="bold")
    fonte_personalizada2 = font.Font(family="Helvetica", size=12, weight="bold")

    frame = tk.Frame(janela, bg="orange")
    frame.pack(side="top", anchor="w", padx=20, pady=20)

    botao_perfil = tk.Button(frame, text="Voltar", bg="orange", font=fonte_personalizada2, command=lambda: treino_livre(janela))
    botao_perfil.pack(side="left", padx=10)

    label = tk.Label(frame, text=f"Treino de {musculo}", bg="orange", font=fonte_personalizada)
    label.pack(side="top", anchor="w")

    quadrado_frame = tk.Frame(janela, bg="beige", width=100, height=altura)
    quadrado_frame.pack_forget()

    def fechar_janela():
        janela.destroy()

    janela.protocol("WM_DELETE_WINDOW", fechar_janela)

# Loop

if __name__ == "__main__":
    janela = tk.Tk()
    janela.title("JokGym")
    home(janela)