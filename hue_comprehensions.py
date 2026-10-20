# 1) List Comprehension mit if/else
#    Zahlen 1 bis 10: gerade Zahlen --> quadriert, ungerade Zahlen --> Wort "ungerade"
zahlen = range(1, 11)
liste = [x ** 2 if x % 2 == 0 else "ungerade" for x in zahlen]
print("List:", liste)

# 2) Set Comprehension mit if/else
#    aus Liste von Noten wird ein Set mit "positiv"/"negativ"
#    set --> jedes Ergebnis bleibt nur einmal übrig
noten = [1, 3, 5, 2, 4, 5, 1]
ergebnis = {"positiv" if n <= 4 else "negativ" for n in noten}
print("Set:", ergebnis)

# 3) Dict Comprehension mit if/else
#    Zu jedem Namen wird gespeichert, ob er kurz oder lang ist
namen = ["Tom", "Vinzent", "Eva", "Fabian", "Elias"]
laengen = {name: "kurz" if len(name) <= 4 else "lang" for name in namen}
print("Dict:", laengen)

