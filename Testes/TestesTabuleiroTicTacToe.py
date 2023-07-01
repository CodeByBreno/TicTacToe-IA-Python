import sys
sys.path.append("..")  # Adiciona o diretório pai ao caminho de pesquisa

from TabuleiroTicTacToe import *;

testes = [];
testes.append(["X", "X", "X", "O", "X", "O", "O", "O", "X"])
testes.append(["X", "O", "X", "O", "X", "O", "O", "O", "X"])
testes.append(["X", "O", "O", "O", "X", "O", "X", "O", "X"])
testes.append(["X", "X", "O", "O", "X", "O", "O", "O", "X"])
testes.append(["O", "X", "X", "O", "X", "O", "O", "O", "X"])
testes.append(["O", "O", "X", "O", "X", "O", "X", "O", "X"])
testes.append(["O", "X", "X", "O", "O", "O", "X", "O", "X"])
testes.append(["X", "X", "O", "O", "X", "O", "X", "O", "X"])
testes.append(["O", "O", "O", " ", "X", " ", " ", "X", " "])
testes.append(["O", "X", " ", " ", "O", "X", " ", " ", "O"])
testes.append(["O", "X", "O", " ", " ", " ", "X", "X", "O"])
testes.append([" ", "X", "O", "O", " ", "X", "O", "X", " "])
testes.append(["O", "X", "X", "O", "X", "O", "X", "O", "X"])
testes.append(["O", "X", "O", "X", "X", "O", "X", "O", "X"])
testes.append(["O", "X", "O", "O", "X", "O", "X", "O", "X"])
testes.append(["O", "X", "O", "X", "O", "O", "X", "O", "X"])
testes.append(["O", "X", "O", "X", "X", "O", "O", "O", "X"])

teste_tabuleiro = TabuleiroTicTacToe();
print(teste_tabuleiro.show());

for i in range(0, len(testes)):
    print("\n====================================================");
    print("                     teste" + str(i) + "                         ");
    print("====================================================");
    teste_tabuleiro = TabuleiroTicTacToe(creation_body = testes[i]);
    print(teste_tabuleiro.show());
    print(teste_tabuleiro.analyse());