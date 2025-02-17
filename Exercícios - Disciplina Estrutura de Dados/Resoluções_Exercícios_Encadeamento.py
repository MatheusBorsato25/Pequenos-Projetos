# Aluno: Matheus Henrique Borsato
# Professor: Marco Aurélio Lopes Barbosa

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    item: int
    prox: No | None


def cria_encadeamento_contrario(lista: list[int]) -> No | None:
    '''
    Cria um encadeamento com os itens de *lista*, mas em ordem contrária.

    Exemplos:
    >>> cria_encadeamento_contrario ([]) is None
    True
    >>> cria_encadeamento_contrario ([1])
    No(item=1, prox=None)
    >>> cria_encadeamento_contrario ([4, 5, 7])
    No(item=7, prox=No(item=5, prox=No(item=4, prox=None)))
    '''
    
    p = None
    
    for numero in lista:
        p = No(numero, p)

    return p


def cria_encadeamento(lista: list[int]) -> No | None:
    '''
    Cria um encadeamento com os itens de *lista*

    Exemplos:
    >>> cria_encadeamento ([]) is None
    True
    >>> cria_encadeamento ([1])
    No(item=1, prox=None)
    >>> cria_encadeamento ([4, 5, 7])
    No(item=4, prox=No(item=5, prox=No(item=7, prox=None)))
    '''

    if lista == []:
        return None
    else:
        p = No(lista[0], None)
        q = p
        for numero in lista[1:]:
            q.prox = No(numero, None)
            q = q.prox        
        return p 


def soma_encadeamento (p: No | None) -> int:
    '''
    Determina a soma dos itens que estão em *p*.

    Exemplos:
    >>> soma_encadeamento(None)
    0
    >>> soma_encadeamento(No(10, None))
    10
    >>> soma_encadeamento(No(20, No(10, None)))
    30
    >>> soma_encadeamento(No(4, No(20, No(10, None))))
    34
    '''
    soma = 0

    q = p
    while q is not None:
        soma += q.item
        q = q.prox
        
    return soma

def valor_maximo_encadeamento (p: No) -> int:
    '''
    Determina qual o valor máximo dos itens que estão em *p*.

    Requer que *p* tenha ao menos um item.

    Exemplos:
    >>> valor_maximo_encadeamento(No(10, None))
    10
    >>> valor_maximo_encadeamento(No(20, No(10, None)))
    20
    >>> valor_maximo_encadeamento(No(20, No(25, No(24, No(10, None)))))
    25
    '''

    valor_maximo: int = p.item
    
    q = p.prox
    
    while q is not None:
        if q.item > valor_maximo:
            valor_maximo = q.item
        q = q.prox

    return valor_maximo


def adiciona_no(n: int, p: No | None) -> No:
    '''
    Cria um novo encadeamento, adicionando *n*, 
    como um novo nó, no final de *p*.

    Exemplos:
    >>> adiciona_no(4, None)
    No(item=4, prox=None)
    >>> adiciona_no(7, No(10, None))
    No(item=10, prox=No(item=7, prox=None))
    >>> adiciona_no(1, No(20, No(10, None)))
    No(item=20, prox=No(item=10, prox=No(item=1, prox=None)))
    >>> adiciona_no(25, No(4, No(20, No(10, None))))
    No(item=4, prox=No(item=20, prox=No(item=10, prox=No(item=25, prox=None))))
    '''
    if p is None:
        return No(n, None)
    else:
        q = p
        while q.prox is not None:
            q = q.prox    
        q.prox = No(n, None)
    
        return p
