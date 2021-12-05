# Eingabe ist eine Liste mit Zahlen, es soll augegebenwerden, wie viele Zahlen
# größer als ihre Vorgänger sind
incr = 0
letzte = int(input())
while True:
    eingabe = input()
    if eingabe != '' and eingabe.isdigit():
        zahl = int(eingabe)
        if zahl > letzte:
            incr += 1
        letzte = zahl
    else:
        break
print(incr)