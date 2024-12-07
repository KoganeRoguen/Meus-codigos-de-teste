import os
import random
from tkinter import Tk, Label, Button, Toplevel
from tkinter import ttk

# Função para centralizar a janela
def centralizar_janela(janela):
    janela.update_idletasks()  # Atualiza as tarefas pendentes
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)

    janela.geometry(f"{largura}x{altura}+{x}+{y}")

# Interfaces
status = os.path.join(os.path.expanduser('~'), 'Documents', 'status.txt')
local = os.path.join(os.path.expanduser('~'), 'Documents', 'local.txt')

# Status do personagem
food = 100
water = 100
energia = 100
força = 10
inteligencia = 10
higiene = 100
intestino = 0
urina = 0
felicidade = 100
pao_frances = 10
garrafa_agua = 10

# Criar janela principal
root = Tk()
root.title("Status")
root.geometry("400x500")

# Centraliza a janela principal
centralizar_janela(root)

# Labels e barras de status do personagem
status_label = Label(root, text='Nome: Jogador')
status_label.pack()

# Função para criar uma barra com rótulo
def create_status_bar(label_text, initial_value):
    label = Label(root, text=label_text)
    label.pack()
    bar = ttk.Progressbar(root, length=300, mode='determinate')
    bar['value'] = initial_value
    bar.pack(pady=5)
    return bar

# Criar barras de status
food_bar = create_status_bar('Alimentação', food)
water_bar = create_status_bar('Hidratação', water)
energia_bar = create_status_bar('Energia (sono)', energia)
higiene_bar = create_status_bar('Higienização', higiene)
intestino_bar = create_status_bar('Intestino', intestino)
urina_bar = create_status_bar('Bexiga', urina)
felicidade_bar = create_status_bar('Felicidade', felicidade)

# Mostrar força e inteligência
forca_label = Label(root, text=f'Força: {força}')
forca_label.pack()

inteligencia_label = Label(root, text=f'Inteligência: {inteligencia}')
inteligencia_label.pack()

# Variáveis para rastrear se as janelas estão abertas
locais_aberto = False
casa_aberto = False
gela_aberta = False

def update_status():
    food_bar['value'] = food
    water_bar['value'] = water
    energia_bar['value'] = energia
    higiene_bar['value'] = higiene
    intestino_bar['value'] = intestino
    urina_bar['value'] = urina
    felicidade_bar['value'] = felicidade

# Janela para os locais
def open_locais():
    global locais_aberto
    if not locais_aberto:
        locais_aberto = True
        locais_window = Toplevel(root)
        locais_window.title("Locais")
        locais_window.geometry("300x250")
        centralizar_janela(locais_window)  # Centraliza a janela de locais
        
        # Botões para os locais
        casa_button = Button(locais_window, text='Casa', command=open_casa_options)
        casa_button.pack(pady=10)

        mercado_button = Button(locais_window, text='Mercearinha', command=lambda: print("Mercado selecionado"))
        mercado_button.pack(pady=10)

        escola_button = Button(locais_window, text='Escola', command=lambda: print("Escola selecionada"))
        escola_button.pack(pady=10)

        hospital_button = Button(locais_window, text='Hospital', command=lambda: print("Hospital selecionado"))
        hospital_button.pack(pady=10)

        locais_window.protocol("WM_DELETE_WINDOW", close_locais)  # Adiciona fechamento da janela

def close_locais(): 
    global locais_aberto
    locais_aberto = False
    # Pode fazer outras ações necessárias ao fechar

# Função para abrir as opções da casa
def open_casa_options():
    global casa_aberto
    if not casa_aberto:
        casa_aberto = True
        casa_window = Toplevel(root)
        casa_window.title("Casa")
        casa_window.geometry("400x300")
        
        # Botões para ações na casa
        Button(casa_window, text='Abrir geladeira', command=open_fridge_options).pack(pady=10)
        Button(casa_window, text='Dormir', command=go_to_sleep).pack(pady=10)
        Button(casa_window, text='Banheiro', command=use_bathroom_options).pack(pady=10)
        Button(casa_window, text='Ler Livro escolar', command=read_book).pack(pady=10)
        Button(casa_window, text='Desenhar com lápis', command=draw).pack(pady=10)

        casa_window.protocol("WM_DELETE_WINDOW", close_casa)  # Adiciona fechamento da janela

def close_casa():
    global casa_aberto
    casa_aberto = False
    # Pode fazer outras ações necessárias ao fechar

# Lógica para abrir a geladeira
def open_fridge_options():
    global gela_aberta
    if not gela_aberta:
        gela_aberta = True    
        geladeira_window = Toplevel(root)
        geladeira_window.title("Geladeira")
        geladeira_window.geometry("400x300")
        centralizar_janela(geladeira_window)
        
    # Número de produtos na geladeira
    global pf_gela
    pf_gela = Label(geladeira_window, text=f'Pão Francês: {pao_frances}')
    pf_gela.pack()
    
    global ga_gela
    ga_gela = Label(geladeira_window, text=f"Garrafa D'agua: {garrafa_agua}")
    ga_gela.pack()
    
    # Botões para ações na geladeira
    Button(geladeira_window, text='Beber Água', command=drink_water).pack(pady=10)
    Button(geladeira_window, text='Comer Pão Francês', command=eat_bread).pack(pady=10)
    
    geladeira_window.protocol("WM_DELETE_WINDOW", close_casa)
    
def close_gela():
    global gela_aberta
    gela_aberta = False
    
def drink_water():
    # Lógica para beber água
    global water, urina, garrafa_agua, ga_gela
    if garrafa_agua > 0:
        if water < 100:
            garrafa = 15
            water = min(100, water + garrafa)
            bexiga = random.randint(5, 15)
            urina = min(100, urina + bexiga)
            garrafa_agua -= 1
            ga_gela.config(text=f"Garrafa D'agua: {garrafa_agua}")
            update_status()
            dw_window = Toplevel(root)
            dw_window.title('Descrição')
            dw_window.geometry('250x50')
            centralizar_janela(dw_window) # Centraliza a janela de água
            dw_label = Label(dw_window, text='Você bebeu água e matou a sede!')
            dw_label.pack()
        else:
            dw_window = Toplevel(root)
            dw_window.title('Descrição')
            dw_window.geometry('250x50')
            centralizar_janela(dw_window)
            dw_label = Label(dw_window, text='Você já está hidratado.')
            dw_label.pack()
    else:
        dw_window = Toplevel(root)
        dw_window.title('Descrição')
        dw_window.geometry('250x50')
        centralizar_janela(dw_window)
        dw_label = Label(dw_window, text='Você não tem mais água.')
        dw_label.pack()
    
def eat_bread():
    # Lógica para comer pão
    global food, intestino, water, pao_frances, pf_gela
    if pao_frances > 0:  
        if food < 100:
            pf_alimento = 15
            pao_frances -= 1
            pf_gela.config(text=f"Pão francês: {pao_frances}")
            food = min(100, food + pf_alimento)
            fezes = random.randint(5, 15)
            intestino = min(100, intestino + fezes)
            sede = random.randint(3, 7)
            water = max(0, water - sede)
            update_status()
            eb_window = Toplevel(root)
            eb_window.title('Descrição')
            eb_window.geometry('250x50')
            centralizar_janela(eb_window)
            eb_label = Label(eb_window, text='Você comeu pão francês e matou a fome!')
            eb_label.pack()
        else:
            eb_window = Toplevel(root)
            eb_window.title('Descrição')
            eb_window.geometry('250x50')
            centralizar_janela(eb_window)
            eb_label = Label(eb_window, text='Você está cheio.')
            eb_label.pack()
    else:
        eb_window = Toplevel(root)
        eb_window.title('Descrição')
        eb_window.geometry('250x50')
        centralizar_janela(eb_window)
        eb_label = Label(eb_window, text='Você está sem pão francês.')
        
def go_to_sleep():
    # Lógica para dormir
    global energia
    if energia < 100:
        energia = 100
        update_status()
        sleep_window = Toplevel(root)
        sleep_window.title('Descrição')
        sleep_window.geometry('250x50')
        centralizar_janela(sleep_window)  # Centraliza a janela de sono
        sleep_label = Label(sleep_window, text='Você dormiu e recuperou suas energias!')
        sleep_label.pack()
    else:
        sleep_window = Toplevel(root)
        sleep_window.title('Descrição')
        sleep_window.geometry('250x50')
        centralizar_janela(sleep_window)  # Centraliza a janela de descrição
        sleep_label = Label(sleep_window, text='Você não está com sono.')
        sleep_label.pack()

def use_bathroom_options():
    # Lógica para usar o banheiro
    bath_window = Toplevel(root)
    bath_window.title('Banheiro')
    bath_window.geometry('400x300')
    centralizar_janela(bath_window)
    
    Button(bath_window, text='Urinar', command=mijar).pack(pady=10)
    Button(bath_window, text='Defecar', command=cagar).pack(pady=10)
    
def mijar():
    # Lógica para mijar
    global urina
    if urina > 0:  
        if urina < 100:
            urina = 0
            update_status
            urina_window = Toplevel(root)
            urina_window.title('Descrição')
            urina_window.geometry('250x50')
            centralizar_janela(urina_window)
            urina_label = Label(urina_window, text='Você Mijou!')
            urina_label.pack()
    else:
        urina_window = Toplevel(root)
        urina_window.title('Descrição')
        urina_window.geometry('250x50')
        centralizar_janela(urina_window)
        urina_label = Label(urina_window, text='Você está com a bexiga vazia.')
        urina_label.pack()
    update_status()
    
def cagar():
    # Lógica para cagar
    global intestino
    if intestino > 0:
        if intestino < 100:
            intestino = 0
            update_status
            intestino_window = Toplevel(root)
            intestino_window.title('Descrição')
            intestino_window.geometry('250x50')
            centralizar_janela(intestino_window)
            intestino_label = Label(intestino_window, text='Você Cagou!')
            intestino_label.pack()
    else:
        intestino_window = Toplevel(root)
        intestino_window.title('Descrição')
        intestino_window.geometry('250x50')
        centralizar_janela(intestino_window)
        intestino_label = Label(intestino_window, text='Você não está com vontade.')
        intestino_label.pack()
    update_status()
        
def read_book():
    # Lógica para ler um livro
    global inteligencia, energia, felicidade, water, food, intestino
    aumento = random.randint(5, 10)
    perda = random.randint(5, 15)
    tristeza = random.randint(3, 7)
    sede = random.randint(1, 3)
    fome = 1
    fezes = 1
    inteligencia = min(100, inteligencia + aumento)  # Aumenta a inteligência, não passando de 100
    energia = max(0, energia - perda) # Diminui a energia, não negativando o valor
    felicidade = max(0, felicidade - tristeza) # Diminui a felicidade, não negativando o valor
    water = max(0, water - sede) # Diminui a hidratação, não negativando o valor
    food = max(0, food - fome) # Diminui a hidratação, não negativando o valor
    intestino = min(100, intestino + fezes) # Aumenta a vontade de cagar
    # Atualiza o rótulo de inteligência na janela principal
    inteligencia_label.config(text=f'Inteligência: {inteligencia}')
    
    update_status()
    
    read_window = Toplevel(root)
    read_window.title('Descrição')
    read_window.geometry('250x50')
    centralizar_janela(read_window)  # Centraliza a janela de leitura
    read_label = Label(read_window, text=f'Você leu o livro e aumentou sua inteligência!')
    read_label.pack()

def draw():
    # Lógica para desenhar
    update_status()

# Botão para abrir a janela com as opções de locais
open_locais_button = Button(root, text="Locais", command=open_locais)
open_locais_button.pack(pady=10)

# Atualiza o status no início
update_status()

# Loop principal da interface
root.mainloop()