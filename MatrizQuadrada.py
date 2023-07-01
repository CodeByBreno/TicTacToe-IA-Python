class MatrizQuadrada():

    def __init__ (self, conteudo: list | object, dimensao: int, fullfill = False):
        
        if (len(conteudo) != dimensao*dimensao and len(conteudo) != 1):
            quit("A conteudo passado não corresponde ao tamanho da matriz");
        
        self.tamanho = dimensao*dimensao;
        self.dimensao = dimensao;

        if fullfill:
            self.corpo = self.fullfill(conteudo);
        else:
            self.corpo = conteudo;

    def get(self, i: int, j: int):
        return self.corpo[i*self.dimensao + j];

    def show(self):
        resultado = [];
        for i in range(0, self.dimensao):
            for j in range(0,self.dimensao):
                resultado.append(str(self.get(i,j)) + " ");
            resultado.append("\n");
        return "".join(resultado);

    def put(self, value, i: int, j: int):
        self.corpo[i*self.dimensao + j] = value;
        return value;

    def copy(self):
        new_corpo = [];
        for i in range(0, len(self.corpo)):
            new_corpo.append(self.corpo[i]);
        
        return MatrizQuadrada(conteudo = new_corpo, dimensao = self.dimensao);

    def ifPut(self, value, i: int, j: int):
        matriz = self.copy();
        matriz.corpo[i*matriz.dimensao + j] = value;
        return matriz;

    def fullfill(self, valor):
        resultado = [];
        for i in range(0, self.dimensao):
            for j in range(0, self.dimensao):
                resultado.append(valor);
        
        self.corpo = resultado; #Atualizo o valor do corpo da matriz com uma lista totalmente preenchida com o valor enviado

        return resultado; #Retorno a lista com o mesmo valor repetido várias vezes - fullfill da matriz -
