from tkinter import *;
from ctypes import windll;
windll.shcore.SetProcessDpiAwareness(1); #tirado do StackOverFlow, serve para ajustar a resolução da janela

from GameElements import *;
from Constants import *;
from Estilos import *;
from Auxiliares import *;
 
class interfaceGame():
    player_turn = None;

    # Gamemode 0 -> Human vs Human
    # Gamemode 1 -> Human vs Computer
    def __init__(self, root, gamemode): 
        self.tictactoe = Game();
        self.master = root;
        self.build_root();
        #self.titulo = self.build_titulo();
        self.tabuleiro = self.build_tabuleiro();
        self.buttons = self.build_buttons();
        self.gamename = self.build_gamename();
        self.player_turn = self.build_turn();
        self.gameRunning = True;
        self.gamemode = gamemode; 
         
        self.master.bind("<Key>", self.restart_game);
    
    def restart_game(self, event):
        if (event.keysym == "Escape"):
            if (self.tictactoe.isOver()):
                self.tictactoe = Game();
                self.build_buttons();
                self.gameRunning = True;
                self.player_turn = self.build_turn();
            else:
                self.master.destroy();
    
    def play_in(self, l, c):  
        if self.gameRunning:
            if self.tictactoe.can_play(l, c):
                self.tictactoe.play(l, c);  
                self.atualize_tile(l, c);
        
            if self.tictactoe.isOver():
                self.endgame();
    
            if (self.gamemode == 1):
                self.machine_play_in();
    
            print(self.tictactoe.show());
    
    def machine_play_in(self):
        if self.gameRunning:
            # Guarda o tabuleiro antes e depois da maáquina jogar, para com 
            # base nisso determinar qual a posição que deve ter seu conteúdo
            # modificado
            
            state_after_machine_played = self.tictactoe.machine_play();

            old_state = self.tictactoe.state.corpo;
            new_state = state_after_machine_played.corpo;
            l, c = new_state.tilePlayed(old_state);

            self.tictactoe.changeState(state_after_machine_played);
            self.atualize_tile(l,c);

            if self.tictactoe.isOver():
                self.endgame();
    
    def atualize_tile(self, l : int, c : int):
        if (self.tictactoe.get_value(l,c) == 'X'):
            self.create_button(l, c, X_IMAGE);
        else:
            self.create_button(l, c, CIRCLE_IMAGE);
    
        self.player_turn = self.build_turn();
        
    def endgame(self):
        self.gameRunning = False;
        self.highlight_victory();
        self.player_turn = self.build_turn();
        
    def highlight_victory(self):
        victory_case = self.tictactoe.state.endgame_type;
        c = self.tictactoe.state.endgame_ref;

        print(victory_case);
        print(c);
        if (victory_case == "line"):
            self.build_buttons(marked=[(c, 0),
                                       (c, 1), 
                                       (c, 2)]);        
        if (victory_case == "column"):
            self.build_buttons(marked=[(0, c),
                                       (1, c),
                                       (2, c)]);
        
        if (victory_case == "main_diagonal"):
            self.build_buttons(marked=[(0,0),
                                       (1,1),
                                       (2,2)]);
        
        if (victory_case == "secondary_diagonal"):
            self.build_buttons(marked=[(0,2),
                                       (1,1),
                                       (2,0)]);
    
        if (victory_case == "toe"):
            self.build_buttons(marked=[(0,0), (0,1), (0,2),
                                       (1,0), (1,1), (1,2),
                                       (2,0), (2,1), (2,2)]);            
        
    def build_root(self):
        self.master.geometry(str(WIDTH_WINDOW) + 'x' + str(HEIGHT_WINDOW) + "+" + str(PADX_JANELA) + "+" + str(PADY_JANELA));
        #self.master.attributes('-fullscreen', True);
        self.master.title("Jogo da Velha");
        self.master.config(background=BACKGROUND_JANELA);

    def build_titulo(self):
        aux = Label(self.master, 
                    text=TEXTO_TITULO, 
                    font=FONTE_TITULO, 
                    bg=BACKGROUND_TITULO, 
                    fg=FOREGROUND_TITULO,
                    width=WIDTH_WINDOW);
        aux.pack();
        return aux;

    def build_gamename(self):
        visionImage = PhotoImage(file=IMG_GAMENAME);
        figura = Label(self.tabuleiro, image=visionImage);
        figura.image = visionImage;

        aux = Label(self.master,
                    background=BACKGROUND_JANELA,
                    image=visionImage,
                    width=WIDTH_GAMENAME,
                    height=HEIGHT_GAMENAME);
        aux.pack(padx=PADX_GAMENAME, 
                 pady=[PADY_TOP_GAMENAME, PADY_BOTTOM_GAMENAME]);
        return aux;

    def build_tabuleiro(self):
        aux = Frame(self.master, 
                    background=BACKGROUND_TABULEIRO,
                    width=WIDTH_TABULEIRO,
                    height=HEIGHT_TABULEIRO);

        aux.pack(side=LEFT, 
                 pady=PADY_TABULEIRO, 
                 padx=[PADX_ESQ_TABULEIRO, 0]);
        return aux;

    def build_buttons(self, marked : list = []):
        buttons = [];
        print("TABULEIRO : ");
        print(self.tictactoe.show());
        print("-------------");
        for i in range(0, 9):
            line, column = i//3, i%3;

            if (self.tictactoe.get_value(line, column) == 'X'):
                buttons.append(self.create_button(line, column, X_IMAGE));
            if (self.tictactoe.get_value(line, column) == 'O'):
                buttons.append(self.create_button(line, column, CIRCLE_IMAGE));
            if (self.tictactoe.get_value(line, column) == ' '):
                buttons.append(self.create_button(line, column));
        
            if contains(marked, (line, column)):
                buttons[i]["background"] = "#FFE66D";
        return buttons;

    def create_button(self, line, column, image_to_use = PIXEL_VIRTUAL):
        visionImage = PhotoImage(file=image_to_use);
        figura = Label(self.tabuleiro, image=visionImage);
        figura.image = visionImage;

        b = Button(self.tabuleiro, 
                    image=visionImage,
                    width=WIDTH_TABULEIRO//3, 
                    height=HEIGHT_TABULEIRO//3, 
                    command=lambda l=line, c=column: self.play_in(l, c),
                    compound="c");
        
        b.grid(row=line, 
               column=column);
        
        return b;

    def image_turn(self) -> str:
        #Essa função é chamada antes da jogada ser feita
        #Dessa forma, se for a vez do O, é porque ele acabou de jogar, e o próximo é o X. Ou seja, devo apresentar a imagem "vez do X"
        # Analogamente, se for a vez do X, então devo apresentar a imagem "vez do O" 
        if (self.tictactoe.isOver()):
            if (self.tictactoe.winner == "X"):
                return(IMG_VITORIA_X);
            if (self.tictactoe.winner == "O"):
                return(IMG_VITORIA_O);
            if (self.tictactoe.winner == "%"):
                return(IMG_EMPATE);
        else:
            if (self.tictactoe.turn == "O"):
                return(IMG_VEZ_O);
            else:
                return(IMG_VEZ_X);
    
    def build_turn(self):
        if (self.player_turn != None): 
            self.player_turn.pack_forget(); #Ao chamar a função, reescreve o componente no lugar de sua versão anterior
        
        image_to_use = self.image_turn();
        # print("TURNO : " + str(self.tictactoe.turn));
        # print(image_to_use);
        visionImage = PhotoImage(file=image_to_use);
        figura = Label(self.tabuleiro, image=visionImage);
        figura.image = visionImage;

        aux = Label(self.master,
                    background=BACKGROUND_JANELA,
                    image=visionImage,
                    width=WIDTH_TURN,
                    height=HEIGHT_TURN);
        aux.pack(padx=PADX_TURN, 
                 pady=PADY_TURN);
        return aux;

