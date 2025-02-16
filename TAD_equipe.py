from dataclasses import dataclass
from enum import Enum

class Posição (Enum):
    GOLEIRO = 1
    DEFENSOR = 2
    MEIO_CAMPO = 3
    ATACANTE = 4

@dataclass
class Jogador:
    nome: str
    posicao: Posição
    
@dataclass 
class Removido:
    pass

CAPACIDADE_INICIAL = 30
FATOR_CRESCIMENTO = 2.0
FATOR_DECRESCIMENTO = 0.5

class Equipe:
    '''
    Permite o gerenciamento de aspectos de uma Equipe, sendo eles o nome, o orçamento, 
    os jogadores e suas posições.
    
    Exemplos:
    >>> e = Equipe('Felicidade', 1000000)
    >>> e.informa_nome()
    'Felicidade'
    >>> e.altera_nome('Alegria')
    >>> e.informa_nome()
    'Alegria'
    >>> e.capacidade_jogadores()
    30
    >>> e.informa_orcamento()
    '1000000.00'
    >>> e.receita(300000)
    >>> e.despesa(500000)
    >>> e.informa_orcamento()
    '800000.00'
    >>> e.adiciona_jogador('Matheus', 3)
    >>> e.adiciona_jogador('Thiago', 2)
    >>> e.adiciona_jogador('Pedro', 4)
    >>> e.adiciona_jogador('Caio', 1)
    >>> e.adiciona_jogador('Gabriel', 4)
    >>> e.adiciona_jogador('Paulo', 2)
    >>> e.adiciona_jogador('Rogério', 1)
    >>> e.adiciona_jogador('Miguel', 3)
    >>> e.adiciona_jogador('Bruno', 3)
    >>> e.total_jogadores()
    9
    >>> e.lista_jogadores()
    'Caio - GOLEIRO, Rogério - GOLEIRO, Paulo - DEFENSOR, Thiago - DEFENSOR, Bruno - MEIO_CAMPO, Matheus - MEIO_CAMPO, Miguel - MEIO_CAMPO, Gabriel - ATACANTE, Pedro - ATACANTE'
    >>> e.remove_jogador('Eduardo', 3)
    >>> e.remove_jogador('Rogério', 4)
    >>> e.adiciona_jogador('Matheus', 3)  
    >>> e.adiciona_jogador('Thiago', 2)
    >>> e.total_jogadores()
    9
    >>> e.total_goleiros()
    2
    >>> e.total_defensores()
    2
    >>> e.total_meias()
    3
    >>> e.total_atacantes()
    2
    >>> e.remove_jogador('Rogério', 1)
    >>> e.remove_jogador('Caio', 1)
    >>> e.remove_jogador('Paulo', 2)
    >>> e.adiciona_jogador('Caio', 1)
    >>> e.adiciona_jogador('Caio', 2)
    >>> e.total_jogadores()
    8
    >>> e.lista_jogadores() 
    'Caio - GOLEIRO, Caio - DEFENSOR, Thiago - DEFENSOR, Bruno - MEIO_CAMPO, Matheus - MEIO_CAMPO, Miguel - MEIO_CAMPO, Gabriel - ATACANTE, Pedro - ATACANTE'
    >>> e.total_goleiros()
    1
    >>> e.total_defensores()
    2
    >>> e.total_meias()
    3
    >>> e.total_atacantes()
    2
    >>> e.receita(150000)
    >>> e.informa_orcamento()
    '950000.00'
    >>> e.despesa(1000000)
    Traceback (most recent call last):
    ...
    ValueError: Impossível realizar essa operação! O orçamento não pode ser negativo!
    >>> e.despesa(950000)
    >>> e.informa_orcamento()
    '0.00'
    '''
    nome: str
    orcamento: float
    jogadores: list[None | Removido | Jogador]
    posicoes_jogadores: list[int]
    numero_jogadores: int
    numero_jogadores_removidos: int
    
    def __init__(self, nome_time: str, orcamento_inicial: float) -> None:
        '''
        Inicializa uma nova equipe com *nome_time* e *orçamento_inicial*.
        '''
        self.nome = nome_time
        self.orcamento = orcamento_inicial
        self.jogadores = [None] * CAPACIDADE_INICIAL
        self.posicoes_jogadores = [0, 0, 0, 0]
        self.numero_jogadores = 0
        self.numero_jogadores_removidos = 0

    def informa_nome(self) -> str:
        '''
        Devolve o nome da equipe.
        
        Exemplos:
        >>> e = Equipe('Time A', 500000)
        >>> e.informa_nome()
        'Time A'
        '''
        return self.nome
    
    def altera_nome(self, novo: str):
        '''
        Altera o nome da equipe atual por *novo*.
        
        Exemplos:
        >>> e = Equipe('Time A', 500000)
        >>> e.altera_nome('Time B')
        >>> e.informa_nome()
        'Time B'
        '''
        self.nome = novo
    
    def capacidade_jogadores(self):
        '''
        Retorna a capacidade máxima atual de jogadores na equipe.
        
        Exemplos:
        >>> e = Equipe('Time A', 500000)
        >>> e.capacidade_jogadores()
        30
        '''
        return len(self.jogadores)
    
    def receita(self, valor: float):
        '''
        Adiciona *valor* ao orçamento da equipe.
        
        Exemplos:
        >>> e = Equipe('Time A', 500000)
        >>> e.receita(200000)
        >>> e.informa_orcamento()
        '700000.00'
        '''
        self.orcamento += valor
    
    def despesa(self, valor: float):
        '''
        Remove *valor* do orçamento da equipe.
        
        Não permite que o orçamento fique negativo.
        
        Exemplos:
        >>> e = Equipe('Time A', 500000)
        >>> e.despesa(300000)
        >>> e.informa_orcamento()
        '200000.00'
        >>> e.despesa(300000)
        Traceback (most recent call last):
        ...
        ValueError: Impossível realizar essa operação! O orçamento não pode ser negativo!
        '''  
        if self.orcamento - valor < 0.0:
            raise ValueError("Impossível realizar essa operação! O orçamento não pode ser negativo!")
        else:
            self.orcamento -= valor
    
    def informa_orcamento(self) -> str:
        '''
        Retorna o orçamento formatado da equipe.
        
        Exemplos:
        >>> e = Equipe('Time A', 500000)
        >>> e.informa_orcamento()
        '500000.00'
        '''
        return f'{self.orcamento:.2f}'
    
    def adiciona_jogador(self, nome: str, posicao: int):
        '''
        Adiciona *nome* com sua respectiva *posicao* nos
        jogadores da equipe. Se o jogador já está presente, 
        não altera nada.
        
        Requer que *posicao* esteja entre 1 e 4.
        - *posicao* = 1 -> GOLEIRO
        - *posicao* = 2 -> DEFENSOR
        - *posicao* = 3 -> MEIO_CAMPO
        - *posicao* = 4 -> ATACANTE
        
        Exemplos:
        >>> e = Equipe('Time A', 500000)
        >>> e.adiciona_jogador('Pedro', 1)
        >>> e.adiciona_jogador('Pedro', 1)
        >>> e.adiciona_jogador('Pedro', 2)
        >>> e.adiciona_jogador('Matheus', 4)
        >>> e.adiciona_jogador('Gabriel', 0)
        Traceback (most recent call last):
        ...
        ValueError: Posição inválida!
        >>> e.lista_jogadores()
        'Pedro - GOLEIRO, Pedro - DEFENSOR, Matheus - ATACANTE'
        '''
        if posicao < 1 or posicao > 4:
            raise ValueError("Posição inválida!")
        
        if self.numero_jogadores + self.numero_jogadores_removidos == 0.7 * self.capacidade_jogadores():
            self.__redispersiona(FATOR_CRESCIMENTO)
            
        posicao_enum = Posição(posicao)
        indice = self.__calcula_hash(nome, self.capacidade_jogadores())
        
        existe_jogador = False
        while self.jogadores[indice] is not None and not existe_jogador:
            jogador = self.jogadores[indice]
            if isinstance(jogador, Jogador) and jogador == Jogador(nome, posicao_enum):
                existe_jogador = True
            indice = (indice + 1) % self.capacidade_jogadores()
            
        if self.jogadores[indice] is not None and not existe_jogador:
            self.numero_jogadores_removidos -= 1
        if not existe_jogador:
            self.jogadores[indice] = Jogador(nome, posicao_enum)
            self.numero_jogadores += 1
            self.__atualiza_campo_posicoes(posicao, 1)
    
    def remove_jogador(self, nome: str, posicao: int):
        '''
        Remove *nome* com sua respectiva *posicao* dos
        jogadores da equipe. Se o jogador não está presente, 
        não altera nada.
        
        Requer que *posicao* esteja entre 1 e 4.
        - *posicao* = 1 -> GOLEIRO
        - *posicao* = 2 -> DEFENSOR
        - *posicao* = 3 -> MEIO_CAMPO
        - *posicao* = 4 -> ATACANTE
        
        Exemplos:
        >>> e = Equipe('Time A', 500000)
        >>> e.adiciona_jogador('Pedro', 1)
        >>> e.adiciona_jogador('Thiago', 2)
        >>> e.adiciona_jogador('Matheus', 4)
        >>> e.remove_jogador('Matheus', 0)
        Traceback (most recent call last):
        ...
        ValueError: Posição inválida!
        >>> e.remove_jogador('Rafael', 3)
        >>> e.remove_jogador('Thiago', 1)
        >>> e.remove_jogador('Pedro', 1)
        >>> e.lista_jogadores()
        'Thiago - DEFENSOR, Matheus - ATACANTE'
        '''
        if posicao < 1 or posicao > 4:
            raise ValueError("Posição inválida!")
        
        posicao_enum = Posição(posicao)
        indice = self.__calcula_hash(nome, self.capacidade_jogadores())
        
        while self.jogadores[indice] is not None:
            if self.jogadores[indice] == Jogador(nome, posicao_enum):
                self.jogadores[indice] = Removido()
                self.numero_jogadores -= 1
                self.numero_jogadores_removidos += 1
                self.__atualiza_campo_posicoes(posicao, -1)
            indice = (indice + 1) % self.capacidade_jogadores()
        
        if self.capacidade_jogadores() > CAPACIDADE_INICIAL and self.numero_jogadores == 0.25 * self.capacidade_jogadores():
            self.__redispersiona(FATOR_DECRESCIMENTO)
            
    def lista_jogadores(self) -> str:
        '''
        Devolve uma string formatada com os jogadores da
        equipe, contendo seus nomes e posições, estando elas na seguinte
        ordem (GOLEIRO -> DEFENSOR -> MEIO_CAMPO -> ATACANTE)
        
        Exemplos:
        >>> e = Equipe('Time A', 500000)
        >>> e.adiciona_jogador('Pedro', 1)
        >>> e.adiciona_jogador('Thiago', 2)
        >>> e.adiciona_jogador('Matheus', 4)
        >>> e.adiciona_jogador('Rafael', 3)
        >>> e.lista_jogadores()
        'Pedro - GOLEIRO, Thiago - DEFENSOR, Rafael - MEIO_CAMPO, Matheus - ATACANTE'
        >>> e.remove_jogador('Thiago', 2)
        >>> e.lista_jogadores()
        'Pedro - GOLEIRO, Rafael - MEIO_CAMPO, Matheus - ATACANTE'
        '''
        lista: list[Jogador] = []
        
        for elemento in self.jogadores:
            if elemento is not None and isinstance(elemento, Jogador):
                lista.append(elemento)    
        
        ordena_intercalacao(lista)
        
        jogadores_str: list[str] = []
        for jogador in lista:
            jogadores_str.append(f"{jogador.nome} - {jogador.posicao.name}")
        
        return ", ".join(jogadores_str)
    
    def total_jogadores(self) -> int:
        '''
        Devolve o total de jogadores da equipe.
        
        Exemplos:
        >>> e = Equipe('Time A', 500000)
        >>> e.total_jogadores()
        0
        >>> e.adiciona_jogador('Pedro', 1)
        >>> e.adiciona_jogador('Thiago', 2)
        >>> e.adiciona_jogador('Matheus', 4)
        >>> e.adiciona_jogador('Rafael', 3)
        >>> e.total_jogadores()
        4
        >>> e.remove_jogador('Thiago', 2)
        >>> e.total_jogadores()
        3
        '''
        return self.numero_jogadores
    
    def total_goleiros(self) -> int:
        '''
        Devolve o total de goleiros da equipe.
        
        Exemplos:
        >>> e = Equipe('Time A', 500000)
        >>> e.total_goleiros()
        0
        >>> e.adiciona_jogador('Pedro', 1)
        >>> e.adiciona_jogador('Thiago', 2)
        >>> e.adiciona_jogador('Matheus', 1)
        >>> e.total_goleiros()
        2
        >>> e.remove_jogador('Matheus', 1)
        >>> e.total_goleiros()
        1
        '''
        return self.posicoes_jogadores[0]
    
    def total_defensores(self) -> int:
        '''
        Devolve o total de defensores da equipe.
        
        Exemplos:
        >>> e = Equipe('Time A', 500000)
        >>> e.total_defensores()
        0
        >>> e.adiciona_jogador('Pedro', 2)
        >>> e.adiciona_jogador('Thiago', 2)
        >>> e.adiciona_jogador('Matheus', 1)
        >>> e.total_defensores()
        2
        >>> e.remove_jogador('Pedro', 2)
        >>> e.total_defensores()
        1
        '''
        return self.posicoes_jogadores[1]
    
    def total_meias(self) -> int:
        '''
        Devolve o total de meio-campistas da equipe.
        
        Exemplos:
        >>> e = Equipe('Time A', 500000)
        >>> e.total_meias()
        0
        >>> e.adiciona_jogador('Pedro', 3)
        >>> e.adiciona_jogador('Thiago', 3)
        >>> e.adiciona_jogador('Matheus', 3)
        >>> e.total_meias()
        3
        >>> e.remove_jogador('Pedro', 3)
        >>> e.total_meias()
        2
        '''
        return self.posicoes_jogadores[2]
    
    def total_atacantes(self) -> int:
        '''
        Devolve o total de atacantes da equipe.
        
        Exemplos:
        >>> e = Equipe('Time A', 500000)
        >>> e.total_atacantes()
        0
        >>> e.adiciona_jogador('Pedro', 4)
        >>> e.adiciona_jogador('Thiago', 3)
        >>> e.adiciona_jogador('Matheus', 4)
        >>> e.adiciona_jogador('Roberto', 4)
        >>> e.total_atacantes()
        3
        >>> e.remove_jogador('Pedro', 4)
        >>> e.total_atacantes()
        2
        '''
        return self.posicoes_jogadores[3]
    
    def __redispersiona(self, fator: float):
        '''
        Gera uma nova tabela de dispersão para o conjunto, com base no valor de *fator*.
        Dobra o tamanho da tabela, se *fator* = FATOR_CRESCIMENTO = 2.0, 
        diminui pela metade se *fator* = FATOR_DECRESCIMENTO = 0.5.
        
        Requer *fator* = FATOR_CRESCIMENTO (2.0) ou *fator* = FATOR_DECRESCIMENTO (0.5).
        '''
        assert fator == FATOR_CRESCIMENTO or fator == FATOR_DECRESCIMENTO
        if fator == FATOR_CRESCIMENTO:
            nova_capacidade = int(self.capacidade_jogadores() * FATOR_CRESCIMENTO)
        else: # fator == FATOR_DECRESCIMENTO
            nova_capacidade = int(self.capacidade_jogadores() * FATOR_DECRESCIMENTO)
            
        aux = Equipe(self.nome, self.orcamento)
        aux.jogadores = [None] * (nova_capacidade)
        for jogador in self.jogadores:
            if jogador != None and isinstance(jogador, Jogador):
                aux.adiciona_jogador(jogador.nome, jogador.posicao.value)
        self.jogadores = aux.jogadores
        self.numero_jogadores_removidos = 0
        
    def __calcula_hash(self, nome: str, tamanho: int) -> int:
        '''
        Calcula o hash de *nome* e o padroniza para 
        uma capacidade entre 0 e (*tamanho* - 1).  
        '''
        calculo = hash(nome) % tamanho
        return calculo
        
    def __atualiza_campo_posicoes(self, posicao_value: int, operacao: int):
        '''
        Atualiza a quantidade de jogadores de *posicao* em *lista*
        com base em *operacao*.
    
        Se *operacao* == 1 -> Aumenta em 1 o número de jogadores de *posicao*.
        Se *operacao* == -1 -> Diminui em 1 o número de jogadores de *posicao*.
        '''
        assert operacao == 1 or operacao == - 1
        indice = posicao_value - 1  
        self.posicoes_jogadores[indice] += operacao 
 
def ordena_intercalacao(lst: list[Jogador]):
    '''
    Ordena *lst*, uma lista de jogadores utilizando o algoritmo Merge Sort (ordenação por intercalação).
    
    Complexidade: O(n lg n), onde n é o número de elementos de *lst*.
    '''
    if len(lst) > 1:
        m = len(lst) // 2
        a = lst[:m]
        b = lst[m:]
        ordena_intercalacao(a)
        ordena_intercalacao(b)
        intercala(lst, a, b)

def intercala(lst: list[Jogador], a: list[Jogador], b: list[Jogador]):
    '''
    Faz a intercalação em ordem dos elementos
    de *a* e *b* e armazena o resultado em *lst*.

    Requer que len(lst) = len(a) + len(b).

    Os critérios de ordenação são os seguintes:
    1. A posição do jogador (Goleiro -> Defensor -> Meio_Campo -> Atacante);
    2. Ordem alfabética.
    '''
    assert len(lst) == len(a) + len(b)
    
    i = 0; j = 0; k = 0
    while i < len(a) and j < len(b):
        if a[i].posicao.value < b[j].posicao.value:
            lst[k] = a[i]
            i += 1
        elif a[i].posicao.value > b[j].posicao.value:
            lst[k] = b[j]
            j += 1
        else:
            if a[i].nome <= b[j].nome:
                lst[k] = a[i]
                i += 1
            else:
                lst[k] = b[j]
                j += 1
        k += 1
        
    while i < len(a):
        lst[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        lst[k] = b[j]
        j += 1
        k += 1   
        