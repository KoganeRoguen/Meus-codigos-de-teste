import tkinter as tk
import random
import math

class Roleta(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Roleta de Decisões")
        self.geometry("400x400")
        self.canvas = tk.Canvas(self, width=300, height=300)
        self.canvas.pack(pady=20)

        self.segmentos = ["Opção 1", "Opção 2", "Opção 3", "Opção 4", "Opção 5", "Opção 6"]
        self.angle = 0
        self.draw_roleta()

        self.boton_girar = tk.Button(self, text="Girar!", command=self.girar)
        self.boton_girar.pack()

    def draw_roleta(self):
        self.canvas.delete("all")
        for i, segmento in enumerate(self.segmentos):
            start_angle = (360 / len(self.segmentos)) * i + self.angle
            extent_angle = 360 / len(self.segmentos)

            # Desenha o arco
            self.canvas.create_arc(50, 50, 250, 250, start=start_angle, extent=extent_angle, fill=self.get_cor(i), outline="white", width=2)

            # Calcula a posição do texto
            text_angle = start_angle + extent_angle / 2
            x = 150 + 90 * math.cos(math.radians(text_angle))
            y = 150 + 90 * math.sin(math.radians(text_angle))
            self.canvas.create_text(x, y, text=segmento, fill="white")

    def get_cor(self, i):
        cores = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#FFCC33", "#33FFF7"]
        return cores[i % len(cores)]

    def girar(self):
        self.angle += random.randint(720, 1080)  # Giro entre 2 a 3 voltas
        self.animar()

    def animar(self):
        self.canvas.delete("all")
        self.draw_roleta()
        if self.angle > 0:
            self.angle -= 10  # Reduz o ângulo para girar
            self.after(20, self.animar)
        else:
            self.mostrar_resultado()

    def mostrar_resultado(self):
        posicao_final = (360 - (self.angle % 360)) % 360
        indice = int(len(self.segmentos) * (posicao_final / 360)) % len(self.segmentos)
        resultado = self.segmentos[indice]
        self.canvas.create_text(150, 35, text=f"Resultado: {resultado}", fill="black", font=("Arial", 16))

if __name__ == "__main__":
    app = Roleta()
    app.mainloop()