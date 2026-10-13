import random



def lottoziehung(anzahl=6, max_zahl=45):
    
    zahlen = list(range(1, max_zahl + 1))
    for i in range(anzahl):
        letzte = max_zahl - 1 - i              # letzter noch "freier" Index
        idx = random.randint(0, letzte)        # 1 Zufallszahl pro Ziehung
        # gezogene Zahl ans Ende tauschen -> kann nicht mehr gezogen werden
        zahlen[idx], zahlen[letzte] = zahlen[letzte], zahlen[idx]
    return zahlen                              # gezogene Zahlen = letzte 'anzahl' Einträge


def statistik(ziehung, stat, anzahl=6):
       for pos in range(len(ziehung) - anzahl, len(ziehung)):
        stat[ziehung[pos]] += 1


def lotto_statistik(anzahl_ziehungen, max_zahl=45):
    stat = {zahl: 0 for zahl in range(1, max_zahl + 1)}
    for _ in range(anzahl_ziehungen):
        ziehung = lottoziehung()
        statistik(ziehung, stat)               # nach jeder Ziehung aufrufen
    return stat


if __name__ == "__main__":
    print("Lottoziehung:", lottoziehung()[-6:])

    for n in (1000, 10000, 100000):
        stat = lotto_statistik(n)
        print(f"\nStatistik nach {n} Ziehungen:")
        for zahl, haeufigkeit in stat.items():
            prozent = haeufigkeit / n * 100
            print(f"Zahl {zahl:2}: {haeufigkeit:6}x  ({prozent:5.2f} %)")
