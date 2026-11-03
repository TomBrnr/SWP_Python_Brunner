import random
import sys
from collections import Counter

# Ränge 2..14 (Bube = 11, Dame = 12, König = 13, Ass = 14)
SYMBOLE = {11: "B", 12: "D", 13: "K", 14: "A"}
FARBEN = ["♥", "♦", "♣", "♠"]

# Deck: jede Karte ist ein Tupel (Rang, Farbe)
DECK = [(rang, farbe) for farbe in FARBEN for rang in range(2, 15)]

# Exakte Anzahl je Kombination (von 2.598.960 möglichen Händen)
GESAMT = 2_598_960
THEORIE = {
    "Royal Flush": 4,
    "Straight Flush": 36,
    "Poker": 624,
    "Full House": 3_744,
    "Flush": 5_108,
    "Straße": 10_200,
    "Drilling": 54_912,
    "Zwei Paare": 123_552,
    "Paar": 1_098_240,
    "Höchste Karte": 1_302_540,
}


def karte_als_text(karte):
    rang, farbe = karte
    return SYMBOLE.get(rang, str(rang)) + farbe


def bewerte(hand):
    raenge = sorted(rang for rang, _ in hand)
    anzahl = sorted(Counter(raenge).values(), reverse=True)

    flush = len({farbe for _, farbe in hand}) == 1
    strasse = len(set(raenge)) == 5 and (raenge[4] - raenge[0] == 4 or raenge == [2, 3, 4, 5, 14])

    if strasse and flush:
        return "Royal Flush" if raenge[0] == 10 else "Straight Flush"
    if anzahl[0] == 4:
        return "Poker"
    if anzahl == [3, 2]:
        return "Full House"
    if flush:
        return "Flush"
    if strasse:
        return "Straße"
    if anzahl[0] == 3:
        return "Drilling"
    if anzahl == [2, 2, 1]:
        return "Zwei Paare"
    if anzahl[0] == 2:
        return "Paar"
    return "Höchste Karte"


spiele = int(sys.argv[1]) if len(sys.argv) > 1 else 100_000

# Beispielhand
hand = random.sample(DECK, 5)
karten = ""
for k in hand:
    karten = karten + karte_als_text(k) + " "
print("Beispielhand:", karten)
print("Kombination:", bewerte(hand))
print()

# Simulation
zaehler = Counter(bewerte(random.sample(DECK, 5)) for _ in range(spiele))

# Ausgabe
print(f"Ergebnis nach {spiele:,} Spielen".replace(",", "."))
print(f"{'Kombination':<15}{'Anzahl':>9}{'Simuliert':>12}{'Theorie':>12}{'Abweichung':>12}")
print("-" * 60)
for name, moeglich in THEORIE.items():
    simuliert = zaehler[name] / spiele * 100
    theorie = moeglich / GESAMT * 100
    print(f"{name:<15}{zaehler[name]:>9}{simuliert:>11.4f}%{theorie:>11.4f}%{simuliert - theorie:>+11.4f}%")