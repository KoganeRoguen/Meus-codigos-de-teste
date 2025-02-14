import tkinter as tk
from tkinter import messagebox
import random

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 50  # Tamanho do jogador (quadrado)
APPLE_SIZE = PLAYER_SIZE // 2  # Metade do tamanho do jogador
PLAYER_SPEED = 10
APPLE_SPEED = 5
FPS = 60  # Frames por segundo

# Inicializa a janela principal
root = tk.Tk()
root.title("Coletor de Maçãs RPG")
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

# Cria o canvas (área de desenho)
canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg="white")
canvas.pack()

# Personagem (quadrado verde)
player = canvas.create_rectangle(
    SCREEN_WIDTH // 2 - PLAYER_SIZE // 2,
    SCREEN_HEIGHT - PLAYER_SIZE - 10,
    SCREEN_WIDTH // 2 + PLAYER_SIZE // 2,
    SCREEN_HEIGHT - 10,
    fill="green"
)

# Maçã (círculo vermelho)
apple = canvas.create_oval(
    random.randint(0, SCREEN_WIDTH - APPLE_SIZE),
    0,
    random.randint(0, SCREEN_WIDTH - APPLE_SIZE) + APPLE_SIZE,
    APPLE_SIZE,
    fill="red"
)

# Status de RPG
status = {
    "força": 1,  # Aumenta a pontuação por maçã
    "agilidade": 1,  # Aumenta a velocidade do jogador
    "sorte": 1  # Aumenta a chance de itens raros
}

# Itens coletados
inventory = {
    "Item Comum": 0,
    "Item Raro": 0,
    "Item Lendário": 0
}

# Dinheiro e contadores
score = 0
apple_count = 0  # Contador de maçãs coletadas
lootboxes = 0  # Contador de lootboxes
money = 0  # Dinheiro obtido vendendo maçãs

# Sistema Nemesis
nemesis = {
    "nome": "Inimigo Aleatório",
    "maçãs_roubadas": 0,
    "aparecer": False
}

# Curiosidades "Você Sabia?"
curiosidades = [
    "Você sabia? Maçãs são uma ótima fonte de fibras!",
    "Você sabia? O jogador mais rápido do mundo pode coletar 100 maçãs em 1 minuto!",
    "Você sabia? O talismã de sorte aumenta suas chances de ganhar lootboxes!",
    "Você sabia? O sistema Nemesis foi inspirado em Shadow of Mordor!"
]

# Label para exibir informações
score_label = tk.Label(root, text=f"Pontuação: {score} | Maçãs: {apple_count} | Lootboxes: {lootboxes} | Dinheiro: ${money}", font=("Arial", 24))
score_label.pack()

# Função para mover o personagem
def move_player(event):
    if event.keysym == "Left":
        canvas.move(player, -PLAYER_SPEED * status["agilidade"], 0)
    elif event.keysym == "Right":
        canvas.move(player, PLAYER_SPEED * status["agilidade"], 0)

# Função para mover a maçã
def move_apple():
    canvas.move(apple, 0, APPLE_SPEED)
    if canvas.coords(apple)[3] > SCREEN_HEIGHT:
        reset_apple()
    check_collision()
    root.after(1000 // FPS, move_apple)  # Controla o FPS

# Função para resetar a maçã no topo da tela
def reset_apple():
    x = random.randint(0, SCREEN_WIDTH - APPLE_SIZE)
    canvas.coords(
        apple,
        x,
        0,
        x + APPLE_SIZE,
        APPLE_SIZE
    )

# Função para verificar colisão
def check_collision():
    global score, apple_count, lootboxes
    player_coords = canvas.coords(player)
    apple_coords = canvas.coords(apple)
    # Verifica se há sobreposição entre o jogador e a maçã
    if (apple_coords[0] < player_coords[2] and apple_coords[2] > player_coords[0] and
        apple_coords[1] < player_coords[3] and apple_coords[3] > player_coords[1]):
        score += 1 * status["força"]
        apple_count += 1  # Incrementa o contador de maçãs
        if random.randint(1, 10) <= status["sorte"]:  # Chance de ganhar lootbox
            lootboxes += 1
        score_label.config(text=f"Pontuação: {score} | Maçãs: {apple_count} | Lootboxes: {lootboxes} | Dinheiro: ${money}")
        reset_apple()
        check_nemesis()  # Verifica se o Nemesis aparece

# Função para abrir lootbox
def open_lootbox():
    global lootboxes
    if lootboxes > 0:
        lootboxes -= 1
        items = ["Item Comum", "Item Raro", "Item Lendário"]
        probabilities = [70 - status["sorte"] * 5, 25 + status["sorte"] * 3, 5 + status["sorte"] * 2]  # Probabilidades ajustadas pela sorte
        item = random.choices(items, weights=probabilities, k=1)[0]
        inventory[item] += 1  # Adiciona o item ao inventário
        result_label.config(text=f"Você ganhou: {item}")
        if item == "Item Raro":
            status["força"] += 1
        elif item == "Item Lendário":
            status["sorte"] += 1
        score_label.config(text=f"Pontuação: {score} | Maçãs: {apple_count} | Lootboxes: {lootboxes} | Dinheiro: ${money}")
        update_rpg_window()  # Atualiza a janela de informações do RPG
    else:
        result_label.config(text="Você não tem lootboxes!")

# Função para abrir a janela de informações do RPG
def open_rpg_window():
    rpg_window = tk.Toplevel(root)
    rpg_window.title("Status do RPG")
    rpg_window.geometry("300x300")
    
    # Labels para exibir os status, o inventário e a curiosidade
    global status_label, inventory_label, curiosity_label
    status_label = tk.Label(rpg_window, text="", font=("Arial", 14))
    status_label.pack()
    inventory_label = tk.Label(rpg_window, text="", font=("Arial", 14))
    inventory_label.pack()
    curiosity_label = tk.Label(rpg_window, text="", font=("Arial", 12), wraplength=250)
    curiosity_label.pack()
    
    # Atualiza a janela de informações do RPG
    update_rpg_window()

# Função para atualizar a janela de informações do RPG
def update_rpg_window():
    status_text = "\n".join([f"{key}: {value}" for key, value in status.items()])
    inventory_text = "\n".join([f"{key}: {value}" for key, value in inventory.items()])
    curiosity_text = random.choice(curiosidades)  # Escolhe uma curiosidade aleatória
    status_label.config(text=f"Status:\n{status_text}")
    inventory_label.config(text=f"Inventário:\n{inventory_text}")
    curiosity_label.config(text=f"Você Sabia?\n{curiosity_text}")

# Função para abrir a janela de venda de maçãs
def open_sell_window():
    sell_window = tk.Toplevel(root)
    sell_window.title("Venda de Maçãs")
    sell_window.geometry("300x100")
    
    def sell_apples():
        global apple_count, money
        if apple_count > 0:
            money += apple_count
            apple_count = 0
            score_label.config(text=f"Pontuação: {score} | Maçãs: {apple_count} | Lootboxes: {lootboxes} | Dinheiro: ${money}")
            sell_window.destroy()
        else:
            tk.Label(sell_window, text="Você não tem maçãs para vender!", font=("Arial", 12)).pack()
    
    tk.Label(sell_window, text=f"Você tem {apple_count} maçãs. Vender por ${apple_count}?", font=("Arial", 14)).pack()
    tk.Button(sell_window, text="Vender", command=sell_apples, font=("Arial", 14)).pack()

# Função para abrir a janela de loja
def open_shop_window():
    shop_window = tk.Toplevel(root)
    shop_window.title("Loja")
    shop_window.geometry("300x200")
    
    def buy_agility_talisman():
        global money
        if money >= 10:
            money -= 10
            status["agilidade"] *= 1.5  # Aumenta a agilidade em 1.5x
            score_label.config(text=f"Pontuação: {score} | Maçãs: {apple_count} | Lootboxes: {lootboxes} | Dinheiro: ${money}")
            update_rpg_window()
            shop_window.destroy()
        else:
            tk.Label(shop_window, text="Dinheiro insuficiente!", font=("Arial", 12)).pack()
    
    def buy_luck_talisman():
        global money
        if money >= 30:
            money -= 30
            status["sorte"] += 1  # Aumenta a sorte
            score_label.config(text=f"Pontuação: {score} | Maçãs: {apple_count} | Lootboxes: {lootboxes} | Dinheiro: ${money}")
            update_rpg_window()
            shop_window.destroy()
        else:
            tk.Label(shop_window, text="Dinheiro insuficiente!", font=("Arial", 12)).pack()
    
    tk.Label(shop_window, text="Bem-vindo à Loja!", font=("Arial", 16)).pack()
    tk.Button(shop_window, text="Comprar Talismã de Agilidade ($10)", command=buy_agility_talisman, font=("Arial", 12)).pack()
    tk.Button(shop_window, text="Comprar Talismã de Sorte ($30)", command=buy_luck_talisman, font=("Arial", 12)).pack()

# Função para verificar se o Nemesis aparece
def check_nemesis():
    if random.randint(1, 20) == 1:  # 5% de chance de aparecer
        nemesis["aparecer"] = True
        nemesis["maçãs_roubadas"] = random.randint(1, 5)
        global apple_count
        apple_count = max(0, apple_count - nemesis["maçãs_roubadas"])
        score_label.config(text=f"Pontuação: {score} | Maçãs: {apple_count} | Lootboxes: {lootboxes} | Dinheiro: ${money}")
        tk.messagebox.showwarning("Nemesis Apareceu!", f"{nemesis['nome']} roubou {nemesis['maçãs_roubadas']} maçãs!")

# Botão para abrir lootbox
open_button = tk.Button(root, text="Abrir Lootbox", command=open_lootbox, font=("Arial", 16))
open_button.pack()

# Botão para abrir a janela de informações do RPG
rpg_button = tk.Button(root, text="Status do RPG", command=open_rpg_window, font=("Arial", 16))
rpg_button.pack()

# Botão para abrir a janela de venda de maçãs
sell_button = tk.Button(root, text="Vender Maçãs", command=open_sell_window, font=("Arial", 16))
sell_button.pack()

# Botão para abrir a janela de loja
shop_button = tk.Button(root, text="Loja", command=open_shop_window, font=("Arial", 16))
shop_button.pack()

# Label para mostrar o resultado da lootbox
result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack()

# Vincula as teclas ao movimento do personagem
root.bind("<Left>", move_player)
root.bind("<Right>", move_player)

# Inicia o movimento da maçã
move_apple()

# Inicia o loop principal da interface
root.mainloop()