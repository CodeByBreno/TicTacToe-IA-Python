import sys
sys.path.append("..")  # Adiciona o diretório pai ao caminho de pesquisa

from GameElements import *;
import random;

def machine_play(game_state : "Game"):
    min = 2;
    max = -2;
    max_play = None;
    min_play = None;

    turno = game_state.turn;
    for each in game_state.state.actions(turno):
        value = each.minimax();
        
        if turno == "O" and value >= max:
            max = value;
            max_play = each;
        elif turno == "X" and value <= min:
            min = value;
            min_play = each;
    
    if game_state.turn == "O":
        return max_play;
    else:
        return min_play;

turn = 0;
new_game = Game();
new_game.play(random.randint(0,2), random.randint(0,2));

print(new_game.show());
new_game.changeState(machine_play(new_game));
print(new_game.show());
new_game.changeState(machine_play(new_game));
print(new_game.show());
new_game.changeState(machine_play(new_game));
print(new_game.show());
new_game.changeState(machine_play(new_game));
print(new_game.show());
new_game.changeState(machine_play(new_game));
print(new_game.show());