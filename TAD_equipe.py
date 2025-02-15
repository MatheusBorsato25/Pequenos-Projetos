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

class Equipe:
    '''
    '''
    nome: str
    orcamento: float
    jogadores: list[None | Removido | Jogador]
    posicoes_jogadores: list[int]
    numero_jogadores: int
    numero_jogadores_removidos: int
    
    
    def __init__(self, nome_time: str, orcamento_inicial: float) -> None:
        '''
        '''
        self.nome = nome_time
        self.orcamento = orcamento_inicial
        self.jogadores = [None] * CAPACIDADE_INICIAL
        self.posicoes_jogadores = [0, 0, 0, 0]
        self.numero_jogadores = 0
        self.numero_jogadores_removidos = 0

    def informa_nome(self) -> str:
        '''
        '''
        return self.nome
    
    def altera_nome(self, novo: str):
        '''
        '''
        self.nome = novo
    
    def capacidade_jogadores(self):
        '''
        '''
        return len(self.jogadores)
    
    def receita(self, valor: float):
        '''
        '''
        self.orcamento += valor
    
    def despesa(self, valor: float):
        
        if self.orcamento - valor < 0.0:
            raise ValueError("Impossível realizar essa operação! O orçamento deve se manter positivo!")
        else:
            self.orcamento -= valor
    
    def informa_orcamento(self) -> str:
        '''
        '''
        return f'{self.orcamento:.2f}'
    
    def adiciona_jogador(self, nome: str, posicao: Posição):
        '''
        '''
        indice = calcula_hash(nome, self.capacidade_jogadores())
        
        existe_jogador = False
        while self.jogadores[indice] is not None and not existe_jogador:
            jogador = self.jogadores[indice]
            if isinstance(jogador, Jogador) and jogador.nome == nome:
                existe_jogador = True
            indice = (indice + 1) % self.capacidade_jogadores()
            
        if self.jogadores[indice] is not None and not existe_jogador:
            self.numero_jogadores_removidos -=1
        if not existe_jogador:
            self.jogadores[indice] = Jogador(nome, posicao)
            self.numero_jogadores+= 1
        
        atualiza_campo_posicoes(self.posicoes_jogadores, posicao, 1)
    
    def remove_jogador(self, nome: str, posicao: Posição):
        '''
        '''
        indice = calcula_hash(nome, self.capacidade_jogadores())
        
        while self.jogadores[indice] is not None:
            if self.jogadores[indice] == Jogador(nome, posicao):
                self.jogadores[indice] = Removido()
                self.numero_jogadores -= 1
                self.numero_jogadores_removidos += 1
            indice = (indice + 1) % self.capacidade_jogadores()
        
        atualiza_campo_posicoes(self.posicoes_jogadores, posicao, -1)   
    
    def lista_jogadores(self) -> str:
        
        lista: list[Jogador] = []
        
        for elemento in self.jogadores:
            if elemento is not None and isinstance(elemento, Jogador):
                lista.append(elemento)    
        
        ordena_intercalacao(lista)
        
        jogadores_str: list[str] = []
        
        for jogador in lista:
            jogadores_str.append(f"{jogador.nome} - {jogador.posicao.name}")
        
        return " ,".join(jogadores_str)
    
    def total_jogadores(self):
        '''
        '''
        return self.numero_jogadores
    
    def total_goleiros(self):
        '''
        '''
        return self.posicoes_jogadores[0]
    
    def total_defensores(self):
        '''
        '''
        return self.posicoes_jogadores[1]
    
    def total_meias(self):
        '''
        '''
        return self.posicoes_jogadores[2]
    
    def total_atacantes(self):
        '''
        '''
        return self.posicoes_jogadores[3]
     
def calcula_hash(nome: str, tamanho: int) -> int:
    '''
    Calcula o hash de *nome* e o padroniza para 
    uma capacidade entre 0 e (*tamanho* - 1).  
    '''
    calculo = hash(nome) % tamanho
    return calculo
        
def atualiza_campo_posicoes(lista: list[int], posicao: Posição, operacao: int):
    '''
    '''
    indice = posicao.value - 1  
    lista[indice] += operacao  
      
      
def ordena_intercalacao(lst: list[Jogador]):
    '''
    Ordena *lst*, uma lista de jogadores utilizando o algoritmo Merge Sort (ordenação por intercalação).
    
    Complexidade: O(n lg n), onde n é o número de elementos na lista.
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
    1. A posição do jogador;
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
            if a[i].nome <= b[i].nome:
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