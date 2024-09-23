from atleta import Atleta

comissao = []

atleta_rugby = Atleta("João", "2001-01-01", "Rugby",True)
atleta_ping = Atleta("Maria", "2010-01-01", "Ping Pong",True ,"João")
atleta_futebol = Atleta("José", "1980-01-01", "Futebol",True, "Pedro")
atleta_futebol2 = Atleta("Pedro", "1990-01-01", "Futebol", False)

comissao.append(atleta_rugby)
comissao.append(atleta_ping)
comissao.append(atleta_futebol)
comissao.append(atleta_futebol2)

print("Comissão:")
for atleta in comissao:
    print(atleta)

print("Futebol:")
for atleta in comissao:
    if atleta.esporte == "Futebol":
        print(atleta)