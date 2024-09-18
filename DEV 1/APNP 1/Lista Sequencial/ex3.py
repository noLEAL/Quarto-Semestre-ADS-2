#Questão 49. Lê um valor de hora e informa quantos minutos se passaram desde início do dia.

import time


def horariouser(textohora: str):
    """ Converte uma string que recebe do usuario com um horario e retorna quantidades de minutos desdeque comeöou o dia """
    print(" texto recebido na funcao", textohora)

    horario = textohora[:2]
    minuto = textohora[-2:]

    horarioint = int(horario)
    minutoint = int(minuto)

    resultado = horarioint * 60
    resultado = resultado + minutoint

    return resultado

print("Informe o horario desejado: [HORAS:MINUTOS]")
print(horariouser(str(input("Quantidade de minutos: "))))
