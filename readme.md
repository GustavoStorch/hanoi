
# 🏗️ Torre de Hanoi - Simulador Gráfico

Este projeto é um simulador gráfico da **Torre de Hanoi**, desenvolvido em Python utilizando a biblioteca Tkinter. O objetivo é ilustrar visualmente a resolução desse clássico problema matemático, além de registrar todos os movimentos em um arquivo `.txt`.

---

## 📂 Estrutura do Projeto

```
Honoi/
├── resources/
│   └── movimentos.txt        # Arquivo de log dos movimentos
├── app.py                    # Arquivo principal para executar o projeto
├── janela_inicial.py         # Interface para configurar o jogo
├── torre_de_honoi_gui.py     # Interface gráfica e lógica da Torre de Hanoi
└── readme.md                 # Documentação do projeto
```

---

## 📖 Sobre a Torre de Hanoi

A Torre de Hanoi é um quebra-cabeça matemático inventado em 1883 por Édouard Lucas. O desafio consiste em três hastes e um número de blocos de tamanhos diferentes, empilhados de forma decrescente em uma haste.

### ✅ Regras:
- Apenas um bloco pode ser movido por vez.
- Um bloco deve estar sempre no topo da pilha para ser movido.
- Não é permitido colocar um bloco maior sobre um menor.

### 🎯 Objetivo:
Transferir todos os blocos da **haste inicial** para a **haste final**, seguindo as regras acima.

---

## 🚀 Como Executar o Projeto

### ✔️ Pré-requisitos:
- Python 3 instalado.

> 🔸 O projeto utiliza apenas bibliotecas nativas do Python (`tkinter`), não sendo necessário instalar dependências externas.

---

### ▶️ Passo a passo para execução:

1. Clone ou baixe o projeto:

```bash
git clone https://github.com/GustavoStorch/hanoi.git
cd honoi
```

2. Execute o projeto com o seguinte comando:

```bash
python app.py
```

---

## 🧠 Como Funciona

1. Ao rodar `app.py`, abrirá uma janela onde você deve configurar:
   - A quantidade de blocos (de 1 até 20).
   - A haste de origem (**A**, **B** ou **C**).
   - A haste de destino (**A**, **B** ou **C**).

2. Após clicar em **Iniciar**, abrirá a interface gráfica mostrando:
   - As 3 hastes (**A**, **B**, **C** com seus rótulos abaixo).
   - Os blocos empilhados na haste de origem.
   - Animações representando cada movimento dos blocos.

3. Todos os movimentos também são registrados no arquivo:

```
/resources/movimentos.txt
```

Exemplo de registro:

```
Mover bloco 1 de A para C
Mover bloco 2 de A para B
Mover bloco 1 de C para B
...
```

---

## ⚙️ Desempenho e Limitações

- O número de movimentos necessários cresce exponencialmente, seguindo a fórmula:

\(
	ext{Movimentos} = 2^n - 1
\)

| 🧱 Blocos | 🔢 Movimentos         |
|-----------|-----------------------|
| 3         | 7                     |
| 6         | 63                    |
| 10        | 1.023                 |
| 15        | 32.767                |
| 20        | 1.048.575             |

- A interface gráfica funciona bem até 6 blocos para visualização em tempo real.
- Para mais blocos (até 20), o programa registra corretamente os movimentos no arquivo `movimentos.txt`, mas a animação pode se tornar muito demorada.

---

## 🎨 Interface

- Visualização gráfica com três hastes nomeadas (**A**, **B**, **C**).
- Blocos representados visualmente e organizados por tamanho.
- Identificação textual abaixo de cada haste.

---

## ✍️ Autor

- **Gustavo** – Desenvolvedor de Software  

---

## 📜 Licença

Este projeto está licenciado sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.
