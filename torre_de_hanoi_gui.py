import tkinter as tk
import tkinter.messagebox as messagebox
import time
import os

class TorreDeHanoiGUI:
    def __init__(self, janela, quantidade_blocos, haste_inicial, haste_final):
        self.janela = janela
        self.janela.title("Torre de Hanoi")
        self.quantidade_blocos = quantidade_blocos
        self.haste_inicial = haste_inicial
        self.haste_final = haste_final
        self.hastes = {'A': [], 'B': [], 'C': []}

        for i in range(quantidade_blocos, 0, -1):
            self.hastes[self.haste_inicial].append(i)

        self.movimentos = []
        self.contador_movimentos = 0

        self.canvas = tk.Canvas(janela, width=600, height=400, bg='white')
        self.canvas.pack()

        self.desenhar()

        hastes = {'A', 'B', 'C'}
        self.haste_auxiliar = (hastes - {self.haste_inicial, self.haste_final}).pop()

        self.janela.after(1000, lambda: self.resolver(quantidade_blocos, self.haste_inicial, self.haste_final, self.haste_auxiliar))

    def desenhar(self):
        self.canvas.delete('all')

        posicoes_hastes = {'A': 100, 'B': 300, 'C': 500}

        for posicao in posicoes_hastes.values():
            self.canvas.create_rectangle(posicao - 5, 100, posicao + 5, 350, fill='black')

        for haste, blocos in self.hastes.items():
            x = posicoes_hastes[haste]
            y = 350
            for bloco in blocos:
                largura = bloco * 20
                self.canvas.create_rectangle(x - largura // 2, y - 20, x + largura // 2, y, fill='skyblue')
                y -= 25

        for haste, posicao_x in posicoes_hastes.items():
            self.canvas.create_text(posicao_x, 370, text=haste, font=("Arial", 16, "bold"))

        self.janela.update()
        time.sleep(0.5)

    def mover(self, origem, destino):
        bloco = self.hastes[origem].pop()
        self.hastes[destino].append(bloco)
        self.contador_movimentos += 1

        movimento_texto = f"Movimento {self.contador_movimentos}: Bloco {bloco} saiu da haste {origem} e foi para a haste {destino}"
        self.movimentos.append(movimento_texto)

        self.desenhar()

    def resolver(self, n, origem, destino, auxiliar):
        if n == 1:
            self.mover(origem, destino)
        else:
            self.resolver(n - 1, origem, auxiliar, destino)
            self.mover(origem, destino)
            self.resolver(n - 1, auxiliar, destino, origem)

        if n == self.quantidade_blocos and origem == self.haste_inicial and destino == self.haste_final:
            self.salvar_movimentos()
            self.mostrar_total_movimentos()
            self.janela.after(500, self.perguntar_jogar_novamente)

    def salvar_movimentos(self):
        if not os.path.exists("resources"):
            os.makedirs("resources")

        caminho = os.path.join("resources", "movimentos.txt")
        with open(caminho, "w") as arquivo:
            for linha in self.movimentos:
                arquivo.write(linha + "\n")

    def mostrar_total_movimentos(self):
        total = f"Total de movimentos: {self.contador_movimentos}"
        self.canvas.create_text(300, 50, text=total, font=("Arial", 16), fill="red")
        self.janela.update()

    def perguntar_jogar_novamente(self):
        from janela_inicial import JanelaInicial 

        resposta = messagebox.askyesno("Jogar novamente?", "Deseja jogar outra partida?")
        if resposta:
            self.janela.destroy()
            root = tk.Tk()
            JanelaInicial(root)
            root.mainloop()
