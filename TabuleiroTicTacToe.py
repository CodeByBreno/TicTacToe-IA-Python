from MatrizQuadrada import *;

class TabuleiroTicTacToe:
    def __init__(self, creation_body: list | MatrizQuadrada | None = None):
        
        if isinstance(creation_body, list):
            self.tabuleiro= MatrizQuadrada(creation_body, 3);
        elif isinstance(creation_body, MatrizQuadrada):
            self.tabuleiro = creation_body;
        else: 
            self.tabuleiro = MatrizQuadrada(" ", 3, fullfill=True);
    
    def analyse(self):
        resultado = AnalisadorTabuleiro(self).data;
        resultado["count_o"], resultado["count_x"] = self.count();

        return resultado;

    def show(self):
        return self.tabuleiro.show();

    def count(self):
        count_o = 0;
        count_x = 0;

        for i in range(0, self.tabuleiro.dimensao):
            for j in range(0, self.tabuleiro.dimensao):
                if (self.tabuleiro.get(i, j) == "O"):
                    count_o += 1;
                elif (self.tabuleiro.get(i, j) == "X"):
                    count_x += 1;

        return [count_o, count_x];

    def isFull(self):
        for i in range(0, self.tabuleiro.tamanho):
            if (self.tabuleiro.corpo[i] == " "):
                return False;
        return True;

#Analisa a estrutura atual do tabuleiro passado como parâmetro na criação
#Determina tudo que tem de relevante em uma única rodada de código
# - Se o tabuleiro está em um estado final ou não
# - Se estiver num estado final, dá o simbolo do vencedor
# - Também determina o tipo de vitória (linha, coluna, diagonal, etc)
# - Para os casos de vitória linha e coluna, indica o valor da linha ou coluna onde houve vitória
# - também retorna a quantidade de "O" e "X" já jogados

class AnalisadorTabuleiro():

    def __init__(self, tab_analisado: TabuleiroTicTacToe):
        self.tab_analisado = tab_analisado;
        self.data = self.statistics();
    
    #Em ambas as análises, o procedimento é análogo
    # - Primeiro, pego o valor inicial da linha/coluna/diagonal que estou analisando
    # - Se esse valor for " ", já passo para a próxima linha/coluna/diagonal, porque concerteza não terei uma sequencia de 
    #   três nessa
    # - Caso não seja " ", já aproveito para incrementar meu contador de "O" ou o de "X"
    # - Em seguida, guardo esse primeiro valor. Irei usa-lo como referência de comparação. Finalizo o ciclo interno e passo para
    #   o próximo elemento da linha/coluna/diagonal que estou analisando
    # - Verifico se o valor nessa posição é igual ao que guardei antes. Se for, passo para o próximo simbolo na linha/coluna/diagonal
    #   Se não for, paro de analisar essa linha/coluna/diagonal e passo para a próxima linha/coluna/diagonal
    # - Por fim, caso o valor tenha sido igual ao inicial, analiso o próximo. Se ele também for igual aos anteriores, então
    #   temos um vencedor. Retorno todas as informações relevantes a respeito de tal vitória
    def analise_perpendicular(self, tipo):

        for externo in range(0, self.tab_analisado.tabuleiro.dimensao):
            firstCycle = True;
            countOcorrencies = 0;

            for interno in range(0, self.tab_analisado.tabuleiro.dimensao):
                if tipo == "line": aux = self.tab_analisado.tabuleiro.get(externo, interno);
                elif tipo == "column": aux = self.tab_analisado.tabuleiro.get(interno, externo);

                if aux == " ": 
                    break;
                
                if firstCycle:                       
                    simbol = aux;
                    firstCycle = False;
                else:
                    if aux != simbol:              
                        break;                       
                    else:                   
                        countOcorrencies += 1;
                        if countOcorrencies == 2:    
                            return {"final": True,   
                                    "simbol": simbol, 
                                    "type": tipo, 
                                    "ref_number": externo};
        return {"final": False,   
                "simbol": None, 
                "type": None, 
                "ref_number": None};           

    def analise_diagonal(self, tipo):
        firstCycle = True;
        countOcorrencies = 0;

        for c in range(0, 3):
            if tipo == "main_diagonal": aux = self.tab_analisado.tabuleiro.get(c,c);
            elif tipo == "secondary_diagonal": aux = self.tab_analisado.tabuleiro.get(c,2-c);

            if aux == " ": 
                break;
            
            if firstCycle:
                simbol = aux;
                firstCycle = False;
            else:
                if aux != simbol:
                    break;
                else:
                    countOcorrencies += 1;
                    if countOcorrencies == 2:
                        return {"final": True,   
                                "simbol": simbol, 
                                "type": tipo, 
                                "ref_number": None};     
    
        return {"final": False,   
                "simbol": None, 
                "type": None, 
                "ref_number": None};     
 
    def statistics(self):
        aux = self.analise_perpendicular("line");
        if aux["final"] == True:
            return aux;
    
        aux = self.analise_perpendicular("column");
        if aux["final"] == True:
            return aux;
    
        aux = self.analise_diagonal("main_diagonal");
        if aux["final"] == True:
            return aux;
    
        aux = self.analise_diagonal("secondary_diagonal");
        if aux["final"] == True:
            return aux;
    
        if self.tab_analisado.isFull() == False:
            return aux; #Jogo em andamento
        else:
            return {"final": True,   
                    "simbol": "%", 
                    "type": "Toe", 
                    "ref_number": None}; 
