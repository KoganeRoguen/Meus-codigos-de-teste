import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random

class MoneySimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulador de Mendigo Virtual (Streamer)")
        self.master.geometry("250x300")
        self.center_window()
        
        self.money = 0.01  # Valor inicial em reais
        self.total_money = 0.0
        self.upgrade_cost = 1.00  # Custo inicial do upgrade
        self.max_donate = 0.10  # Valor máximo que pode ser juntado
        self.progress_value = 0  # Valor do progresso
        self.boost_cost = 10.00  # Custo inicial para comprar peças melhores
        self.speed_multiplier = 1  # Multiplicador de velocidade

        self.label_money = tk.Label(master, text="Total: R$ 0.00")
        self.label_money.pack()
        
        self.label_streaming = tk.Label(master, text="")
        self.label_streaming.pack()

        self.button_juntar = tk.Button(master, text="Mendigar Donate", command=self.start_donate_progress)
        self.button_juntar.pack(pady=5)

        self.progressbar = ttk.Progressbar(master, length=200, maximum=30)  # Define o máximo como 30
        self.progressbar.pack(pady=5)

        self.button_upgrade = tk.Button(master, text=f"Gostosificação R$ {self.upgrade_cost:.2f}", command=self.upgrade)
        self.button_upgrade.pack(pady=5)

        self.button_boost = tk.Button(master, text=f"Comprar Peças Melhores R$ {self.boost_cost:.2f}", command=self.buy_boost)
        self.button_boost.pack(pady=5)

    def center_window(self):
        window_width = 250
        window_height = 300
        
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        
        x_coordinate = int((screen_width // 2)) - (window_width // 2)
        y_coordinate = int((screen_height // 2)) - (window_height // 2)
        
        self.master.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
        
    def start_donate_progress(self):
        self.progress_value = 0
        self.progressbar['value'] = self.progress_value
        self.label_streaming.config(text="Streaming...")  # Mostra a mensagem "Streaming..."
        self.button_juntar.config(state=tk.DISABLED)  # Desabilita o botão enquanto a barra enche
        self.update_progress()  # Inicia a atualização da barra de progresso

    def update_progress(self):
        self.progress_value += 1
        self.progressbar['value'] = self.progress_value
        if self.progress_value < 30 / self.speed_multiplier:  # Acelera a barra
            self.master.after(int(1000 / self.speed_multiplier), self.update_progress)
        else:
            # Adiciona um valor aleatório entre 0,01 e 0,10 ao total
            self.total_money += round(random.uniform(0.01, 0.10), 2)  
            self.label_money.config(text=f"Total: R$ {self.total_money:.2f}")
            self.label_streaming.config(text="")  # Remove a mensagem "Streaming..."
            self.button_juntar.config(state=tk.NORMAL)  # Habilita o botão novamente

            self.check_upgrade_availability()
            self.check_victory_condition()

    def buy_boost(self):
        if self.total_money >= self.boost_cost:
            self.total_money -= self.boost_cost
            self.speed_multiplier *= 1.5  # Acelera a barra em 1.5x
            self.boost_cost *= 2  # Duplica o custo do próximo boost
            self.label_money.config(text=f"Total: R$ {self.total_money:.2f}")
            self.button_boost.config(text=f"Comprar Peças Melhores R$ {self.boost_cost:.2f}")
            self.check_upgrade_availability()
            self.check_victory_condition()
        else:
            messagebox.showwarning("Oh não!", "Você não tem dinheiro suficiente para comprar peças melhores.")

    def upgrade(self):
        if self.total_money >= self.upgrade_cost:
            self.total_money -= self.upgrade_cost
            self.upgrade_cost *= 1.75  # Aumentar o custo do próximo upgrade
            self.label_money.config(text=f"Total: R$ {self.total_money:.2f}")
            self.button_upgrade.config(text=f"Upgrade R$ {self.upgrade_cost:.2f}")
            self.check_upgrade_availability()
            self.check_victory_condition()
        else:
            messagebox.showwarning("Oh não!", "Você não tem dinheiro suficiente para comprar cosméticos para ficar mais gostoso(a) :(")

    def check_upgrade_availability(self):
        if self.total_money >= self.upgrade_cost:
            self.button_upgrade.config(state=tk.NORMAL)
        else:
            self.button_upgrade.config(state=tk.DISABLED)

    def check_victory_condition(self):
        if self.total_money >= 1_000_000_000_000_000:
            messagebox.showinfo("Você venceu!", "Parabéns! Você é o primeiro Streamer Quadrilionário e mais gostoso do mundo!! :D")
            self.master.quit()
                
if __name__ == "__main__":
    root = tk.Tk()
    app = MoneySimulator(root)
    root.mainloop()