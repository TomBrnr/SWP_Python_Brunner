import random


def lottoziehung():
    zahlen = list(range(1, 46))
    gezogen = []

    for i in range(6):
        index = random.randint(0, len(zahlen) - 1) 
        gezogen.append(zahlen.pop(index))          

    return gezogen


def statistik(ziehung, stat):
    for zahl in ziehung:
        stat[zahl] += 1  


def lotto_statistik(anzahl):
    stat = {}
    for zahl in range(1, 46):
        stat[zahl] = 0   

    for i in range(anzahl):
        ziehung = lottoziehung()
        statistik(ziehung, stat)   

    return stat


print("Lottoziehung:", lottoziehung())

for anzahl in [1000, 10000, 100000]:
    stat = lotto_statistik(anzahl)
    print(f"\nStatistik nach {anzahl} Ziehungen:")
    for zahl in stat:
        print(f"{zahl}: {stat[zahl]}")
