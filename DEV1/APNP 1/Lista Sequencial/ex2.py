#Questão 39. Elabore um algoritmo que lê um número e imprime a raiz quadrada do número.
import math

def raizquadrada(inteiro: int ):

    resultado = math.sqrt(inteiro)

    return resultado

print(raizquadrada(int(input("Insira um numero inteiro:"))))
