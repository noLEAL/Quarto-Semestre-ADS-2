from random import randint


def prencher(listvazia: list):
    """Recebe uma lista vazia e retorna uma lista cheia de inteiros aleatorios, não ordenados"""

    for i in range(100):
        item = randint(1,1000)
        listvazia.append(item)
    return listvazia

def organizar(listdesord: list):

    listord = sorted(listdesord)

    return listord

def tiraduvida(listd: list):
    control = True

    for i in range(len(listd)-1):
        if listd[i] > listd[i+1]:
            control = False

    return control

def pesquisabinaria(listord: list,objescolido: int):
    objresult = 0
    #if ord == False:

    return objresult

lopcontrol = True
while lopcontrol:

    print("Escolha um nome para sua lista:")
    agendauser = input(str('--->'))

    print("Nome escolido foi:", agendauser)
    agendauser = []

    prencher(agendauser)
    print("Sua Lista comtem:\n", agendauser)

    print("Deseja ordenar:\n [Y] Sim X [N] Não")
    tempescolha = input('--->')

    if tempescolha.lower() == 'y':
        agendauser = organizar(agendauser)
        print("Sua Lista comtem:\n", agendauser)

    print("O Qual numero deseja pesquisar:")
    objdefinido = int(input('--->'))

    test = tiraduvida(agendauser)
    print(test)


