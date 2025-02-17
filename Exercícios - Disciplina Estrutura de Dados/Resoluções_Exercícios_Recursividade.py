# Aluno: Matheus Henrique Borsato
# Professor: Marco Aurélio Lopes Barbosa

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    primeiro: int
    resto: Lista


Lista = No | None


def algum_impar (lst: Lista) -> bool:
    '''
    Devolve True se algum dos elementos de *lst* for ímpar.
    Caso contrário, devolve False.

    Exemplos:
    >>> algum_impar(None)
    False
    >>> algum_impar(No(4, None))
    False
    >>> algum_impar(No(7, None))
    True
    >>> algum_impar(No(2, No(6, No(10, None))))
    False
    >>> algum_impar(No(2, No(5, No(10, None))))
    True
    '''
    if lst is None:
        return False
    else:
        return (lst.primeiro % 2) != 0 or \
                algum_impar (lst.resto)


def valor_maximo (lst: Lista) -> int | None:
    '''
    Devolve o valor máximo de *lst*.
    Devolve None se *lst* é vazia.

    Exemplos:
    >>> valor_maximo(None) is None
    True
    >>> valor_maximo(No(5, None))
    5
    >>> valor_maximo(No(2, No(1, No(19, No(6, None)))))
    19
    >>> valor_maximo(No(2, No(15, No(12, No(6, None)))))
    15
    '''
    if lst is None:
        return None
    else:
        m = valor_maximo(lst.resto)
        if m is None:
            return lst.primeiro
        elif lst.primeiro > m:
            m = lst.primeiro
        return m


def string_repetida (palavra: str, n: int) -> str:
    '''
    Devolve *palavra* repetida *n* vezes.

    Exemplos:
    >>> string_repetida('casa', 0)
    ''
    >>> string_repetida('mouse', 1)
    'mouse'
    >>> string_repetida('garrafa', 4)
    'garrafagarrafagarrafagarrafa'
    '''
    if n == 0:
        return ''
    else:
        return palavra + string_repetida (palavra, n - 1)


def numero_no_arranjo (lst: list[int], numero: int) -> int:
    '''
    Conta quantas vezes *n* aparece em *lst*

    Exemplos:
    >>> numero_no_arranjo([], 3)
    0
    >>> numero_no_arranjo([4,1], 1)
    1
    >>> numero_no_arranjo([4,2], 1)
    0
    >>> numero_no_arranjo([3, 4, 8, 10, 4, 3, 4], 4)
    3
    >>> numero_no_arranjo([3, 4, 8, 10, 4, 3, 4], 3)
    2
    >>> numero_no_arranjo([3, 4, 8, 10, 4, 3, 4], 2)
    0
    '''
    if lst == []:
        return 0
    elif lst[0] == numero:
        return 1 + numero_no_arranjo (lst[1:], numero)
    else:
        return numero_no_arranjo (lst[1:], numero)


def potencia (a: int, n: int) -> int:
    '''
    Calcula o valor de *a* elevado a *n*.
    Requer que *a* seja diferente de 0 e
    *n* seja um número natural.

    Exemplos:
    >>> potencia(8, 0)
    1
    >>> potencia(1, 8)
    1
    >>> potencia(2, 5)
    32
    >>> potencia(-3, 4)
    81
    >>> potencia(-5, 3)
    -125
    >>> potencia(6, 5)
    7776
    '''
    if n == 0:
        return 1
    else:
        return a * potencia(a, n-1) 


def lista_positivos (lst: Lista) -> Lista:
    '''
    Cria uma nova lista com os elementos positivos de *lst*.

    Exemplos:
    >>> lista_positivos(None) is None
    True
    >>> lista_positivos(No(-2, No(-3, None))) is None
    True
    >>> lista_positivos(No(1, No(-5, No(9, No(15, None)))))
    No(primeiro=1, resto=No(primeiro=9, resto=No(primeiro=15, resto=None)))
    >>> lista_positivos(No(0, No(-5, No(9, No(-15, None)))))
    No(primeiro=9, resto=None)
    '''
    if lst is None:
        return None
    elif lst.primeiro <= 0:
        return lista_positivos(lst.resto)
    else:
        return No(lst.primeiro, lista_positivos(lst.resto))


def tamanho_maximo (lst: list[str]) -> int:
    '''
    Devolve o tamanho da maior string de *lst*.

    Exemplos:
    >>> tamanho_maximo ([])
    0
    >>> tamanho_maximo (['Corinthians'])
    11
    >>> tamanho_maximo (['oi', 'carro', 'celular', 'casa'])
    7
    '''
    
    def __tamanho_maximo (lst: list[str], n: int) -> int:
        # devolve o tamanho máximo entre as primeiras *n* strings de *lst*.
        if n == 0:
            return 0
        else:
            return max(len(lst[n - 1]), __tamanho_maximo(lst, n - 1))
    return __tamanho_maximo (lst, len(lst))


def impar(n: int) -> bool:
    '''
    Devolve True se *n* é ímpar. 
    Caso contrário, devolve False.
    
    Requer quer n >= 0.
    
    Exemplos:
    >>> impar(0)
    False
    >>> impar(5)
    True
    >>> impar(4)
    False
    >>> impar(19)
    True
    '''
    assert n >= 0
    if n == 0:
        return False
    else:
        return par(n - 1)
    
    
def par(n: int) -> bool:
    '''
    Devolve True se *n* é par.
    Caso contrário, devolve False.
    
    Requer quer n >= 0.
    
    Exemplos: 
    >>> par(0)
    True
    >>> par(4)
    True
    >>> par(5)
    False
    >>> par(17)
    False
    '''
    assert n >= 0
    if n == 0:
        return True
    else:
        return impar(n - 1)
    
    
def nao_decrescente (lst: list[int]) -> bool:
    '''
    Devolve True se *lst* está em ordem não decrescente. 
    Devolve False, caso contrário.
    
    Exemplos:
    >>> nao_decrescente([])
    True
    >>> nao_decrescente([5])
    True
    >>> nao_decrescente([2, 1])
    False
    >>> nao_decrescente([4, 4, 4, 4])
    True
    >>> nao_decrescente([1, 2, 3, 4, 5])
    True
    >>> nao_decrescente([1, 2, 3, 4, 5, 4])
    False
    '''
    def __nao_decrescente(lst: list[int], n: int) -> bool:
    # verifica se os primeiros *n* números de *lst* estão em ordem não decrescente.
        if n == 1 or n == 0:
            return True
        else:
            return lst[n - 1] >= lst[n - 2] and __nao_decrescente(lst, n - 1)
    return __nao_decrescente(lst, len(lst))


def remove_zero (lst: Lista) -> Lista:
    '''
    Modifica *lst*, removendo todas as 
    ocorrências do valor 0.
    
    Exemplos:
    >>> remove_zero(None) is None
    True
    >>> remove_zero(No(0, No(0, None))) is None
    True
    >>> remove_zero(No(7, None))
    No(primeiro=7, resto=None)
    >>> remove_zero(No(1, No(0, None)))
    No(primeiro=1, resto=None)
    >>> remove_zero(No(0, No(8, No(9, No(0, No(6, None))))))
    No(primeiro=8, resto=No(primeiro=9, resto=No(primeiro=6, resto=None)))
    >>> remove_zero(No(8, No(0, No(9, No(0, No(4, None))))))
    No(primeiro=8, resto=No(primeiro=9, resto=No(primeiro=4, resto=None)))
    '''
    if lst is None:
        return None
    elif lst.primeiro == 0:
        return remove_zero(lst.resto)
    else:
        lst.resto = remove_zero(lst.resto)
        return lst
    
    
def divisores (x: int, n: int) -> list[int]:
    '''
    Cria um arranjo com os divisores de *n* 
    que são menores ou iguais a *x*.
    
    Requer que 0 <= *x* <= *n*
    
    Exemplos:
    >>> divisores(0, 12)
    []
    >>> divisores(28, 29)
    [1]
    >>> divisores(29, 29)
    [1, 29]
    >>> divisores(6, 12)
    [1, 2, 3, 4, 6]
    >>> divisores(12, 18)
    [1, 2, 3, 6, 9]
    >>> divisores(50, 100)
    [1, 2, 4, 5, 10, 20, 25, 50]
    '''
    assert 0 <= x <= n
    
    if x == 0:
        return []
    elif n % x != 0:
        return divisores (x - 1, n)
    else:
        return divisores (x - 1, n) + [x]
    
    
def prefixo(lsta: Lista, lstb: Lista) -> bool:
    '''
    Devolve True se *lsta* é prefixo de *lstb*, isto é, *lstb* começa com
    *lsta*. Devolve False caso contrário.

    Exemplos
    >>> prefixo(None, None)
    True
    >>> prefixo(None, No(10, No(20, None)))
    True
    >>> prefixo(No(10, None), None)
    False
    >>> prefixo(No(10, No(20, None)), No(10, No(20, No(30, No(40, None)))))
    True
    >>> prefixo(No(10, No(2, None)), No(10, No(20, No(30, No(40, None)))))
    False
    '''
    if lsta is None:
        return True
    elif lstb is None:
        return False
    else:
        return lsta.primeiro == lstb.primeiro and prefixo(lsta.resto, lstb.resto)


def ordena (lst: list[int]):
    '''
    Ordena os elementos de *lst* de modo
    não decrescente.
    
    Requer que len(lst) > 0.
    
    Exemplos:
    >>> lista = [5]
    >>> ordena(lista)
    >>> lista
    [5]
    >>> lista = [1, 7, 5, 3, 4]
    >>> ordena(lista)
    >>> lista
    [1, 3, 4, 5, 7]
    >>> lista.append(3)
    >>> lista
    [1, 3, 4, 5, 7, 3]
    >>> ordena(lista)
    >>> lista
    [1, 3, 3, 4, 5, 7]
    '''
    assert len(lst) > 0
    
    def __ordena (lst: list[int], tamanho: int):
        
        if tamanho < len(lst):
            __ordena(lst, tamanho + 1)
            maior_atual = maximo(lst[:tamanho + 1])
            lst[tamanho], lst[maior_atual] = lst[maior_atual], lst[tamanho]
            
    __ordena (lst, 0)
    
    
def maximo(lst: list[int]) -> int:
    '''
    Encontra o índice do valor máximo de *lst*.
    Requer que len(lst) > 0.

    Exemplos
    >>> maximo([3])
    0
    >>> maximo([3, 2])
    0
    >>> maximo([3, 2, 4])
    2
    >>> maximo([3, 9, 2, 4, 1])
    1
    '''
    assert len(lst) > 0
    
    def __maximo (lst: list[int], tamanho: int) -> int:

        if tamanho == 0:
            return 0
        else:
            m = __maximo(lst, tamanho - 1)
            if lst[tamanho] > lst[m]:
                m = tamanho
            return m
        
    return __maximo (lst, len(lst) - 1)
