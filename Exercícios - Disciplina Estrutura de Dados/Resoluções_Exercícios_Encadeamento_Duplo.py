# Aluno: Matheus Henrique Borsato
# Professor: Marco Aurélio Lopes Barbosa

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    ante: No | None
    item: int 
    prox: No | None


def lista_nos(lista: list[int]) -> No | None:
    '''
    Devolve um encadeamento duplo com os elementos de *lst*.

    Exemplos
    >>> lista_nos([])
    >>> lista_nos([4])
    No(ante=None, item=4, prox=None)
    >>> lista_nos([9, 2, 4])
    No(ante=None, item=9, prox=No(ante=..., item=2, prox=No(ante=..., item=4, prox=None)))
    '''
    
    if lista == []:
        return None

    inicio = No(None, lista[0], None)
    final = inicio

    for i in range(1, len(lista)):
        final.prox = No(final, lista[i], None)
        final = final.prox
        
    return inicio


def lista_nos_inversa(lista: list[int]) -> No | None:
    '''
    Devolve um encadeamento duplo com os elementos de *lst*, mas em ordem contrária.

    Exemplos
    >>> lista_nos_inversa([])
    >>> lista_nos_inversa([4])
    No(ante=None, item=4, prox=None)
    >>> lista_nos_inversa([9, 2, 4])
    No(ante=None, item=4, prox=No(ante=..., item=2, prox=No(ante=..., item=9, prox=None)))
    '''

    if lista == []:
        return None

    final = No(None, lista[0], None)
    inicio = final

    for i in range (1, len(lista)):
        inicio.ante = No(None, lista[i], inicio)
        inicio = inicio.ante

    lista_inversa = inicio

    return lista_inversa


def troca_prox(p: No):
    '''
    Troca *p* de lugar com *p.prox*.
    Requer que *p.prox* seja um No.

    Exemplos
    >>> p = lista_nos([7, 4, 6])
    >>> troca_prox(p)
    >>> p.ante
    No(ante=None, item=4, prox=No(ante=..., item=7, prox=No(ante=..., item=6, prox=None)))
    >>> p.item
    7
    >>> p.ante.item
    4
    >>> p.prox.item
    6
    '''
    assert p.prox is not None
    q = p.prox
    p.prox = q.prox
    if p.prox is not None:
        p.prox.ante = p
    q.ante = p.ante
    if q.ante is not None:
        q.ante.prox = q
    q.prox = p
    p.ante = q


def troca_ante(p: No):
    '''
    Troca *p* de lugar com *p.ante*.
    Requer que *p.ante* seja um No.

    Exemplos
    >>> p = lista_nos([7, 4, 6]).prox
    >>> troca_ante(p)
    >>> p
    No(ante=None, item=4, prox=No(ante=..., item=7, prox=No(ante=..., item=6, prox=None)))
    >>> p.item
    4
    >>> p.prox.item
    7
    >>> p.prox.prox.item
    6
    '''
    assert p.ante is not None
    troca_prox(p.ante)
    
    
def inverte(p: No | None) -> No | None:
    '''
    Inverte a ordem dos elementos de *p*.
    
    Exemplos
    >>> inverte(None)
    >>> inverte(No(None, 3, None))
    No(ante=None, item=3, prox=None)
    >>> inverte(lista_nos([6, 2, 4]))
    No(ante=None, item=4, prox=No(ante=..., item=2, prox=No(ante=..., item=6, prox=None)))
    >>> inverte(inverte(lista_nos([6, 2, 4])))
    No(ante=None, item=6, prox=No(ante=..., item=2, prox=No(ante=..., item=4, prox=None)))
    '''
    
    if p is None:
        return None
    
    q = p.prox
    p.prox = None
    
    while q is not None:
        prox = q.prox
        q.ante = None
        q.prox = p
        p.ante = q
        p = q
        q = prox
        
    return p
    
def insere_numero(p: No | None, n: int) -> No | None:
    '''
    Insere um nó com *n* mantendo *p* ordenado de forma não decrescente.
    
    Exemplos
    >>> insere_numero(None, 1)
    No(ante=None, item=1, prox=None)
    >>> insere_numero(No(None, 3, None), 5)
    No(ante=None, item=3, prox=No(ante=..., item=5, prox=None))
    >>> insere_numero(No(None, 5, None), 3)
    No(ante=None, item=3, prox=No(ante=..., item=5, prox=None))
    >>> insere_numero(lista_nos([4, 6, 10]), 2)
    No(ante=None, item=2, prox=No(ante=..., item=4, prox=No(ante=..., item=6, prox=No(ante=..., item=10, prox=None))))
    >>> insere_numero(lista_nos([4, 6, 10]), 5)
    No(ante=None, item=4, prox=No(ante=..., item=5, prox=No(ante=..., item=6, prox=No(ante=..., item=10, prox=None))))
    >>> insere_numero(lista_nos([4, 6, 10]), 8)
    No(ante=None, item=4, prox=No(ante=..., item=6, prox=No(ante=..., item=8, prox=No(ante=..., item=10, prox=None))))
    >>> insere_numero(lista_nos([4, 6, 10]), 12)
    No(ante=None, item=4, prox=No(ante=..., item=6, prox=No(ante=..., item=10, prox=No(ante=..., item=12, prox=None))))
    '''
    novo = No(None, n, None)
    
    if p is None:
        return novo

    q = p
    anterior = None
    
    while q is not None and q.item < n:
        anterior = q
        q = q.prox
        
    if anterior is None:
        novo.prox = p
        p.ante = novo
        p = novo
    else:    
        anterior.prox = novo
        novo.ante = anterior
        novo.prox = q
        if q is not None:
            q.ante = novo
            
    return p
