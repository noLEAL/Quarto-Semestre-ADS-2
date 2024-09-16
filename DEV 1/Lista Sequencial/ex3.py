#Questão 49. Lê um valor de hora e informa quantos minutos se passaram desde início do dia.

import time


def horariouser(textohora: str):
    """ Converte uma string que recebe do usuario com um horario e retorna quantidades de minutos desdeque comeöou o dia """
    print(" texto recebido na funcao", textohora)

    horario = textohora[:2]
    minuto = textohora[-2:]

    print("filtro para pegar apenas os dois primeiros e ultimos caracteres // ainda uma string", horario, minuto)

    horarioint = int(horario)
    minutoint = int(minuto)

    print(horarioint, minutoint)
    print(type(horarioint), type(minutoint))

    print("conversäao")

    minutos = horarioint * 60
    print(horario)
    print(type(horario))

    return

print("Informe o horario desejado: [HORAS:MINUTOS]")
horariouser(str(input()))
