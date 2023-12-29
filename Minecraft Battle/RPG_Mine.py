import random
from tkinter import Tk, Label, Button, Toplevel

p_hp = 100
ed_hp = 1000

p_sp = 1
p_pc = 5

root = Tk()
root.title("Battle")
root.geometry("400x300")

status_label = Label(root, text=f'''
========================== Battle =========================

    Ender dragon HP: {ed_hp}

------------------------------------------------------------------------------------
                      
    Player HP: {p_hp}
                      
===========================================================
                     ''')

status_label.pack()

def update_status():
    status_label.config(text=f'''
========================== Battle =========================

    Ender dragon HP: {ed_hp}

------------------------------------------------------------------------------------
                      
    Player HP: {p_hp}
                      
===========================================================
                     ''')

def use_sword():
    global ed_hp, p_hp
    
    sword_damage = random.randint(8, 16)
    
    if ed_hp > 0:
        ed_hp -= sword_damage
        update_status()        

        if ed_hp <= 0:
            status_label.config(text="\nYou defeated the Ender Dragon! You Won :D")
            sword_button.destroy()

def use_bow():
    global ed_hp, p_hp
    
    bow_damage = random.randint(15, 30)
    shot = random.randint(1, 2)
    
    if shot == 2:
        ed_hp -= bow_damage
        update_status()
    else:
        None
        if ed_hp <= 0:
            status_label.config(text="\nYou defeated the Ender Dragon! You Won :D")
            bow_button.destroy()
       
bow_button = Button(root, text="Bow", command=use_bow)       
bow_button.pack()
        
sword_button = Button(root, text="Sword", command=use_sword)
sword_button.pack()

root.mainloop()

'''
# Player Turn

    if choice == '1':
        if player_sp == 0:
            s_dmg = random.randint(20, 35)*(1.5)
        else:
            s_dmg = random.randint(20, 35)
        if cpu_choice == 3:
            print('\n --- CPU bloqueou com escudo --- ')
        else:
            cpu_hp -= s_dmg
            print(f'\n -= Player deu {s_dmg} de dano com a Espada =- ')
    if choice == '2':
        chance = random.randint(1, 2)
        if chance == 1:
            if player_sp == 0:
                a_dmg = random.randint(30, 50)*(1.5)
            else:
                a_dmg = random.randint(30, 50)    
            cpu_hp -= a_dmg
            print(f'\n -= Player deu {a_dmg} de dano com o Machado =- ')
        elif cpu_choice == 3:
            print(f'\n -= Player quebrou o escudo de CPU e deu {a_dmg} de dano com o Machado =- ')
        else:
            print('\n --- Player errou o ataque de Machado --- ')
    if choice == '3':
        print('\n -= Player usou Escudo =- ')
        if cpu_choice == 1:
            print('\n --- CPU ataca Player com ataque com espada mas o Player bloqueou com escudo ---')
        elif cpu_choice == 2:
            cpu_chance = random.randint (1, 2)
            if cpu_chance == 1:
                if cpu_sp == 0:
                    cpu_a_dmg = random.randint(30, 50)*(1.5)
                else:
                    cpu_a_dmg = random.randint(30, 50)
                player_hp -= cpu_a_dmg
                print(f'\n --- CPU quebrou o escudo do Player e deu {cpu_a_dmg} de dano com o Machado --- ')
            else:
                print(f'\n --- CPU errou o ataque de Machado --- ')
    if choice == '4':
        if player_sp == 0:
            print(f'\n --- Player não possui mais Poções de força --- ')
        else:
            player_sp -= 1
            print(f'\n -= Player usou Poção de força (restantes: {player_sp}x) =- ')
    if choice == '5':
        if player_pc == 0:
            print(f'\n --- Player não possui mais Poções de cura --- ')
        else:
            player_pc -= 1
            health = random.randint(25, 40)
            player_hp += health
            print(f'\n -= Player usou Poção de cura e recuperou {health}+ de life (restantes: {player_pc}x) =- ')

# CPU Turn

    if cpu_choice == 1:
        if cpu_sp == 0:
            cpu_s_dmg = random.randint(20, 35)*(1.5)
        else:
            cpu_s_dmg = random.randint(20, 35)
        if choice == '3':
            print('\n --- Player bloqueou com escudo --- ')
        else:
            player_hp -= cpu_s_dmg
            print(f'\n -= CPU deu {cpu_s_dmg} de dano com a Espada =- ')
    if cpu_choice == 2:
        cpu_chance = random.randint(1, 2)
        if cpu_chance == 1:
            if cpu_sp == 0:
                cpu_a_dmg = random.randint(30, 50)*(1.5)
            else:
                cpu_a_dmg = random.randint(30, 50)
            player_hp -= cpu_a_dmg
            print(f'\n -= CPU deu {cpu_a_dmg} de dano com o Machado =- ')
        elif choice == 3:
            print(f'\n -= CPU quebrou o escudo de Player e deu {a_dmg} de dano com o Machado =- ')
        else:
            print('\n --- CPU errou o ataque de Machado --- ')
    if cpu_choice == 3:
        print('\n -= CPU usou escudo =- ')
        if choice == '1':
            print('\n --- Player ataca CPU com ataque com espada mas o Player bloqueou com escudo ---')
        elif choice == '2':
            chance = random.randint (1, 2)
            if chance == 1:
                if player_sp == 0:
                    a_dmg = random.randint(30, 50)*(1.5)
                else:
                    a_dmg = random.randint(30, 50)
                cpu_hp -= a_dmg
                print(f'\n --- Player quebrou o escudo do CPU e deu {cpu_a_dmg} de dano com o Machado --- ')
            else:
                print(f'\n --- Player errou o ataque de Machado --- ')
    if cpu_choice == 4:
        if cpu_sp == 0:
            print(f'\n --- CPU não possui mais Poções de força --- ')
        else:
            cpu_sp -= 1
            print(f'\n -= CPU usou Poção de força (restantes: {cpu_sp}x) =- ')
    if cpu_choice == 5:
        if cpu_pc == 0:
            print(f'\n --- Player não possui mais Poções de cura --- ')
        else:
            cpu_pc -= 1
            cpu_health = random.randint(25, 40)
            cpu_hp += cpu_health
            print(f'\n -= CPU usou Poção de cura e recuperou {cpu_health}+ de life (restantes: {cpu_pc}x) =- ')
            
# both HP
    print('\n===========================================================')
    print(f'\n Player HP: {player_hp} ')
    print('\n-----------------------------------------------------------')
    print(f'\n CPU HP: {cpu_hp} ')
    
'''
