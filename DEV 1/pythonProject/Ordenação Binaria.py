import random
agenda = []

for i in range(100):
    #item +=1
    item = random.randint(1,1000)
    agenda.append(item)

print(agenda)
agendaord = sorted(agenda)
print(agendaord)
