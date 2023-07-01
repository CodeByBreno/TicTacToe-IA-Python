import sys
sys.path.append("..")  # Adiciona o diretório pai ao caminho de pesquisa

from GameElements import *;
testes = [];

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

for i in range(0, len(testes)):
    test = State("O", matriz_creation=MatrizQuadrada(testes[i], dimensao=3));
    print("\nMatriz:\n" + test.show())
    print("Minimax do estado: " + str(test.minimax()));

