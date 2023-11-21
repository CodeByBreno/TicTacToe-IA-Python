from playsound import playsound
import random;

def play_toc():
    rand = random.randint(0,2);
    if (rand == 0):
        playsound(r'C:\Users\Breno Gabriel\Documents\Projetos Pessoais\TicTacToe_Game\audio\toc1.mp3');
    if (rand == 1):
        playsound(r'C:\Users\Breno Gabriel\Documents\Projetos Pessoais\TicTacToe_Game\audio\toc2.mp3');
    if (rand == 2):
        playsound(r'C:\Users\Breno Gabriel\Documents\Projetos Pessoais\TicTacToe_Game\audio\toc3.mp3');

for i in range(0, 100):
    play_toc();
