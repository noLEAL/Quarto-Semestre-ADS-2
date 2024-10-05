#!/usr/bind/env python

flag = True

while flag:
    try:
        print("Digite algo:")
        a = int(input())

        if a == 100:
            raise TypeError("Customizado")
        elif a == 200:
            raise NameError("Customizado")
        else:
            b = a * 2
            print(f"O dobro de {a} é {b}.")
    except ValueError:
        flag = False
        print("Você não deve digitar letras")
    except TypeError:
        print("Erro 100: Não sei fazer esse calculo para 100")
    except:
        print("Erro!")
else:
    print("Finalizado")
