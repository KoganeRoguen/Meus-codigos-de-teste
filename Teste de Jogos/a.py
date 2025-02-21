import tkinter as tk
from tkinter import messagebox
import random

# Configurações da tela
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
PLAYER_SIZE, APPLE_SIZE = 50, 25
PLAYER_SPEED, APPLE_SPEED, FPS = 10, 5, 60

# Inicializa a janela principal
root = tk.Tk()
root.title("Coletor de Maçãs RPG")
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

# Cria o canvas (área de desenho)
canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg="white")
canvas.pack()

# Personagem (quadrado verde)
player = canvas.create_rectangle(SCREEN_WIDTH // 2 - PLAYER_SIZE // 2,
                                  SCREEN_HEIGHT - PLAYER_SIZE - 10,
                                  SCREEN_WIDTH // 2 + PLAYER_SIZE // 2,
                                  SCREEN_HEIGHT - 10,
                                  fill="green")

# Maçã (círculo vermelho)
apple = canvas.create_oval(random.randint(0, SCREEN_WIDTH - APPLE_SIZE), 0,
                            random.randint(0, SCREEN_WIDTH - APPLE_SIZE) + APPLE_SIZE,
                            APPLE_SIZE, fill="red")

# Status e inventário
status = {"força": 1, "agilidade": 1, "sorte": 1, "dano": 1, "defesa": 0}
inventory = {f"{item} {quality}": 0 for item in ["Espada", "Capacete", "Peitoral", "Calça", "Bota"]
              for quality in ["Comum", "Rara", "Lendária"]}
equipped_items = {item: None for item in ["espada", "capacete", "peitoral", "calça", "bota"]}

# Dinheiro e contadores
score, apple_count, lootboxes, money = 0, 0, 0, 0

# Curiosidades
curiosidades = [
    "Você sabia? Maçãs são uma ótima fonte de fibras!",
    "Você sabia? O jogador mais rápido do mundo pode coletar 100 maçãs em 1 minuto!",
    "Você sabia? O talismã de sorte aumenta suas chances de ganhar lootboxes!",
    "Você sabia? O sistema Nemesis foi inspirado em Shadow of Mordor!"
]

# Atualiza a label de pontuação
def update_score_label():
    score_label.config(text=f"Pontuação: {score} | Maçãs: {apple_count} | Lootboxes: {lootboxes} | Dinheiro: ${money}")

# Função para mover o jogador
def move_player(event):
    offset = PLAYER_SPEED * status["agilidade"] * (-1 if event.keysym == "Left" else 1)
    canvas.move(player, offset, 0)

# Função para mover a maçã
def move_apple():
    canvas.move(apple, 0, APPLE_SPEED)
    if canvas.coords(apple)[3] > SCREEN_HEIGHT:
        reset_apple()
    check_collision()
    root.after(1000 // FPS, move_apple)

# Resetar a maçã
def reset_apple():
    x = random.randint(0, SCREEN_WIDTH - APPLE_SIZE)
    canvas.coords(apple, x, 0, x + APPLE_SIZE, APPLE_SIZE)

# Verificar colisão
def check_collision():
    global score, apple_count, lootboxes
    if canvas.coords(apple)[1] < canvas.coords(player)[3] and \
       canvas.coords(apple)[3] > canvas.coords(player)[1] and \
       canvas.coords(apple)[0] < canvas.coords(player)[2] and \
       canvas.coords(apple)[2] > canvas.coords(player)[0]:
        score += status["força"]
        apple_count += 1
        if random.randint(1, 10) <= status["sorte"]:
            lootboxes += 1
        update_score_label()
        reset_apple()

# Abrir lootbox
def open_lootbox():
    global lootboxes
    if lootboxes > 0:
        lootboxes -= 1
        item = random.choices(
            [f"{item} {quality}" for item in ["Espada", "Capacete", "Peitoral", "Calça", "Bota"]
             for quality in ["Comum", "Rara", "Lendária"]],
            weights=[25, 15, 10, 25, 10, 5, 5, 5, 5, 10, 5, 5, 35, 15, 10]
        )[0]
        inventory[item] += 1
        result_label.config(text=f"Você ganhou: {item}")
        update_status(item)
        update_score_label()
    else:
        result_label.config(text="Você não tem lootboxes!")

# Atualiza status com base no item
def update_status(item):
    if "Espada" in item:
        status["dano"] += {"Comum": 5, "Rara": 15, "Lendária": 30}[item.split()[1]]
    else:
        status["defesa"] += {"Capacete": { "Comum": 1, "Rara": 2, "Lendária": 4 },
                              "Peitoral": { "Comum": 2, "Rara": 5, "Lendária": 7 },
                              "Calça": { "Comum": 1, "Rara": 3, "Lendária": 5 },
                              "Bota": { "Comum": 1, "Rara": 1, "Lendária": 3 }}[item.split()[0]][item.split()[1]]

# Janela de equipamentos
def open_equipment_window():
    stop_apple_movement()  # Para as maçãs ao abrir a janela
    equip_window = tk.Toplevel(root)
    equip_window.title("Equipamentos do Personagem")
    equip_window.geometry("300x400")
    
    tk.Label(equip_window, text="Equipamentos:", font=("Arial", 16)).pack(pady=5)

    # Espada
    sword_frame = tk.Frame(equip_window)
    sword_frame.pack(pady=5)
    tk.Label(sword_frame, text="Espada:").grid(row=0, column=0)
    sword_var = tk.StringVar(value="Nenhuma")
    tk.Label(sword_frame, textvariable=sword_var).grid(row=0, column=1)

    # Adiciona botões para espadas
    for sword in ["Espada Comum", "Espada Rara", "Espada Lendária"]:
        if inventory[sword] > 0:
            tk.Button(sword_frame, text=f"Equipar {sword}", command=lambda s=sword: equip_item("espada", s)).grid(column=0, sticky="w")

    # Armaduras
    armor_frame = tk.Frame(equip_window)
    armor_frame.pack(pady=5)

    for armor in ["Capacete", "Peitoral", "Calça", "Bota"]:
        tk.Label(armor_frame, text=f"{armor}:").pack(anchor="w")
        armor_var = tk.StringVar(value="Nenhuma")
        tk.Label(armor_frame, textvariable=armor_var).pack()
        
        for quality in ["Comum", "Rara", "Lendária"]:
            item = f"{armor} {quality}"
            if inventory[item] > 0:
                tk.Button(armor_frame, text=f"Equipar {item}", command=lambda a=item: equip_item(armor.lower(), a)).pack(anchor="w")

    equip_window.protocol("WM_DELETE_WINDOW", lambda: (start_apple_movement(), equip_window.destroy()))  # Retorna ao movimento das maçãs ao fechar

# Equipar item
def equip_item(item_type, item_name):
    equipped_items[item_type] = item_name
    update_equipment_labels()

# Janela de status RPG
def open_rpg_window():
    stop_apple_movement()  # Para as maçãs ao abrir a janela
    rpg_window = tk.Toplevel(root)
    rpg_window.title("Status do RPG")
    rpg_window.geometry("300x400")
    
    global status_label
    status_label = tk.Label(rpg_window, text="", font=("Arial", 14))
    status_label.pack(pady=5)
    
    update_rpg_window()
    rpg_window.protocol("WM_DELETE_WINDOW", lambda: (start_apple_movement(), rpg_window.destroy()))  # Retorna ao movimento das maçãs ao fechar

# Atualiza a janela de informações do RPG
def update_rpg_window():
    status_text = "\n".join([f"{key}: {value}" for key, value in status.items()])
    status_label.config(text=f"Status:\n{status_text}")

# Funções de venda e loja
def open_sell_window():
    stop_apple_movement()  # Para as maçãs ao abrir a janela
    sell_window = tk.Toplevel(root)
    sell_window.title("Venda de Maçãs")
    sell_window.geometry("300x100")
    
    def sell_apples():
        global apple_count, money
        if apple_count > 0:
            money += apple_count
            apple_count = 0
            update_score_label()
            sell_window.destroy()
        else:
            tk.Label(sell_window, text="Você não tem maçãs para vender!", font=("Arial", 12)).pack()
    
    tk.Label(sell_window, text=f"Você tem {apple_count} maçãs. Vender por ${apple_count}?", font=("Arial", 14)).pack()
    tk.Button(sell_window, text="Vender", command=sell_apples, font=("Arial", 14)).pack()
    sell_window.protocol("WM_DELETE_WINDOW", lambda: (start_apple_movement(), sell_window.destroy()))  # Retorna ao movimento das maçãs ao fechar

def open_shop_window():
    stop_apple_movement()  # Para as maçãs ao abrir a janela
    shop_window = tk.Toplevel(root)
    shop_window.title("Loja")
    shop_window.geometry("300x200")
    
    def buy_talisman(talisman_type, cost):
        global money
        if money >= cost:
            money -= cost
            status[talisman_type] *= 1.5 if talisman_type == "agilidade" else 1
            update_score_label()
            shop_window.destroy()
        else:
            tk.Label(shop_window, text="Dinheiro insuficiente!", font=("Arial", 12)).pack()
    
    tk.Label(shop_window, text="Bem-vindo à Loja!", font=("Arial", 16)).pack(pady=5)
    tk.Button(shop_window, text="Comprar Talismã de Agilidade ($10)", command=lambda: buy_talisman("agilidade", 10), font=("Arial", 12)).pack(pady=5)
    tk.Button(shop_window, text="Comprar Talismã de Sorte ($30)", command=lambda: buy_talisman("sorte", 30), font=("Arial", 12)).pack(pady=5)
    shop_window.protocol("WM_DELETE_WINDOW", lambda: (start_apple_movement(), shop_window.destroy()))  # Retorna ao movimento das maçãs ao fechar

# Para as maçãs
def stop_apple_movement():
    global apple_movement
    apple_movement = False

def start_apple_movement():
    global apple_movement
    apple_movement = True
    move_apple()

# Verificar se o Nemesis aparece
def check_nemesis():
    if random.randint(1, 20) == 1:
        nemesis = {"nome": "Inimigo Aleatório", "maçãs_roubadas": random.randint(1, 5)}
        global apple_count
        apple_count = max(0, apple_count - nemesis["maçãs_roubadas"])
        update_score_label()
        messagebox.showwarning("Nemesis Apareceu!", f"{nemesis['nome']} roubou {nemesis['maçãs_roubadas']} maçãs!")

# Botões principais
score_label = tk.Label(root, text="", font=("Arial", 12))
score_label.place(relx=0.5, rely=0.1, anchor='center')
update_score_label()

tk.Button(root, text="Abrir Lootbox", command=open_lootbox, font=("Arial", 16)).place(relx=0.5, rely=0.3, anchor='center')
tk.Button(root, text="Equipar Itens", command=open_equipment_window, font=("Arial", 16)).place(relx=0.5, rely=0.4, anchor='center')
tk.Button(root, text="Status do RPG", command=open_rpg_window, font=("Arial", 16)).place(relx=0.5, rely=0.5, anchor='center')
tk.Button(root, text="Vender Maçãs", command=open_sell_window, font=("Arial", 16)).place(relx=0.5, rely=0.6, anchor='center')
tk.Button(root, text="Loja", command=open_shop_window, font=("Arial", 16)).place(relx=0.5, rely=0.7, anchor='center')
result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.place(relx=0.5, rely=0.8, anchor='center')

# Inicia o movimento da maçã e o loop principal
apple_movement = True
move_apple()
root.mainloop()