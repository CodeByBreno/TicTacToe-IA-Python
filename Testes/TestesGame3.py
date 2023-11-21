import sys
sys.path.append("..")  # Adiciona o diretório pai ao caminho de pesquisa

from GameElements import *;
import random;

turn = 0;
new_game = Game();
new_game.play(random.randint(0,2), random.randint(0,2));

while(True):
    turn += 1;
    min = 2;
    max = -2;
    max_play = None;
    min_play = None;
    
    print("------------- Turno " + str(turn) + " --------------");
    print(new_game.show());

    if new_game.isOver():
        break;

    turno = new_game.turn;
    for each in new_game.state.actions(turno):
        value = each.minimax();
        
        if turno == "O" and value >= max:
            max = value;
            max_play = each;
        elif turno == "X" and value <= min:
            min = value;
            min_play = each;
    
    if new_game.turn == "O":
        new_game.changeState(max_play);
    else:
        new_game.changeState(min_play);