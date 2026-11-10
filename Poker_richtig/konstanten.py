# Ränge 2..14 (Bube = 11, Dame = 12, König = 13, Ass = 14)
SYMBOLE: dict[int, str] = {11: "B", 12: "D", 13: "K", 14: "A"}
FARBEN: list[str] = ["♥", "♦", "♣", "♠"]

# Deck: jede Karte ist ein Tupel (Rang, Farbe)
DECK: list[tuple[int, str]] = [(rang, farbe) for farbe in FARBEN for rang in range(2, 15)]

# Exakte Anzahl je Kombination (von 2.598.960 möglichen Händen)
GESAMT: int = 2_598_960
THEORIE: dict[str, int] = {
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
