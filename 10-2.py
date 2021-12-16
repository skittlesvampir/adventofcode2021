from sys import stdin
schließend = [")", "]", "}", ">"]
umgekehrt = {}
umgekehrt[">"] = "<"
umgekehrt["}"] = "{"
umgekehrt[")"] = "("
umgekehrt["]"] = "["
geöffnete_klammern = []
for line in stdin:
    zeichen = list(line.strip())
    klammern = []
    fehlerhaft = False
    for z in zeichen:
        if z in schließend:
            if umgekehrt[z] == klammern[-1]:
                klammern.pop()
            else:
                fehlerhaft = True
                break
        else:
            klammern.append(z)
    if fehlerhaft == False:
        klammern.reverse()
        geöffnete_klammern.append(klammern)
punkte = {}
punkte["("] = 1
punkte["["] = 2
punkte["{"] = 3
punkte["<"] = 4
zeilen_punkte = []
for g in geöffnete_klammern:
    tmp = 0
    for e in g:
        tmp *= 5
        tmp += punkte[e]
    zeilen_punkte.append(tmp)

zeilen_punkte.sort()
print(zeilen_punkte[len(zeilen_punkte)//2])
