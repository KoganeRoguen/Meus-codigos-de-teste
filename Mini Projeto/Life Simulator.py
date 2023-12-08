import os
from tkinter import Tk, Label, Button, Toplevel

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

# Geladeira
comida = 10
água = 10

# Informar o seu nome
name = input('\n> Informe o seu nome: ')

# Criar janela principal
root = Tk()
root.title("Status")
root.geometry("400x300")

# Labels com status do personagem
status_label = Label(root, text=f'''
Nome: {name}
____________________
> Alimentação [{food}%]
> Hidratação [{water}%]
> Energia(sono) [{energia}%]
> Força {força}
> Inteligência {inteligencia}
> Higienização [{higiene}%]
> Intestino [{intestino}%]
> Bexiga [{urina}%]
> Felicidade [{felicidade}%]
''')
status_label.pack()

# Função para atualizar status
def update_status():
    status_label.config(text=f'''
Nome: {name}
____________________
> Alimentação [{food}%]
> Hidratação [{water}%]
> Energia(sono) [{energia}%]
> Força {força}
> Inteligência {inteligencia}
> Higienização [{higiene}%]
> Intestino [{intestino}%]
> Bexiga [{urina}%]
> Felicidade [{felicidade}%]
''')

# Janela para as opções do local
def open_local_options():
    local_window = Toplevel(root)
    local_window.title("Casa")
    local_window.geometry("400x300")
    abrir_geladeira_button = Button(local_window, text='Abrir geladeira', command=open_fridge)
    abrir_geladeira_button.pack()
    dormir_button = Button(local_window, text='Dormir', command=go_to_sleep)
    dormir_button.pack()
    usar_banheiro_button = Button(local_window, text='Usar o banheiro', command=use_bathroom)
    usar_banheiro_button.pack()
    ler_livro_button = Button(local_window, text='Ler Livro escolar', command=read_book)
    ler_livro_button.pack()
    desenhar_button = Button(local_window, text='Desenhar com lápis', command=draw)
    desenhar_button.pack()

# Lógica para as ações de cada botão
def open_fridge():
    # Lógica para abrir a geladeira
    update_status()

def go_to_sleep():
    # Lógica para dormir
    global energia
    energia = 100
    update_status()
    sleep_window = Toplevel(root)
    sleep_window.title('Descrição')
    sleep_window.geometry('250x50')
    sleep_label = Label(sleep_window, text='Você dormiu e recuperou suas energias')
    sleep_label.pack()
    
def use_bathroom():
    # Lógica para usar o banheiro
    update_status()

def read_book():
    # Lógica para ler um livro
    update_status()

def draw():
    # Lógica para desenhar
    update_status()

# Botão para abrir a janela com as opções do local
open_local_button = Button(root, text="Local", command=open_local_options)
open_local_button.pack()

# Loop principal da interface
root.mainloop()
