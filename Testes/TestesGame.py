import sys
sys.path.append("..")  # Adiciona o diretório pai ao caminho de pesquisa

from GameElements import *;
import random;

new_game = Game();

print("Jogo começou!");
print(new_game.state.show());

print("==== 1ª Jogada");
print(new_game.play(1,2));
print(new_game.state.show());

print("==== 2ª Jogada");
print(new_game.play(1,2));
print(new_game.state.show());

print("==== 3ª Jogada");
print(new_game.play(0,1));
print(new_game.state.show());

print("==== 4ª Jogada");
print(new_game.play(0,0));
print(new_game.state.show());

print("Próximas jogadas possíveis para 'O':\n");
for each in new_game.state.actions(new_game.turn):
    print(each.show());
    print("Minimax do estado = " + str(each.minimax()) + "\n-----------------");
