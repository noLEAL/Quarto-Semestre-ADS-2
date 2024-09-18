#Questão 37. Elabore um algoritmo que lê o raio de um círculo e mostre como saída o perímetro e a área.

def calcparimetro(raio: float):
    """Função que define o perimetro do circulo a partir do raio fornecido pelo usuario """
    pi = 3.14159
    perimetro = (2*pi) * raio

    return perimetro

print(calcparimetro(float(input("Digite o raio do circulo em cm: "))))