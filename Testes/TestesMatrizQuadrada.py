import sys
sys.path.append("..")  # Adiciona o diretório pai ao caminho de pesquisa

from MatrizQuadrada import *;

# ===================================================
#                Testagem da Matriz
# ===================================================

teste = MatrizQuadrada([1,2,3,4,5,6,7,8,9], 3);
print(teste.show());

for i in range(0, teste.dimensao):
    for j in range(0, teste.dimensao):
        if ((i*teste.dimensao + j)%2 == 0): teste.put("X", i, j);
        else: teste.put("O", i, j);

print(teste.show());

teste.fullfill("A");
print(teste.show());

print(teste.ifPut("B", 1, 2).show());
print(teste.show());