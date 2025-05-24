import tkinter as tk
from torre_de_hanoi_gui import TorreDeHanoiGUI

class JanelaInicial:
    def __init__(self, master):
        self.master = master
        master.title("Configuração Torre de Hanoi")
        master.geometry("300x200")

        tk.Label(master, text="Digite a quantidade de blocos (1 a 6):").pack(pady=5)
        self.entrada_blocos = tk.Entry(master)
        self.entrada_blocos.pack()

        tk.Label(master, text="Digite a haste inicial (A, B ou C):").pack(pady=5)
        self.entrada_inicial = tk.Entry(master)
        self.entrada_inicial.pack()

        tk.Label(master, text="Digite a haste final (A, B ou C):").pack(pady=5)
        self.entrada_final = tk.Entry(master)
        self.entrada_final.pack()

        self.botao_iniciar = tk.Button(master, text="Iniciar", command=self.iniciar_jogo)
        self.botao_iniciar.pack(pady=10)

        self.mensagem = tk.Label(master, text="", fg="red")
        self.mensagem.pack()

    def iniciar_jogo(self):
        blocos = self.entrada_blocos.get().strip()
        inicial = self.entrada_inicial.get().strip().upper()
        final = self.entrada_final.get().strip().upper()

        if not blocos.isdigit():
            self.mensagem.config(text="Digite um número válido para blocos.")
            return

        quantidade = int(blocos)
        if quantidade < 1 or quantidade > 10:
            self.mensagem.config(text="Quantidade de blocos deve ser entre 1 e 10.")
            return

        if inicial not in ('A', 'B', 'C'):
            self.mensagem.config(text="Haste inicial inválida. Escolha A, B ou C.")
            return

        if final not in ('A', 'B', 'C'):
            self.mensagem.config(text="Haste final inválida. Escolha A, B ou C.")
            return

        if inicial == final:
            self.mensagem.config(text="Haste inicial e final devem ser diferentes.")
            return

        self.master.destroy()

        root = tk.Tk()
        jogo = TorreDeHanoiGUI(root, quantidade, inicial, final)
        root.mainloop()
