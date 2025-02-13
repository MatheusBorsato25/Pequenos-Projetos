# Simulador - Campeonato Brasileiro
# Autor: Matheus Henrique Borsato

from dataclasses import dataclass


@dataclass
class Equipe:
    '''
    Representa uma equipe participante do campeonato.

    Atributos:
        nome (str): Nome da equipe;
        pontos (int): Pontuação total da equipe no campeonato;
        jogos (int): Número total de jogos disputados;
        vitorias (int): Número total de vitórias;
        empates (int): Número total de empates;
        derrotas (int): Número total de derrotas;
        gols_marcados (int): Total de gols marcados pela equipe;
        gols_sofridos (int): Total de gols sofridos pela equipe;
        saldo_gols (int): Diferença entre gols marcados e gols sofridos;
        aproveitamento (float): Porcentagem de aproveitamento da equipe no campeonato. Por padrão, é iniciado em 100.0;
        desempenho (list[str]): Histórico dos resultados da equipe (ex: ['V', 'D', 'E', 'V', 'V']).
    '''
    nome: str
    pontos: int
    jogos: int
    vitorias: int
    empates: int
    derrotas: int
    gols_marcados: int
    gols_sofridos: int
    saldo_gols: int
    aproveitamento: float
    desempenho: list[str] 


@dataclass
class Jogo:
    '''
    Representa uma partida entre duas equipes em uma rodada do campeonato.
    Cada jogo possui um mandante e um visitante, podendo ou não ter um placar definido.
    '''
    mandante: Equipe
    gols_mandante: int | None
    visitante: Equipe
    gols_visitante: int | None


@dataclass
class Rodada:
    '''
    Representa uma rodada do campeonato, contendo um conjunto de jogos e 
    seu número de identificação.
    '''
    lista_jogos: list[Jogo]
    numero: int
    

def procura_nome (lista: list[str], nome: str) -> bool:
    '''
    Verifica se *nome* está em *lista*. Devolve True, caso esteja
    e False, caso contrário.
    
    Exemplos:
    >>> procura_nome ([], 'equipe')
    False
    >>> procura_nome (['time', 'gol'], 'equipe')
    False
    >>> procura_nome (['time', 'equipe'], 'equipe')
    True
    '''
    esta = False
    i = 0
    while i < len(lista) and not esta:
        if nome == lista[i]:
            esta = True
        i += 1
    return esta


def registra_equipe(lista: list[str]):
    '''
    Registra uma nova equipe em *lista*.

    O usuário informa o nome da equipe a ser adicionada. A função verifica se a equipe já foi 
    registrada ou se o limite máximo de 20 equipes foi atingido. Se a equipe já estiver presente, 
    a adição não é realizada. Caso o limite tenha sido atingido, uma exceção é levantada.
    '''
    try:
        if len(lista) == 20:
            raise ValueError('As 20 Equipes foram registradas!')
        nome: str = input('\nNome da Equipe: ')
        nova = True
        for equipe in lista:
            if nome == equipe:
                nova = False
                print ('\nEquipe já registrada!')
        if nova:
            lista.append(nome)
    except ValueError as e:
        print(f'\nErro: {e}')


def exibe_equipes(lista: list[str]):
    '''
    Exibe *lista* que representa as equipes registradas no campeonato, numeradas em ordem.
    '''
    print()
    n = 1
    for equipe in lista:
        print(f'{n:2}º: {equipe}')
        n += 1

            
def altera_equipe(lista: list[str]):
    '''
    Altera o nome de uma equipe registrada no campeonato em *lista*.

    O usuário informa o nome atual da equipe e o novo nome desejado. Caso o novo nome já
    esteja registrado, a alteração não é realizada. Se o nome atual não for encontrado na lista, 
    nenhuma alteração é feita.
    '''
    nome = input('\nNome atual da Equipe: ')
    novo_nome = input('Novo nome da Equipe: ')
    encontrado = False
    
    if procura_nome(lista, novo_nome):
        print('\nNome já registrado!')
    else:
        i = 0
        while i < len(lista) and not encontrado:
            if lista[i] == nome:
                lista[i] = novo_nome
                encontrado = True
            i += 1
        if not encontrado:
            print ('\nNome não encontrado!')
    
    
def converte_equipe(lista: list[str]) -> list[Equipe]:
    '''
    Converte *lista* em uma lista de objetos da classe Equipe.
    
    Exemplos:
    >>> time = ['Corinthians']
    >>> converte_equipe(time)
    [Equipe(nome='Corinthians', pontos=0, jogos=0, vitorias=0, empates=0, derrotas=0, gols_marcados=0, gols_sofridos=0, saldo_gols=0, aproveitamento=100.0, desempenho=['Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada', 'Nada'])]
    '''
    equipes: list[Equipe] = []
    for nome in lista:
        equipe = Equipe(nome, 0, 0, 0, 0, 0, 0, 0, 0, 100.0, ['Nada'] * 38)
        equipes.append(equipe)
    
    return equipes


def gera_rodadas(lista: list[Equipe]) -> list[list[Jogo]]:
    '''
    Gera as rodadas de um campeonato para uma *lista* de classes Equipe.
    
    O sistema utiliza um método de emparelhamento circular para garantir que todas as equipes joguem entre si, 
    com revezamento dos mandos de campo, nos dois turnos.
    
    Exemplos:
    >>> equipes = ['Corinthians', 'Palmeiras', 'Santos', 'São Paulo']
    >>> rodadas = gera_rodadas(converte_equipe(equipes))
    >>> len(rodadas) # Teremos 3 rodadas no primeiro turno e 3 no segundo.
    6
    >>> len(rodadas[0]) == len(rodadas[1]) == 2 # Cada rodada tem 2 jogos (4 equipes).
    True
    >>> rodadas[0][0].mandante.nome
    'Corinthians'
    >>> rodadas[0][0].visitante.nome
    'São Paulo'
    >>> rodadas[0][0].gols_mandante is None and rodadas[0][0].gols_visitante is None
    True
    >>> rodadas[1][0].mandante.nome
    'Santos'
    >>> rodadas[1][0].visitante.nome
    'Corinthians'
    '''
    total_rodadas = len(lista) - 1
    rodadas_primeiro_turno = []; rodadas_segundo_turno = []
    
    for i in range(total_rodadas):
        rodada_primeiro_turno = []; rodada_segundo_turno = []
        for j in range(len(lista) // 2):
            timeA = lista[j]
            timeB = lista[len(lista) - 1 - j]
            if i % 2 == 0:
                rodada_primeiro_turno.append(Jogo(timeA, None, timeB, None))
                rodada_segundo_turno.append(Jogo(timeB, None, timeA, None))
            else:
                rodada_primeiro_turno.append(Jogo(timeB, None, timeA, None))
                rodada_segundo_turno.append(Jogo(timeA, None, timeB, None))
        
        rodadas_primeiro_turno.append(rodada_primeiro_turno)
        rodadas_segundo_turno.append(rodada_segundo_turno)

        lista.insert(1, lista.pop())
        
    return rodadas_primeiro_turno + rodadas_segundo_turno        


def escolhe_rodada(tabela: list[list[Jogo]]) -> Rodada:
    '''
    Solicita ao usuário a escolha de uma rodada de *tabela*, onde estão todas as rodadas.
    
    Se o número inserido estiver fora do intervalo válido, um erro é levantado,
    e o usuário é solicitado a inserir um número válido até que uma entrada correta seja fornecida.
    
    Devolve um objeto da classe Rodada, correspondente à rodada escolhida.
    '''
    while True:
        try:
            numero = int(input('\nEscolha a rodada a ser visualizada: '))
            if numero < 1 or numero > len(tabela):
                raise ValueError 
            return Rodada(tabela[numero - 1], numero)
        except ValueError:
            print('\nErro: Rodada não válida! Por favor, digite um número entre 1 e 38!')


def exibe_rodada(rodada: list[Jogo]):
    '''
    Exibe os jogos de *rodada*, listando cada jogo com seu respectivo 
    número de identificação, times participantes e placar.
    '''
    print()
    n = 1
    for jogo in rodada:
        exibe_jogo(n, jogo)    
        n += 1


def escolhe_jogo(rodada: Rodada) -> Jogo:
    '''
    Solicita ao usuário a escolha de uma jogo em *rodada*, onde estão todos os jogos de uma rodada.
    
    Se o número inserido estiver fora do intervalo válido, um erro é levantado,
    e o usuário é solicitado a inserir um número válido até que uma entrada correta seja fornecida.
    
    Devolve um objeto da classe Jogo, correspondente ao jogo escolhido.
    '''
    while True:
        try:
            numero_jogo = int(input('\nEscolha o número do jogo: '))
            if numero_jogo < 1 or numero_jogo > 10:
                raise ValueError
            return rodada.lista_jogos[numero_jogo - 1]  # Retorna um Jogo válido
        except ValueError:
            print('\nErro: Digite um jogo válido!')
            
            
def exibe_jogo(n: int, jogo: Jogo):
    '''
    Exibe *jogo* de número *n*, mostrando o nome dos times mandante e visitante, e o placar correspondente, caso ele exista.
    Se nenhum placar foi registrado, ele é representado por '-'.
    '''
    if jogo.gols_mandante is None:
        gols_mandante: str | int = '-'
    else:
        gols_mandante = jogo.gols_mandante
    if jogo.gols_visitante is None:
        gols_visitante: str | int = '-'
    else:
        gols_visitante = jogo.gols_visitante
    print (f'{n:2}º {jogo.mandante.nome:<20} {gols_mandante:^3} X {gols_visitante:^3} {jogo.visitante.nome:>20}')


def resultado(jogo: Jogo, rodada: int):
    '''
    Registra o resultado de *jogo* ocorrido na *rodada*º, a partir de informações inseridas pelo usuário.
    Não altera jogos já registrados.
    '''
    try:
        if jogo.gols_mandante is not None or jogo.gols_visitante is not None:
           raise ValueError("Resultado já registrado!")
        else:
            print(f'\nDigite o Placar de {jogo.mandante.nome} X {jogo.visitante.nome}\n')
            gols_A = int(input(f'{jogo.mandante.nome}: '))
            gols_B = int(input(f'{jogo.visitante.nome}: '))
            jogo.gols_mandante = gols_A
            jogo.gols_visitante = gols_B
            jogo.mandante.jogos += 1
            jogo.visitante.jogos += 1
            jogo.mandante.gols_marcados += gols_A
            jogo.mandante.gols_sofridos += gols_B
            jogo.visitante.gols_marcados += gols_B
            jogo.visitante.gols_sofridos += gols_A
            jogo.mandante.saldo_gols = jogo.mandante.gols_marcados - jogo.mandante.gols_sofridos
            jogo.visitante.saldo_gols = jogo.visitante.gols_marcados - jogo.visitante.gols_sofridos
    
            if gols_A == gols_B: #Empate
                empate(jogo.mandante, jogo.visitante, rodada)
            elif gols_A > gols_B: # Vitória do Time A
                vitoria(jogo.mandante, jogo.visitante, rodada)
            else: # Derrota do Time A
                vitoria(jogo.visitante, jogo.mandante, rodada)
        
            jogo.mandante.aproveitamento = (jogo.mandante.pontos / (jogo.mandante.jogos * 3)) * 100
            jogo.visitante.aproveitamento = (jogo.visitante.pontos / (jogo.visitante.jogos * 3)) * 100
        
    except ValueError as e:
        if "invalid literal" in str(e):
            print("\nErro: Resultado inválido! Digite valores válidos!")  # Caso de entrada não numérica
        else:
            print(f'\nErro: {e}') 


def vitoria(timeA: Equipe, timeB: Equipe, rodada: int):
    '''
    Registra a vitória de *timeA* sobre *timeB* na *rodada* especificada.
    
    Atualiza os pontos, vitórias e derrotas de cada time, além de registrar o desempenho em *rodada*. 
    
    Exemplos:
    >>> times = ['Corinthians', 'Flamengo']
    >>> equipes = converte_equipe(times)
    >>> timeA = equipes[0]
    >>> timeB = equipes[1]
    >>> vitoria(timeA, timeB, 1)
    >>> timeA.pontos
    3
    >>> timeA.vitorias
    1
    >>> timeB.derrotas
    1
    >>> timeA.desempenho[0]
    'Vitória'
    >>> timeB.desempenho[0]
    'Derrota'
    '''
    timeA.pontos += 3
    timeA.vitorias += 1
    timeB.derrotas += 1
    timeA.desempenho[rodada - 1] = 'Vitória'
    timeB.desempenho[rodada - 1] = 'Derrota'
        
        
def empate(timeA: Equipe, timeB: Equipe, rodada: int):
    '''
    Registra o empate entre *timeA* e *timeB* na *rodada* especificada.
    
    Atualiza os pontos e empates de cada time, além de registrar o desempenho em *rodada*.
    
    Exemplos:
    >>> times = ['Corinthians', 'Flamengo']
    >>> equipes = converte_equipe(times)
    >>> timeA = equipes[0]
    >>> timeB = equipes[1]
    >>> empate(timeA, timeB, 1)
    >>> timeA.pontos
    1
    >>> timeB.pontos
    1
    >>> timeA.empates
    1
    >>> timeB.empates
    1
    >>> timeA.desempenho[0]
    'Empate'
    >>> timeB.desempenho[0]
    'Empate'
    '''
    timeA.pontos += 1
    timeB.pontos += 1
    timeA.empates += 1 
    timeB.empates += 1
    timeA.desempenho[rodada - 1] = 'Empate'
    timeB.desempenho[rodada - 1] = 'Empate'
    
    
def jogos_equipe(nomes_equipes: list[str], rodadas: list[list[Jogo]]) -> str:
    '''
    Exibe todos os jogos e dados da equipe especificada pelo usuário, a partir da escolha de um time
    presente em *nomes_equipes* e de *rodadas* que representa todos os jogos do campeonato.
    
    Se o nome inserido estiver fora dos registrados, um erro é levantado,
    e o usuário é solicitado a inserir um nome válido até que uma entrada correta seja fornecida. 
    
    O nome especificado pelo usuário é devolvido, no caso de ser válido.
    '''
    while True:
        try:
            time = input('\nNome do Time: ')
            if not procura_nome(nomes_equipes, time):
                raise ValueError("Esse time não está presente no campeonato! Por favor, digite um time válido!")
            else:
                n = 1
                print(f'\n Jogos e Dados da Equipe "{time}":\n')
                for i in range(len(rodadas)):
                    encontrado = False
                    j = 0
                    while j < len(rodadas[i]) and not encontrado:
                        if rodadas[i][j].mandante.nome == time or rodadas[i][j].visitante.nome == time:
                            exibe_jogo(n, rodadas[i][j])
                            encontrado = True
                            n += 1
                        else:
                            j += 1
            return time
        except ValueError as e:
            print(f'\nErro: {e}')         


def dados_equipe(time: str, lista_times: list[Equipe]):
    '''
    Exibe os dados de *time*, que está presente em *lista_times*
    '''
    i = 0
    encontrado = False
    while i < len(lista_times) and not encontrado:
        if lista_times[i].nome == time:
            equipe_desejada = lista_times[i]
            encontrado = True
        else:
            i += 1
    print('\n  Dados da Equipe escolhida:\n')
    print('Pontos: ', equipe_desejada.pontos)
    print('Jogos: ', equipe_desejada.jogos)
    print('Vitórias: ', equipe_desejada.vitorias)
    print('Empates: ', equipe_desejada.empates)
    print('Derrotas: ', equipe_desejada.derrotas)
    print('Gols Marcados: ', equipe_desejada.gols_marcados)
    print('Gols Sofridos: ', equipe_desejada.gols_sofridos)
    print('Saldo de Gols: ', equipe_desejada.saldo_gols)    
    print(f'Aproveitamento: {equipe_desejada.aproveitamento:.1f}%')
  
  
def altera_resultado(jogo: Jogo, rodada: int):
    '''
    Altera o resultado de um *jogo* da *rodada*º ou o apaga, conforme a escolha do usuário. 
    
    Se nenhum resultado foi registrado em *jogo*, não realiza nenhuma alteração.
    '''
    try:
        if jogo.gols_mandante is None or jogo.gols_visitante is None:
            raise ValueError("Nenhum resultado registrado!")
        else:
            opcao = int(input("\nVocê deseja alterar o resultado ou apagá-lo? Digite 1 para ALTERAR ou 2 para APAGAR.\nEscolha uma opção: "))
            if opcao != 1 and opcao != 2:
                raise ValueError('Opção inválida!')
            else:
                jogo.mandante.jogos -= 1; jogo.visitante.jogos -= 1
                jogo.mandante.gols_marcados -= jogo.gols_mandante
                jogo.mandante.gols_sofridos -= jogo.gols_visitante
                jogo.visitante.gols_marcados -= jogo.gols_visitante
                jogo.visitante.gols_sofridos -= jogo.gols_mandante
                jogo.mandante.saldo_gols = jogo.mandante.gols_marcados - jogo.mandante.gols_sofridos
                jogo.visitante.saldo_gols = jogo.visitante.gols_marcados - jogo.visitante.gols_sofridos
                jogo.mandante.desempenho[rodada - 1] = 'Nada'
                jogo.visitante.desempenho[rodada - 1] = 'Nada'
                
                if jogo.gols_mandante == jogo.gols_visitante: # Empate
                    jogo.mandante.pontos -= 1
                    jogo.visitante.pontos -= 1
                    jogo.mandante.empates -= 1
                    jogo.visitante.empates -= 1
                elif jogo.gols_mandante > jogo.gols_visitante: # Vitória do Time A
                    jogo.mandante.pontos -= 3
                    jogo.mandante.vitorias -= 1
                    jogo.visitante.derrotas -= 1
                else: # Derrota do Time A
                    jogo.visitante.pontos -= 3
                    jogo.visitante.vitorias -= 1
                    jogo.mandante.derrotas -= 1
                    
                if jogo.mandante.jogos == 0:
                    jogo.mandante.aproveitamento = 100.0
                else:
                    jogo.mandante.aproveitamento = (jogo.mandante.pontos / (jogo.mandante.jogos * 3)) * 100
                if jogo.visitante.jogos == 0:
                    jogo.visitante.aproveitamento = 100.0
                else:
                    jogo.visitante.aproveitamento = (jogo.visitante.pontos / (jogo.visitante.jogos * 3)) * 100
                jogo.gols_mandante = None
                jogo.gols_visitante = None
                if opcao == 1:
                    resultado(jogo, rodada)
                    
    except ValueError as e:
        if "invalid literal" in str(e):
            print("\nErro: Opção inválida! Digite um número válido!")  # Caso de entrada não numérica
        else:
            print(f'\nErro: {e}') 

   
def exibe_tabela(equipes: list[Equipe]):
    '''
    Exibe a tabela ordenada do campeonato, a partir de *equipes*.
    '''
    print()
    print (f'{'CLASSIFICAÇÃO':^24} {'P':^5} {'J':^5} {'V':^5} {'E':^5} {'D':^5} {'GM':^5} {'GS':^5} {'SG':^5} {'%':^7} {'                            DESEMPENHO'}')
    n = 1
    ordena_intercalacao(equipes)
    for equipe in equipes:
        print (f'{n:2}º {equipe.nome:<20} {equipe.pontos:^5} {equipe.jogos:^5} {equipe.vitorias:^5} {equipe.empates:^5} {equipe.derrotas:^5} {equipe.gols_marcados:^5} {equipe.gols_sofridos:^5} {equipe.saldo_gols:^5} {(f'{equipe.aproveitamento:.1f}%'):^7} {' '.join(converter_para_letras(equipe.desempenho))}') 
        n += 1


def converter_para_letras(desempenho: list[str]) -> list[str]:
    '''
    Converte os status de *desempenho* dos times em letras representativas.

    A função recebe uma lista de strings, em que cada uma é convertida para uma letra 
    correspondente: 'Vitória' para 'V', 'Empate' para 'E', 'Derrota' para 'D' e 'Nada' para '-'.

    Exemplos:
    >>> converter_para_letras([])
    []
    >>> converter_para_letras(['Vitória', 'Empate', 'Derrota', 'Nada'])
    ['V', 'E', 'D', '-']
    '''
    resultado: list[str] = []
    for status in desempenho:
        if status == 'Vitória':
            resultado.append('V')
        elif status == 'Empate':
            resultado.append('E')
        elif status == 'Derrota':
            resultado.append('D')
        elif status == 'Nada':
            resultado.append('-')
    return resultado


def ordena_intercalacao(lst: list[Equipe]):
    '''
    Ordena *lst*, uma lista de equipes utilizando o algoritmo Merge Sort (ordenação por intercalação).
    
    O algoritmo divide recursivamente a lista ao meio e depois intercala as sublistas ordenadas.
    Complexidade: O(n lg n), onde n é o número de elementos na lista.
    '''
    if len(lst) > 1:
        m = len(lst) // 2
        a = lst[:m]
        b = lst[m:]
        ordena_intercalacao(a)
        ordena_intercalacao(b)
        intercala(lst, a, b)


def intercala(lst: list[Equipe], a: list[Equipe], b: list[Equipe]):
    '''
    Faz a intercalação em ordem dos elementos
    de *a* e *b* e armazena o resultado em *lst*.

    Requer que len(lst) = len(a) + len(b).

    Os critérios de ordenação são os seguintes:
    1. **Pontos**: As equipes são ordenadas primeiro pelo número de pontos.
    2. **Vitórias**: Em caso de empate em pontos, a ordenação é feita pelo número de vitórias.
    3. **Saldo de Gols**: Se ainda houver empate, o saldo de gols é considerado.
    4. **Nome da Equipe**: Como último critério, as equipes são ordenadas pelo nome em ordem alfabética.
    '''
    assert len(lst) == len(a) + len(b)
    
    i = 0; j = 0; k = 0
    while i < len(a) and j < len(b):
        if a[i].pontos > b[j].pontos:
            lst[k] = a[i]
            i += 1
        elif a[i].pontos < b[j].pontos:
            lst[k] = b[j]
            j += 1
        else:
            if a[i].vitorias > b[j].vitorias:
                lst[k] = a[i]
                i += 1
            elif a[i].vitorias < b[j].vitorias:
                lst[k] = b[j]
                j += 1
            else:
                if a[i].saldo_gols > b[j].saldo_gols:
                    lst[k] = a[i]
                    i += 1
                elif a[i].saldo_gols < b[j].saldo_gols:
                    lst[k] = b[j]
                    j += 1
                else:
                    if a[i].nome <= b[j].nome:
                        lst[k] = a[i]
                        i += 1
                    elif a[i].nome > b[j].nome:
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


def exibe_regras():
    '''
    Exibe as regras do campeonato, incluindo seu formato, os critérios de desempate
    e as consequências relacionadas à cada colocação.
    '''
    print('\n========== REGRAS DO CAMPEONATO ==========\n')
    print('FORMATO:')
    print('- 20 equipes disputam o campeonato.')
    print('- 38 rodadas (ida e volta).')
    print('- Sistema de pontos corridos: cada vitória vale 3 pontos, empates valem 1 ponto e derrotas valem 0 pontos.\n')

    print('CRITÉRIOS DE DESEMPATE:')
    print('1. Pontos')
    print('2. Número de vitórias')
    print('3. Saldo de gols')
    print('4. Ordem alfabética\n')

    print('CLASSIFICAÇÃO FINAL:')
    print('- 1º lugar: CAMPEÃO')
    print('- 2º a 4º lugar: Classificados para a fase de grupos da Libertadores')
    print('- 5º e 6º lugar: Classificados para a fase preliminar da Libertadores')
    print('- 7º a 12º lugar: Classificados para a Copa Sul-Americana\n')

    print('REBAIXAMENTO:')
    print('- Os últimos 4 colocados (17º ao 20º lugar) são rebaixados para a segunda divisão.\n')
    
    print('==========================================')
       
       
def menu_principal():
    '''
    Exibe o menu principal do programa com todas as operações disponíveis.
    '''
    sair = False
    equipes = []
    while not sair:
        print("\nSeja Bem-Vindo ao Simulador de Campeonato Brasileiro:\n")
        print("1) Registrar uma Equipe")
        print("2) Visualizar Equipes")
        print("3) Alterar uma Equipe")
        print("4) Iniciar Simulação do Campeonato")
        print("5) Exibir Regras do Campeonato")
        print("6) Sair\n")
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao < 1 or opcao > 6:
                raise ValueError('Opção inválida!')
            elif opcao == 1:
                registra_equipe(equipes)
            elif opcao == 2: 
                exibe_equipes(equipes)
            elif opcao == 3:
                altera_equipe(equipes)
            elif opcao == 4:
                if len(equipes) != 20:
                    raise ValueError("São necessárias 20 equipes para o campeonato começar!")
                else:
                    sair_2 = False
                    times = converte_equipe(equipes)
                    rodadas = gera_rodadas(times)
                    while not sair_2:
                        print("\n1) Exibir uma Rodada")
                        print("2) Inserir Resultado")
                        print("3) Alterar Resultado")
                        print("4) Ver Desempenho de Equipe")
                        print("5) Visualizar Tabela do Campeonato")
                        print("6) Exibir Regras do Campeonato")
                        print("7) Sair e Finalizar Campeonato\n")
                        try:
                            opcao2 = int(input("Escolha uma opção: "))
                            if opcao2 < 1 or opcao2 > 7:
                                raise ValueError
                            elif opcao2 == 1:
                                exibe_rodada(escolhe_rodada(rodadas).lista_jogos)
                            elif opcao2 == 2: 
                                rodada = escolhe_rodada(rodadas)
                                exibe_rodada(rodada.lista_jogos)
                                resultado(escolhe_jogo(rodada), rodada.numero)
                            elif opcao2 == 3:
                                rodada = escolhe_rodada(rodadas)
                                exibe_rodada(rodada.lista_jogos)
                                altera_resultado(escolhe_jogo(rodada), rodada.numero)
                            elif opcao2 == 4:
                                dados_equipe(jogos_equipe(equipes, rodadas), times)
                            elif opcao2 == 5:
                                exibe_tabela(times)
                            elif opcao2 == 6:
                                exibe_regras()
                            elif opcao2 == 7:
                                sair_2 = True
                                exibe_tabela(times)
                                print('\nCampeonato Finalizado!')
                        except ValueError:
                            print("\nErro: Opção inválida! Digite um número válido!")  # Caso de entrada não numérica
            elif opcao == 5:
                exibe_regras()
            elif opcao == 6:
                sair = True
                print ('\nFim da Sessão!')
                print()
        except ValueError as e:
            if "invalid literal" in str(e):
                print("\nErro: Opção inválida! Digite um número válido!")  # Caso de entrada não numérica
            else:
                print(f'\nErro: {e}')  


def main():
    menu_principal()
    
    
main()
