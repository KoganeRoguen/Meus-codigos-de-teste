import subprocess,random,time,os

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

with open(status, 'w') as file:
    content = f'''____________________

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
'''
    file.write(content)
    subprocess.Popen(['notepad.exe', status])

with open(local, 'w') as file:
    content = f'''____________________

      = Casa =
____________________

> Abrir geladeira
> Dormir
> Usar o banheiro
> Ler Livro escolar
> Desenhar com lápis
'''
    file.write(content)
    subprocess.Popen(['notepad.exe', local])