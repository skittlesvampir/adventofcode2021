from sys import stdin
schließend = [")", "]", "}", ">"]
umgekehrt = {}
umgekehrt[">"] = "<"
umgekehrt["}"] = "{"
umgekehrt[")"] = "("
umgekehrt["]"] = "["
fehler = []
for line in stdin:
    zeichen = list(line)
#print(zeichen)
    klammern = []
    for z in zeichen:
        if z in schließend:
            if umgekehrt[z] == klammern[-1]:
                klammern.pop()
            else:
                fehler.append(z)
                break
        else:
            klammern.append(z)
punkte = {}
punkte[")"] = 3
punkte["]"] = 57
punkte["}"] = 1197
punkte[">"] = 25137
summe = 0
for f in fehler:
	summe += punkte[f]

print(summe)
