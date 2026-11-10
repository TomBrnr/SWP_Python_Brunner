import random
import sys
from collections import Counter

from konstanten import SYMBOLE, DECK, GESAMT, THEORIE

Karte = tuple[int, str]


# Karte als Text, z. B. (14, "♠") -> "A♠"
def karte_als_text(karte: Karte) -> str:
    rang, farbe = karte
    return SYMBOLE.get(rang, str(rang)) + farbe


# Ränge der Hand aufsteigend sortiert
def sortierte_raenge(hand: list[Karte]) -> list[int]:
    raenge: list[int] = []
    for rang, _ in hand:
        raenge.append(rang)
    return sorted(raenge)

# Wie oft jeder Rang vorkommt, z. B. [3, 2] bei einem Full House
def haeufigkeiten_der_raenge(hand: list[Karte]) -> list[int]:
    return sorted(Counter(sortierte_raenge(hand)).values(), reverse=True)


# Alle Karten haben dieselbe Farbe
def ist_flush(hand: list[Karte]) -> bool:
    return len({farbe for _, farbe in hand}) == 1


# Fünf Ränge hintereinander, auch A-2-3-4-5 (Ass zählt dann als 1)
def ist_strasse(hand: list[Karte]) -> bool:
    raenge = sortierte_raenge(hand)
    return len(set(raenge)) == 5 and (raenge[4] - raenge[0] == 4 or raenge == [2, 3, 4, 5, 14])


# Straße in einer Farbe
def ist_straight_flush(hand: list[Karte]) -> bool:
    return ist_strasse(hand) and ist_flush(hand)


# Straight Flush von 10 bis Ass (Royal Flush)
def ist_royal_flush(hand: list[Karte]) -> bool:
    return ist_straight_flush(hand) and sortierte_raenge(hand)[0] == 10


# Vier gleiche Ränge
def ist_poker(hand: list[Karte]) -> bool:
    return haeufigkeiten_der_raenge(hand)[0] == 4


# Drilling und Paar
def ist_full_house(hand: list[Karte]) -> bool:
    return haeufigkeiten_der_raenge(hand) == [3, 2]


# Drei gleiche Ränge
def ist_drilling(hand: list[Karte]) -> bool:
    return haeufigkeiten_der_raenge(hand)[0] == 3


# Zwei verschiedene Paare
def ist_zwei_paare(hand: list[Karte]) -> bool:
    return haeufigkeiten_der_raenge(hand) == [2, 2, 1]


# Zwei gleiche Ränge
def ist_paar(hand: list[Karte]) -> bool:
    return haeufigkeiten_der_raenge(hand)[0] == 2


# Gibt die beste Kombination der Hand zurück
def bestimme_kombination(hand: list[Karte]) -> str:
    # Reihenfolge ist wichtig: von der besten zur schlechtesten Kombination
    if ist_royal_flush(hand):
        return "Royal Flush"
    if ist_straight_flush(hand):
        return "Straight Flush"
    if ist_poker(hand):
        return "Poker"
    if ist_full_house(hand):
        return "Full House"
    if ist_flush(hand):
        return "Flush"
    if ist_strasse(hand):
        return "Straße"
    if ist_drilling(hand):
        return "Drilling"
    if ist_zwei_paare(hand):
        return "Zwei Paare"
    if ist_paar(hand):
        return "Paar"
    return "Höchste Karte"


# Anzahl der Spiele aus der Kommandozeile, sonst 100 000
spiele: int = int(sys.argv[1]) if len(sys.argv) > 1 else 100_000

# Beispielhand: 5 zufällige Karten ziehen und anzeigen
hand: list[Karte] = random.sample(DECK, 5)
karten: str = ""
for k in hand:
    karten = karten + karte_als_text(k) + " "
print("Beispielhand:", karten)
print("Kombination:", bestimme_kombination(hand))
print()

# Simulation: viele Hände ziehen und Kombinationen zählen
zaehler: Counter[str] = Counter()
for _ in range(spiele):
    neue_hand: list[Karte] = random.sample(DECK, 5)
    kombination: str = bestimme_kombination(neue_hand)
    zaehler[kombination] += 1

# Ausgabe: Simulation und Theorie in Prozent vergleichen
print(f"Ergebnis nach {spiele} Spielen")
print(f"{'Kombination':<15}{'Simuliert':>10}{'Theorie':>10}")
for name, moeglich in THEORIE.items():
    simuliert = zaehler[name] / spiele * 100
    theorie = moeglich / GESAMT * 100
    print(f"{name:<15}{simuliert:>9.3f}%{theorie:>9.3f}%")