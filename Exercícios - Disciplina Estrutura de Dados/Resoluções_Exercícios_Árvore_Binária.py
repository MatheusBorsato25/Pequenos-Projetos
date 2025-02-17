# Aluno: Matheus Henrique Borsato
# Professor: Marco Aurélio Lopes Barbosa

from __future__ import annotations
from dataclasses import dataclass

r'''
Desenhe uma árvore binária como os elementos 3, 6, 8, 20, 21, 22, 23, 30, 40, 46, 50, 60 de maneira
que qualquer busca binária em um arranjo com esses elementos ou na árvore se comporte da mesma
forma (como o exemplo do material).

              22
            /    \
         /          \
        8           40  
      /   \       /    \
     3     20    23    50
      \      \    \   /  \
       6     21   30 46  60
'''

@dataclass
class No:
    esq: Arvore
    val: int
    dir: Arvore
    
Arvore = No | None

def numero_elementos (t: Arvore) -> int:
    r'''
    Conta a quantidade de elementos de *t*.
    Exemplos:

          t4  6
            /   \
          /       \
    t2  3          9  t3
      /   \      /   \
     0  t1 4    7      15 t0
            \         /  \ 
             5       12  20
             
    >>> t0 = No(No(None, 12, None), 15, No(None, 20, None))
    >>> t1 = No(None, 4, No(None, 5, None))
    >>> t2 = No(No(None, 0, None), 3, t1)
    >>> t3 = No(No(None, 7, None), 9, t0)
    >>> t4 = No(t2, 6, t3)
    >>> numero_elementos(None)
    0
    >>> numero_elementos(t0)
    3
    >>> numero_elementos(t1)
    2
    >>> numero_elementos(t2)
    4
    >>> numero_elementos(t3)
    5
    >>> numero_elementos(t4)
    10
    '''
    if t is None:
        return 0
    else:
        return 1 + numero_elementos(t.esq) + numero_elementos(t.dir)
    
def grau_dois (t: Arvore) -> int:
    r'''
    Conta a quantidade de nós com grau 2 de *t*.
    
    Exemplos:

          t4  6
            /   \
          /       \
    t2  3          9  t3
      /   \      /   \
     0  t1 4    7      15 t0
            \         /  \ 
             5       12  20
             
    >>> t0 = No(No(None, 12, None), 15, No(None, 20, None))
    >>> t1 = No(None, 4, No(None, 5, None))
    >>> t2 = No(No(None, 0, None), 3, t1)
    >>> t3 = No(No(None, 7, None), 9, t0)
    >>> t4 = No(t2, 6, t3)
    >>> grau_dois(None)
    0
    >>> grau_dois(t0)
    1
    >>> grau_dois(t1)
    0
    >>> grau_dois(t2)
    1
    >>> grau_dois(t3)
    2
    >>> grau_dois(t4)
    4
    '''
    if t is None:
        return 0
    elif t.esq is not None and t.dir is not None:
        return 1 + grau_dois(t.esq) + grau_dois(t.dir)
    else:
        return grau_dois(t.esq) + grau_dois (t.dir)
    

def cheia (t: Arvore) -> bool:
    r'''
    Verifica se *t* é uma árvore cheia, ou seja, se todos os 
    seus nós tem grau 0 ou 2. Devolve True se *t* for cheia 
    e False, caso contrário.
     
    Exemplos:

               t6  6
                 /   \
               /       \
          t4  2          9  t5
            /   \      /   \
       t3 0    t2 4   7     15 t1
        /   \   /   \      /    
    t0-1     1 3     5    12   
    
    >>> t0 = No(None, -1, None)
    >>> t1 = No(No(None, 12, None), 15, None)
    >>> t2 = No(No(None, 3, None), 4, No(None, 5, None))
    >>> t3 = No(t0, 0, No(None, 1, None))
    >>> t4 = No(t3, 2, t2)
    >>> t5 = No(No(None, 7, None), 9, t1)
    >>> t6 = No(t4, 6, t5)
    >>> cheia(None)
    True
    >>> cheia(t0)
    True
    >>> cheia(t1)
    False
    >>> cheia(t2)
    True
    >>> cheia(t3)
    True
    >>> cheia(t4)
    True
    >>> cheia(t5)
    False
    >>> cheia(t6)
    False
    >>> t2.esq = None
    >>> cheia(t2)
    False
    >>> cheia(t4)
    False
    '''
    if t is None:
        return True
    elif (t.esq is not None and t.dir is not None) or (t.esq is None and t.dir is None):
        return cheia(t.esq) and cheia(t.dir)
    else:
        return False
    
    
def valor_maximo (t: Arvore) -> int | None:
    r'''
    Devolve o valor máximo entre os elementos de *t*. 
    Devolve None se a árvore estiver vazia.
    
    Exemplos:

        t4    6
            /   \
          /       \
    t2  3          15  t3
      /   \       /   \
    19  t1 4     8     2 t0
            \        /   \ 
            18      10    0 t5
    
    >>> t5 = No(None, 0, None)         
    >>> t0 = No(No(None, 10, None), 2, t5)
    >>> t1 = No(None, 4, No(None, 18, None))
    >>> t2 = No(No(None, 19, None), 3, t1)
    >>> t3 = No(No(None, 8, None), 15, t0)
    >>> t4 = No(t2, 6, t3)
    >>> valor_maximo(None) is None
    True
    >>> valor_maximo(t5)
    0
    >>> valor_maximo(t0)
    10
    >>> valor_maximo(t1)
    18
    >>> valor_maximo(t2)
    19
    >>> valor_maximo(t3)
    15
    >>> valor_maximo(t4)
    19
    '''
    def _maximo(a: int | None, b: int | None) -> int | None:
        if a is None:
            return b
        if b is None:
            return a
        else:
            return max(a, b)
    if t is None:
        return None
    else:
        return _maximo(t.val, _maximo(valor_maximo(t.esq), valor_maximo(t.dir)))
    
    
r'''
Desenhe a sequência de ABBs geradas pela inserção dos elementos 6, 1, 3, 7, 8, 12, 9, 5, 4, 2, 16.

     ins      ins              ins              ins                     ins                        ins
None --->  6  --->         6   --->        6    --->        6           --->          6            --->           6
      6        1         /      3       /        7       /     \         8         /     \          12         /     \
                        1              1               1         7               1         7                  1       7
                                        \               \                         \         \                  \       \
                                         3               3                         3         8                  3       8
                                                                                                                         \
                                                                                                                          12
                                                                                                                          
  ins                         ins                         ins                            ins                                       ins                   
  --->         6              --->          6             --->            6              --->               6                      --->                6
   9        /     \            5         /     \           4          /       \           2             /       \                   16             /       \     
           1       7                    1       7                    1         7                      1           7                              1           7         
            \       \                    \       \                    \         \                       \          \                               \           \
             3       8                    3       8                    3         8                       3          8                               3           8   
                      \                    \       \                     \        \                    /   \         \                            /   \          \
                       12                   5       12                    5        12                  2    5         12                          2    5          12
                       /                            /                    /         /                       /          /                               /           / \
                      9                            9                    4         9                       4          9                               4           9   16
'''                                                                                             

r'''
Partindo do resultado do exercício anterior, desenhe a sequência de ABBs geradas pela remoção dos
elementos 12, 1, 3, 6, 7, 8, 5, 9, 4, 2.

          6                                   6                                     6                                        6
      /       \              rem          /       \               rem           /       \                  rem           /       \
    1           7            --->       1           7             --->        3           7                --->        2           7
      \          \            12          \          \             1        /   \           \               3            \          \
       3          8                        3          8                    2     5           8                            5          8
     /   \         \                     /   \         \                        /             \                          /            \ 
     2    5         12                   2    5         9                      4               9                        4              9 
         /         /  \                      /           \                                      \                                       \
        4         9    16                   4             16                                     16                                     16
        
                  5                               5                               5                          4                               
              /       \                       /       \                       /       \                   /     \                      4
  rem        2         7           rem       2         8          rem        2         9         rem     2       9        rem        /   \         rem       2        rem 
  --->        \         \          --->       \         \         --->        \         \        --->             \       --->      2     16       --->       \       --->     16
   6           4         8          7          4         9         8           4         16       5               16       9                        4          16      2
                          \                               \   
                           9                               16
                            \
                             16                      
'''                         


def remove_negativo(t: Arvore):
    r'''
    Altera os elementos negativos de *t* 
    para seus valores absolutos.
    
    Requer que *t* não seja vazia.
    
    Exemplos:

          t4  6
            /   \
          /       \
    t2 -3          9  t3
      /   \      /   \
     0  t1 4   -7     -15 t0
            \         /  \ 
            -5       12  -20
             
    >>> t0 = No(No(None, 12, None), -15, No(None, -20, None))
    >>> t1 = No(None, 4, No(None, -5, None))
    >>> t2 = No(No(None, 0, None), -3, t1)
    >>> t3 = No(No(None, -7, None), 9, t0)
    >>> t4 = No(t2, 6, t3)
    >>> remove_negativo(t0)
    >>> t0
    No(esq=No(esq=None, val=12, dir=None), val=15, dir=No(esq=None, val=20, dir=None))
    >>> t1
    No(esq=None, val=4, dir=No(esq=None, val=-5, dir=None))
    >>> remove_negativo(t2)
    >>> t1
    No(esq=None, val=4, dir=No(esq=None, val=5, dir=None))
    '''
    if t is not None:
        remove_negativo(t.esq)
        remove_negativo(t.dir)
        if t.val < 0:
            t.val = t.val * (-1)
         
            
def eh_abb (t: Arvore) -> bool:
    r'''
    Verifica se *t* é uma árvore binária de busca (ABB). 
    Devolve True, caso seja e False, caso contrário.
     
    Exemplos:

               t6  6
                 /   \
               /       \
          t4  2          9  t5
            /   \      /   \
       t3 0    t2 4   7     15 t1
        /   \   /   \      /    
    t0-1     1 3     5    12  
    
    >>> t0 = No(None, -1, None)
    >>> t3 = No(t0, 0, No(None, 1, None))
    >>> t2 = No(No(None,3, None), 4, No(None, 5, None))
    >>> t4 = No(t3, 2, t2)
    >>> t1 = No(No(None, 12, None), 15, None)
    >>> t5 = No(No(None, 7, None), 9, t1)
    >>> t6 = No(t4, 6, t5)
    >>> eh_abb(None)
    True
    >>> eh_abb(t6)
    True
    >>> t5.val = 20
    >>> eh_abb(t6)
    False
    >>> eh_abb(t5)
    False
    >>> eh_abb(t1)
    True
    >>> eh_abb(t4)
    True
    >>> t3.val = 10
    >>> eh_abb(t4)
    False
    >>> eh_abb(t3)
    False
    >>> eh_abb(t0)
    True
    >>> eh_abb(t2)
    True
    '''
    
    if t is None:
        return True
    elif (t.esq is None or t.esq.val < t.val) and (t.dir is None or t.dir.val > t.val):
        return eh_abb(t.esq) and eh_abb(t.dir)
    else:
        return False
      
      
def eh_balanceada (t: Arvore) -> bool:
    r'''
    Verifica se *t* é uma árvore binária balanceada. 
    Devolve True, caso seja e False, caso contrário.
     
    Exemplos:

               t6  6
                 /   \
               /       \
          t4  2          9  t5
            /   \      /   \
       t3 0    t2 4   7     15 t1
        /   \   /   \      /    
    t0-1     1 3     5    12  
    
    >>> t0 = No(None, -1, None)
    >>> t3 = No(t0, 0, No(None, 1, None))
    >>> t2 = No(No(None,3, None), 4, No(None, 5, None))
    >>> t4 = No(t3, 2, t2)
    >>> t1 = No(No(None, 12, None), 15, None)
    >>> t5 = No(No(None, 7, None), 9, t1)
    >>> t6 = No(t4, 6, t5)
    >>> eh_balanceada(None)
    True
    >>> eh_balanceada(t6)
    True
    >>> eh_balanceada(t5)
    True
    >>> t5.esq = None
    >>> eh_balanceada(t6)
    False
    >>> eh_balanceada(t5)
    False
    >>> eh_balanceada(t1)
    True
    >>> eh_balanceada(t4)
    True
    >>> t2.esq = None
    >>> eh_balanceada(t2)
    True
    >>> eh_balanceada(t4)
    True
    >>> t4.dir = None
    >>> eh_balanceada(t4)
    False
    >>> eh_balanceada(t3)
    True
    '''
    if t is None:
        return True
    elif abs(altura(t.esq) - altura(t.dir)) <= 1:
        return eh_balanceada(t.esq) and eh_balanceada(t.dir)
    else:
        return False
    
    
def altura(t: Arvore) -> int:
    r'''
    Devolve a altura da árvore *t*. Devolve -1 se *t* é None.

    Exemplos:

          t4  9
            /   \
         /         \
    t2  8           6  t3
      /   \       /
     4  t1 7     5
            \
             2

    >>> t1 = No(None, 7, No(None, 2, None))
    >>> t2 = No(No(None, 4, None), 8, t1)
    >>> t3 = No(No(None, 5, None), 6, None)
    >>> t4 = No(t2, 9, t3)
    >>> altura(None)
    -1
    >>> altura(t1)
    1
    >>> altura(t4)
    3
    '''
    if t is None:
        return -1
    else:
        return 1 + max(altura(t.esq), altura(t.dir))


def sucessor(t: Arvore, n: int) -> int | None:
    r'''
    Devolve o sucessor de *n* em *t*, ou seja, 
    o menor valor maior que *n* em *t*. 
    Devolve None se não existe sucessor de *n*.

    Exemplos:

          t4  8
            /   \
         /         \
    t2  5           12  t3
      /   \       /
     4  t1 6     9
            \
             7

    >>> t1 = No(None, 6, No(None, 7, None))
    >>> t2 = No(No(None, 4, None), 5, t1)
    >>> t3 = No(No(None, 9, None), 12, None)
    >>> t4 = No(t2, 8, t3)
    >>> sucessor(t4, 8)
    9
    >>> sucessor(t4, 9)
    12
    >>> sucessor(t4, 12) is None
    True
    >>> sucessor(t4, 7)
    8
    >>> sucessor(t2, 7) is None
    True
    >>> sucessor(t4, 5)
    6
    >>> sucessor(t4, 6)
    7
    >>> sucessor(t4, 4)
    5
    >>> t4.dir = None
    >>> sucessor(t4, 8) is None
    True
    '''
    assert eh_abb(t) == True
    assert busca(t, n) == True
    
    if t is None:
        return None
    if n < t.val:
        possivel_sucessor = sucessor(t.esq, n)
        if possivel_sucessor is not None:
            return possivel_sucessor
        else:
            return t.val
    elif n > t.val:
        return sucessor(t.dir, n)
    else:
        if t.dir is not None:
            return menor_na_subarvore(t.dir)
        else:  
            return None


def busca(t: Arvore, val: int) -> bool:
    r'''
    Devolve True se *val* está em *t* e False caso contrário.

    Requer que *t* seja uma ABB.

    Exemplos
               t
             4
           /   \
         /       \
        1          7 
      /   \       /
    -3     2     5
            \
             3

    >>> no_esq = No(No(None, -3, None), 1, No(None, 2, No(None, 3, None)))
    >>> no_dir = No(No(None, 5, None), 7, None)
    >>> t = No(no_esq, 4, no_dir)
    >>> busca(None, 10)
    False
    >>> busca(t, 0)
    False
    >>> busca(t, 1)
    True
    >>> busca(t, 2)
    True
    >>> busca(t, 3)
    True
    >>> busca(t, 4)
    True
    >>> busca(t, 5)
    True
    >>> busca(t, 6)
    False
    >>> busca(t, 7)
    True
    '''
    if t is None:
        return False
    elif val == t.val:
        return True
    elif val < t.val:
        return busca(t.esq, val)
    else:  # val > t.val
        return busca(t.dir, val)
    
    
def menor_na_subarvore(t: Arvore) -> int:
    r'''
    Devolve o menor valor de *t*.

    Exemplos:

          t4  8
            /   \
         /         \
    t2  5           12  t3
      /   \       /
     4  t1 6     9
            \
             7

    >>> t1 = No(None, 6, No(None, 7, None))
    >>> t2 = No(No(None, 4, None), 5, t1)
    >>> t3 = No(No(None, 9, None), 12, None)
    >>> t4 = No(t2, 8, t3)
    >>> menor_na_subarvore(t4)
    4
    >>> menor_na_subarvore(t3)
    9
    '''
    assert t is not None
    if t.esq is None:
        return t.val
    else:
        return menor_na_subarvore(t.esq)


def menor_na_arvore(t: Arvore) -> int | None:
    r'''
    Devolve o menor valor de *t*. Devolve None
    se *t* é vazia.

    Exemplos:

          t4  8
            /   \
         /         \
    t2  5           12  t3
      /   \       /
     2  t1 6     10
            \
             7

    >>> t1 = No(None, 6, No(None, 7, None))
    >>> t2 = No(No(None, 2, None), 5, t1)
    >>> t3 = No(No(None, 10, None), 12, None)
    >>> t4 = No(t2, 8, t3)
    >>> menor_na_arvore(None) is None
    True
    >>> menor_na_arvore(t4)
    2
    >>> menor_na_arvore(t3)
    10
    '''
    if t is None:
        return None
    if t.esq is None:
        return t.val
    else:
        return menor_na_arvore(t.esq)
    
    
def maior_na_arvore(t: Arvore) -> int | None:
    r'''
    Devolve o maior valor de *t*. Devolve None
    se *t* é vazia.

    Exemplos:

          t4  8
            /   \
         /         \
    t2  5           12  t3
      /   \       /
     2  t1 6     10
            \
             7

    >>> t1 = No(None, 6, No(None, 7, None))
    >>> t2 = No(No(None, 2, None), 5, t1)
    >>> t3 = No(No(None, 10, None), 12, None)
    >>> t4 = No(t2, 8, t3)
    >>> maior_na_arvore(None) is None
    True
    >>> maior_na_arvore(t4)
    12
    >>> maior_na_arvore(t2)
    7
    '''
    if t is None:
        return None
    if t.dir is None:
        return t.val
    else:
        return maior_na_arvore(t.dir)
    
    
def amplitude(t: Arvore) -> int:
    r'''
    Devolve o amplitude de *t*, ou seja, 
    a diferença entre o valor máximo e mínimo.

    Requer que *t* seja não vazia.
    
    Exemplos:

          t4  8
            /   \
         /         \
    t2  5           12  t3
      /   \       /
     2  t1 6     10
            \
             7

    >>> t1 = No(None, 6, No(None, 7, None))
    >>> t2 = No(No(None, 2, None), 5, t1)
    >>> t3 = No(No(None, 10, None), 12, None)
    >>> t4 = No(t2, 8, t3)
    >>> amplitude(t4)
    10
    >>> amplitude(t2)
    5
    >>> amplitude(t3)
    2
    >>> amplitude(t1)
    1
    >>> t1.dir = None
    >>> amplitude(t1)
    0
    >>> t3.dir = No(None, 100, None)
    >>> amplitude(t3)
    90
    >>> amplitude(t4)
    98
    >>> t2.esq = None
    >>> amplitude(t4)
    95
    >>> t4.esq = None
    >>> amplitude(t4)
    92
    '''
    assert t is not None
    maior = maior_na_arvore(t.dir)
    menor = menor_na_arvore(t.esq)
    if maior is not None and menor is not None:
        return maior - menor
    elif maior is None and menor is not None:
        return t.val - menor
    elif menor is None and maior is not None:
        return maior - t.val
    else:
        return t.val - t.val
    
    
def arranjo_crescente(t: Arvore) -> list[int]:
    r'''
    Cria um arranjo ordenado em ordem crescente 
    a partir dos valores *t*.
    
    Requer que *t* seja uma ABB.
    
    Exemplos:

          t4  8
            /   \
         /         \
    t2  5           12  t3
      /   \       /   \
     2  t1 6     10    15  t0
            \
             7

    >>> t0 = No(None, 15, None)
    >>> t1 = No(None, 6, No(None, 7, None))
    >>> t2 = No(No(None, 2, None), 5, t1)
    >>> t3 = No(No(None, 10, None), 12, t0)
    >>> t4 = No(t2, 8, t3)
    >>> arranjo_crescente(None)
    []
    >>> arranjo_crescente(t0)
    [15]
    >>> arranjo_crescente(t1)
    [6, 7]
    >>> arranjo_crescente(t2)
    [2, 5, 6, 7]
    >>> arranjo_crescente(t3)
    [10, 12, 15]
    >>> arranjo_crescente(t4)
    [2, 5, 6, 7, 8, 10, 12, 15]
    '''
    assert eh_abb(t) == True
    if t is None:
        return []
    else:
        return arranjo_crescente(t.esq) + [t.val] + arranjo_crescente(t.dir)
     
     
def arranjo_decrescente(t: Arvore) -> list[int]:
    r'''
    Cria um arranjo ordenado em ordem decrescente 
    a partir dos valores *t*.
    
    Requer que *t* seja uma ABB.
    
    Exemplos:

          t4  8
            /   \
         /         \
    t2  5           12  t3
      /   \       /   \
     2  t1 6     10    15  t0
            \
             7

    >>> t0 = No(None, 15, None)
    >>> t1 = No(None, 6, No(None, 7, None))
    >>> t2 = No(No(None, 2, None), 5, t1)
    >>> t3 = No(No(None, 10, None), 12, t0)
    >>> t4 = No(t2, 8, t3)
    >>> arranjo_decrescente(None)
    []
    >>> arranjo_decrescente(t0)
    [15]
    >>> arranjo_decrescente(t1)
    [7, 6]
    >>> arranjo_decrescente(t2)
    [7, 6, 5, 2]
    >>> arranjo_decrescente(t3)
    [15, 12, 10]
    >>> arranjo_decrescente(t4)
    [15, 12, 10, 8, 7, 6, 5, 2]
    '''
    assert eh_abb(t) == True
    if t is None:
        return []
    else:
        return arranjo_decrescente(t.dir) + [t.val] + arranjo_decrescente(t.esq)
    
    
def cria_arvore(lst: list[int]) -> Arvore:
    '''
    Cria uma ABB a partir de *lst*, 
    sendo ele um arranjo ordenado de modo crescente. 
    
    Exemplos:
    >>> cria_arvore([]) is None
    True
    >>> cria_arvore([2])
    No(esq=None, val=2, dir=None)
    >>> cria_arvore([2, 3])
    No(esq=None, val=2, dir=No(esq=None, val=3, dir=None))
    >>> cria_arvore([2, 3, 5])
    No(esq=No(esq=None, val=2, dir=None), val=3, dir=No(esq=None, val=5, dir=None))
    >>> cria_arvore([2, 3, 5, 7])
    No(esq=No(esq=None, val=2, dir=None), val=3, dir=No(esq=None, val=5, dir=No(esq=None, val=7, dir=None)))
    >>> cria_arvore([1, 2, 3, 4, 5, 6, 7])
    No(esq=No(esq=No(esq=None, val=1, dir=None), val=2, dir=No(esq=None, val=3, dir=None)), val=4, dir=No(esq=No(esq=None, val=5, dir=None), val=6, dir=No(esq=None, val=7, dir=None)))
    '''
    if lst == []:
        return None
    else:
        inicio = 0
        fim = len(lst) - 1
        m = (inicio + fim) // 2
        return No(cria_arvore(lst[:m]), lst[m], cria_arvore(lst[m + 1:]))
    
    
def insere_iterativa(t: Arvore, val: int) -> No:
    '''
    Devolve a raiz da ABB que é o resultado da inserção de *val* em *t*.
    Se *val* já está em *t*, devolve *t*.

    Requer que *t* seja uma ABB.

    Exemplos:
    >>> r = None
    >>> r = insere_iterativa(r, 7)
    >>> r
    No(esq=None, val=7, dir=None)
    >>> r = insere_iterativa(r, 7)
    >>> r
    No(esq=None, val=7, dir=None)
    >>> r = insere_iterativa(r, 3)
    >>> r
    No(esq=No(esq=None, val=3, dir=None), val=7, dir=None)
    >>> r = insere_iterativa(r, 12)
    >>> r
    No(esq=No(esq=None, val=3, dir=None), val=7, dir=No(esq=None, val=12, dir=None))
    >>> r = insere_iterativa(r, 4)
    >>> r
    No(esq=No(esq=None, val=3, dir=No(esq=None, val=4, dir=None)), val=7, dir=No(esq=None, val=12, dir=None))
    >>> r = insere_iterativa(r, 10)
    >>> r
    No(esq=No(esq=None, val=3, dir=No(esq=None, val=4, dir=None)), val=7, dir=No(esq=No(esq=None, val=10, dir=None), val=12, dir=None))
    >>> r = insere_iterativa(r, 11)
    >>> r
    No(esq=No(esq=None, val=3, dir=No(esq=None, val=4, dir=None)), val=7, dir=No(esq=No(esq=None, val=10, dir=No(esq=None, val=11, dir=None)), val=12, dir=None))
    >>> r = insere_iterativa(r, 1)
    >>> r
    No(esq=No(esq=No(esq=None, val=1, dir=None), val=3, dir=No(esq=None, val=4, dir=None)), val=7, dir=No(esq=No(esq=None, val=10, dir=No(esq=None, val=11, dir=None)), val=12, dir=None))
    >>> r = insere_iterativa(r, 9)
    >>> r
    No(esq=No(esq=No(esq=None, val=1, dir=None), val=3, dir=No(esq=None, val=4, dir=None)), val=7, dir=No(esq=No(esq=No(esq=None, val=9, dir=None), val=10, dir=No(esq=None, val=11, dir=None)), val=12, dir=None))
    '''
    novo = No(None, val, None)
    if t is None:
        return novo
    p: No | None = t
    pai = None
    while p is not None:
        pai = p
        if val < p.val:
            p = p.esq
        elif val > p.val:
            p = p.dir 
        else:
            return t
    if pai is not None:
        if pai.val < val:
            pai.dir = novo
        else:
            pai.esq = novo
    return t


def remove_iterativa(t: Arvore, val: int) -> Arvore:
    r'''
    Devolve a raiz da ABB que é o resultado da remoção de *val* em *t*.
    Se *val* não está em *t*, devolve *t*.
    Se *t* só tem um nó e *val* está nesse nó, devolve None.

    Requer que *t* seja uma ABB.

    Exemplos

         5
       /   \
     /       \
    1         10
     \       /
      3     6
     / \     \
    2   4     8

    >>> r = None
    >>> for val in [5, 1, 3, 10, 6, 4, 8, 2]:
    ...     r = insere_iterativa(r, val)
    >>> r = remove_iterativa(r, 4)
    >>> r
    No(esq=No(esq=None, val=1, dir=No(esq=No(esq=None, val=2, dir=None), val=3, dir=None)), val=5, dir=No(esq=No(esq=None, val=6, dir=No(esq=None, val=8, dir=None)), val=10, dir=None))
    >>> # Remoção de nó interno sem filho a esquerda
    >>> r = remove_iterativa(r, 1)
    >>> r
    No(esq=No(esq=No(esq=None, val=2, dir=None), val=3, dir=None), val=5, dir=No(esq=No(esq=None, val=6, dir=No(esq=None, val=8, dir=None)), val=10, dir=None))
    >>> # Remoção de nó interno sem filho a direita
    >>> r = remove_iterativa(r, 10)
    >>> r
    No(esq=No(esq=No(esq=None, val=2, dir=None), val=3, dir=None), val=5, dir=No(esq=None, val=6, dir=No(esq=None, val=8, dir=None)))
    >>> # Remoção de nó interno com dois filhos
    >>> r = remove_iterativa(r, 5)
    >>> r
    No(esq=No(esq=None, val=2, dir=None), val=3, dir=No(esq=None, val=6, dir=No(esq=None, val=8, dir=None)))
    >>> r = remove_iterativa(r, 10)
    >>> r
    No(esq=No(esq=None, val=2, dir=None), val=3, dir=No(esq=None, val=6, dir=No(esq=None, val=8, dir=None)))
    >>> r = remove_iterativa(r, 3)
    >>> r
    No(esq=None, val=2, dir=No(esq=None, val=6, dir=No(esq=None, val=8, dir=None)))
    >>> r = remove_iterativa(r, 2)
    >>> r
    No(esq=None, val=6, dir=No(esq=None, val=8, dir=None))
    >>> r = remove_iterativa(r, 6)
    >>> r
    No(esq=None, val=8, dir=None)
    >>> r = remove_iterativa(r, 8)
    >>> r is None
    True
    >>> r = remove_iterativa(r, 8)
    >>> r is None
    True
    '''
    if t is None:
        return None
    p: No | None = t
    pai = None
    while p is not None and p.val != val:
        pai = p
        if val < p.val:
            p = p.esq
        else:
            p = p.dir
    if p is None:
        return t
    if p.esq is None and p.dir is None:
        if pai is None: 
            return None
        if pai.esq == p:
            pai.esq = None
        else:
            pai.dir = None
        return t
    elif p.esq is None or p.dir is None:
        if p.esq is not None:
            filho = p.esq
        elif p.dir is not None:
            filho = p.dir
        if pai is None:  # Nó removido é a raiz
            return filho
        if pai.esq == p:
            pai.esq = filho
        else:
            pai.dir = filho
        return t
    else:
        m = maximo(p.esq)  
        p.val = m  
        removido: No | None = p.esq
        pai_removido = p
        while removido is not None and removido.val != m:
            pai_removido = removido
            removido = removido.dir
        if pai_removido and removido:
            if pai_removido.esq == removido:
                pai_removido.esq = removido.esq
            else:
                pai_removido.dir = removido.esq
    return t


def maximo(t: No) -> int:
    '''
    Encontra o valor máximo em *t*.

    Requer que *t* seja uma ABB.

    Exemplos
    >>> r = None
    >>> for val in [5, 1, 2, 7, 6, 3, 8, 4]:
    ...     r = insere_iterativa(r, val)
    >>> maximo(r)
    8
    '''
    while t.dir is not None:
        t = t.dir
    return t.val
