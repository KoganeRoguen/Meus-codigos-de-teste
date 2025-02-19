import random
import tkinter as tk
from tkinter import Tk, Label, Button, messagebox, ttk

# Função para centralizar a janela
def centraliza_janela(janela, largura, altura):
    # Obtém as dimensões da tela
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    
    # Calcula a posição x e y para centralizar a janela
    x = (screen_width // 2) - (largura // 2)
    y = (screen_height // 2) - (altura // 2)
    
    # Define a geometria da janela
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

root = Tk()
root.title("Gerador de Nome")

# Define as dimensões da janela
largura_janela = 400
altura_janela = 300

# Chama a função para centralizar a janela
centraliza_janela(root, largura_janela, altura_janela   )

v = ['a','e','i','o','u', 'y']
c = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']

info_label = Label(root, text='Clique no botão abaixo para gerar um nome', justify='center')
info_label.pack()

# Função para que a caixinha de entrada aceite apenas dígitos numéricos
def valida_num(char):
    return char.isdigit() # Permite apenas dígitos

vcmd = (root.register(valida_num), '%S')

# Faz uma caixinha de entrada
label_num_caracteres = tk.Entry(root, width=3, validate='key', validatecommand=vcmd)
label_num_caracteres.pack(pady=10)
def gerar_nome():
    # Obtém o número de caracteres da entrada
    try:
        n = int(label_num_caracteres.get())
        if n <= 2:
            messagebox.showerror('Erro', 'É válido apenas 3 ou mais caracteres. Tente novamente')
            return
        elif n > 10:
            messagebox.showerror('Erro', 'Um nome com mais de 10 caracteres é muito grande. Tente algo mais curto')
            return
    except ValueError:
        messagebox.showerror('Erro', 'Favor, inserir um valor.')
        return
    
    # Gerar o nome
    nome = random.choice(v) + random.choice(c)
    for _ in range(n - 2):
        if nome[-1] in v:
            nome += random.choice(c)
        else:
            nome += random.choice(v)
            
    info_label.config(text=f'O nome gerado foi: {nome}!')
    
# Centraliza o botão e todos os elementos da janela
generate_button = Button(root, text='Gerar Nome', command=gerar_nome)
generate_button.pack(pady=10)

for widget in [info_label, label_num_caracteres, generate_button]:
    widget.pack(side='top', pady=10)

root.mainloop()