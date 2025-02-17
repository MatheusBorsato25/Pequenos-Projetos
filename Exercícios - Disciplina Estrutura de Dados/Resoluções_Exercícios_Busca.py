# Aluno: Matheus Henrique Borsato
# Professor: Marco Aurélio Lopes Barbosa

# Considere um arranjo com os valores 3, 6, 8, 9, 20, 21, 22, 23, 30, 40, 45, 46, 50, 60 e diga quais são os
#índices dos valores que são comparados com a chave em uma busca binária para cada uma das chaves: 6, 30, 41, 50, 70.

# [3, 6, 8, 9, 20, 21, 22, 23, 30, 40, 45, 46, 50, 60]
# Chave 6 - Índices: 6, 2, 0, 1
# Chave 30 - Índices: 6, 10, 8
# Chave 41 - Índices: 6, 10, 8, 9
# Chave 50 - Índices: 6, 10, 12
# Chave 70 - Índices: 6, 10, 12, 13

def busca_binaria(valores: list[int], chave: int) -> int:
    '''
    Se *chave* está presente em *valores*, devolve o índice i tal que
    *valores[i] == chave*. Senão devolve o índice i tal que a inserção de
    *chave* na posição *i* de *valores* mantém *valores* em ordem não
    crescente.

    Requer que *valores* esteja em ordem não crescente.

    Exemplos

    >>> busca_binaria([], 10)
    0
    >>> busca_binaria([7], 4)
    1
    >>> busca_binaria([7], 8)
    0
    >>> busca_binaria([7], 7)
    0
    >>> busca_binaria([20, 12, 10, 8, 6], 4)
    5
    >>> busca_binaria([20, 12, 10, 8, 6], 6)
    4
    >>> busca_binaria([20, 12, 10, 8, 6], 7)
    4
    >>> busca_binaria([20, 12, 10, 8, 6], 9)
    3
    >>> busca_binaria([20, 12, 10, 8, 6], 10)
    2
    >>> busca_binaria([20, 12, 10, 8, 6], 11)
    2
    >>> busca_binaria([20, 12, 10, 8, 6], 12)
    1
    >>> busca_binaria([20, 12, 10, 8, 6], 17)
    1
    >>> busca_binaria([20, 12, 10, 8, 6], 20)
    0
    >>> busca_binaria([20, 12, 10, 8, 6], 21)
    0
    '''

    ini = 0
    fim = len(valores) - 1
    while ini <= fim:
        m = (ini + fim) // 2
        if chave == valores[m]:
            return m
        elif chave > valores[m]:
            fim = m - 1
        else: # chave > valores[m]
            ini = m + 1
    return ini


def busca_binaria_recursiva(valores: list[int], chave: int) -> int:
    '''
    Se *chave* está presente em *valores*, devolve o índice i tal que
    *valores[i] == chave*. Senão devolve o índice i tal que a inserção de
    *chave* na posição *i* de *valores* mantém *valores* em ordem não
    decrescente.

    Requer que *valores* esteja em ordem não decrescente.

    Exemplos

    >>> busca_binaria_recursiva([], 10)
    0
    >>> busca_binaria_recursiva([7], 4)
    0
    >>> busca_binaria_recursiva([7], 8)
    1
    >>> busca_binaria_recursiva([7], 7)
    0
    >>> busca_binaria_recursiva([6, 8, 10, 12, 20], 7)
    1
    >>> busca_binaria_recursiva([6, 8, 10, 12, 20], 10)
    2
    >>> busca_binaria_recursiva([6, 8, 10, 12, 20], 11)
    3
    >>> busca_binaria_recursiva([6, 8, 10, 12, 20], 12)
    3
    >>> busca_binaria_recursiva([6, 8, 10, 12, 20], 17)
    4
    >>> busca_binaria_recursiva([6, 8, 10, 12, 20], 20)
    4
    >>> busca_binaria_recursiva([6, 8, 10, 12, 20], 21)
    5

    Testes de propriedade

    O teste a seguir cria uma lista 0, 2, ..., 98 e realiza uma busca binária
    para 0, 1, 2, ..., 99.

    >>> lst = list(range(0, 100, 2))
    >>> for i in range(100):
    ...     assert busca_binaria_recursiva(lst, i) == (i + 1) // 2
    '''

    def _busca_binaria(lst: list[int], chave: int, inicio: int, fim: int) -> int:
        if fim < inicio:
            return inicio
        else: # inicio <= fim:
            m = (inicio + fim) // 2
            if chave == lst[m]:
                return m
            elif chave < lst[m]:
                return _busca_binaria(lst, chave, inicio, m - 1)
            else: # chave > lst[m]
                return _busca_binaria(lst, chave, m + 1, fim)
    return _busca_binaria(valores, chave, 0, len(valores) - 1)


def busca_primeira_ocorrencia(valores: list[int], chave: int) -> int:
    '''
    Se *chave* está presente em *valores*, devolve o índice i da primeira ocorrência
    de *chave* no arranjo. Senão devolve o índice i tal que a inserção de
    *chave* na posição *i* de *valores* mantém *valores* em ordem não
    decrescente.

    Requer que *valores* esteja em ordem não decrescente.

    Exemplos

    >>> busca_primeira_ocorrencia([], 10)
    0
    >>> busca_primeira_ocorrencia([7], 4)
    0
    >>> busca_primeira_ocorrencia([7], 8)
    1
    >>> busca_primeira_ocorrencia([7], 7)
    0
    >>> busca_primeira_ocorrencia([6, 8, 8, 8, 20], 7)
    1
    >>> busca_primeira_ocorrencia([6, 8, 8, 8, 10], 8)
    1
    >>> busca_primeira_ocorrencia([6, 8, 8, 8, 10], 10)
    4
    >>> busca_primeira_ocorrencia([6, 6, 6, 6, 6], 6)
    0
    >>> busca_primeira_ocorrencia([6, 8, 12, 12, 12, 12, 12, 12, 12], 12)
    2
    '''
    ini = 0
    fim = len(valores) - 1
    while ini <= fim:
        m = (ini + fim) // 2
        if chave == valores[m]:
            if m == 0 or chave != valores[m - 1]:
                return m
            else:
                fim = m - 1
        elif chave < valores[m]:
            fim = m - 1
        else: # chave > valores[m]
            ini = m + 1
    return ini


def raiz_quadrada (n: int) -> int:
    '''
    Calcula a raiz quadrada inteira de *n*, se ela existir.
    Devolve -1 se *n* não tiver raiz quadrada inteira.
    
    Requer que *n* seja não negativo.
    
    Exemplos:
    >>> raiz_quadrada(0)
    0
    >>> raiz_quadrada(1)
    1
    >>> raiz_quadrada(4)
    2
    >>> raiz_quadrada(9)
    3
    >>> raiz_quadrada(16)
    4
    >>> raiz_quadrada(25)
    5
    >>> raiz_quadrada(576)
    24
    >>> raiz_quadrada(2)
    -1
    >>> raiz_quadrada(10)
    -1
    '''
    assert n >= 0
    
    inicio = 0
    fim = n
    while inicio <= fim:
        m = (inicio + fim) // 2
        if m * m == n:
            return m
        elif m * m < n:
            inicio = m + 1
        else: # m * m > n
            fim = m - 1
    return -1
