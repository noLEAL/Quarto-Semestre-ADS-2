#Questão 55. Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% para o garçom.
# Faça um programa que leia o valor gasto com as despesas realizadas em um restaurante e mostre o valor total com a gorjeta.


def valortotal(total: float):

    resutado = (total * 10)/100

    return resutado


print(valortotal(float(input("Digite Valor total da compra "))))

