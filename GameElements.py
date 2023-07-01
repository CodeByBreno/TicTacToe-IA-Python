from TabuleiroTicTacToe import *;
import random;

#A interface entre o visual do jogo e a lógica interna é a seguinte
#   - A parte externa deve fornecer quem está jogando no momento, o player1 ou player2
#   - Se o player que está jogando for humano, deve fornecer também onde será colocada a nova jogada
#   - Se o player for um robo, o sistema interno vai calcular sua jogada
#   - Em todo caso, o sistema interno retorna o desenho do tabuleiro após a nova jogada

class State():

    def __init__(self, first_player, matriz_creation : MatrizQuadrada | None = None):
        if matriz_creation == None:
            self.corpo = TabuleiroTicTacToe();
        else:
            self.corpo = TabuleiroTicTacToe(creation_body = matriz_creation);

        self.terminal = False;
        self.value = None;
        self.first_player = first_player;

    def initializeState(self):
        aux = self.corpo.analyse();

        self.terminal = aux["final"];
        self.value = self.valorSimbolo(aux["simbol"]);
        self.victory_type = aux["type"]; 
        self.ref_number = aux["ref_number"];
        self.count_o = aux["count_o"];
        self.count_x = aux["count_x"];
        return aux;
    
    def turn(self):
        total_jogadas = self.count_o + self.count_x;
        if ( (total_jogadas%2 == 0) == (self.first_player == "O") ): #É um XOR entre esses valores lógicos
            #Se um numero par de jogadas foi feita, e "O" começou, ele é o próximo a jogar
            #Se um numero ímpar de jogadas foi feita, e "X começou", então "O" é o próximo
            return "O"; 
        else:
            #Se um numero par de jogadas foi feita, e "X" começou, então ele é o próximo
            #Se um numero ímpar de jogadas foi feita, e "O" começou, então ele é o próximo
            return "X"; 
    
    def actions(self, player_symbol): 
        list_actions : list[State] = [];
        
        for linha in range(0, self.corpo.tabuleiro.dimensao):
            for coluna in range(0, self.corpo.tabuleiro.dimensao):
                if self.corpo.tabuleiro.get(linha, coluna) == " ":
                    possivel_jogada = self.corpo.tabuleiro.ifPut(player_symbol, linha, coluna);
                    new_state = State(self.first_player, matriz_creation = possivel_jogada);
                    list_actions.append(new_state);

        return list_actions;

    def minimax(self, turno = None):
        self.initializeState();

        if turno == None:
            turno = self.turn();

        if self.terminal == True:
            return self.value;
    
        if turno == "O":
            max = -2;
            for possible_play in self.actions(player_symbol = turno):
                possible_play.initializeState();
                value = possible_play.minimax("X");

                if value > max:
                    max = value;
            
            return max;
    
        if turno == "X":
            min = 2;
            for possible_play in self.actions(player_symbol = turno):
                possible_play.initializeState();
                value = possible_play.minimax("O");

                if value < min:
                    min = value;
            
            return min;

    def valorSimbolo(self, simbol):
        if simbol == "O":
            return 1;    #"O" é o MAX
        elif simbol == "X":
            return -1;   #"X" é o MIN
        elif simbol == "%":
            return 0;    #"%" é o TOE
        else:
            return None;

    def show(self):
        return self.corpo.tabuleiro.show();

    def put(self, value: str, i: int, j: int):
        valor_posicao = self.corpo.tabuleiro.get(i, j);

        if valor_posicao == " ":
            self.corpo.tabuleiro.put(value, i, j);
            return True;
        else:
            return False;

class Game():
    #Um jogo possui dois jogadores e um tabuleiro
    def __init__(self, modo = 1, player_simbol = "O", initial_state : list = None, first_player : str = None):
        
        if initial_state == None:
            self.turn = self.firstToPlay();
            self.state = State(self.turn);        
        else:
            new_state = State(first_player, matriz_creation = MatrizQuadrada(conteudo = initial_state, dimensao = 3))
            new_state.initializeState();
            self.turn = new_state.turn();
            self.state = new_state;

    def firstToPlay(self):
        if (random.randint(0,9) < 5):
            return "O";
        else:
            return "X";

    def getPlayers(self):
        return self.player1, self.player2;

    def tabuleiroAtual(self):
        return self.state.corpo.tabuleiro; #Retorna a matriz quadrada que representa o estado atual do state

    def play(self, linha: int, coluna: int):
        isPossible = self.state.put(self.turn, linha, coluna);

        if isPossible:
            self.alternateTurn();
            return("Jogada realizada com sucesso!")
        else:
            return("Essa jogada não é possivel! Já jogaram ai!");

    def changeState(self, next_state : State):
        self.state = next_state;
        self.alternateTurn();
        return ("Jogada realizada com sucesso");

    def show(self):
        return self.state.show();

    def isOver(self):
        self.state.initializeState();
        return self.state.terminal;

    def alternateTurn(self):
        if self.turn == "O":
            self.turn = "X";
        else:
            self.turn = "O";

class Player():

    def __init__(self, partida: Game, simbol: str, human = True):
        self.partida = partida;
        self.simbol = simbol;
        self.human = human;

    def play(self, linha = None, coluna = None):
        self.partida.state.tabuleiro.put(linha, coluna);
        return self.partida.tabuleiroAtual();

