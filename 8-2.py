# "Inspiriert" von Jonathan Paulson (github.com/jonathanpaulson/AdventOfCode)
from sys import stdin

def zahl_entziffern(n):
    vertauschung = {} # Eigentlich -> verwirrt
    for w in vorn[n]: # 1
        if len(w) == 2:
            cf = w
            break
    for w in vorn[n]: # 7
        if len(w) == 3:
            for z in w:
                if z not in cf:
                    vertauschung[z] = "a"
                    break
            break
    for w in vorn[n]: # 6
        if len(w) == 6 and (cf[0] in w) != (cf[1] in w):
            if cf[0] in w:
                vertauschung[cf[0]] = "f"
                vertauschung[cf[1]] = "c"
            else:
                vertauschung[cf[1]] = "f"
                vertauschung[cf[0]] = "c"
    for w in vorn[n]: # 4
        if len(w) == 4:
            bd = []
            for z in w:
                if z not in cf:
                    bd.append(z)
    for w in vorn[n]: # 0
        if len(w) == 6 and (bd[0] in w) != (bd[1] in w):
            if bd[0] in w:
                vertauschung[bd[0]] = "b"
                vertauschung[bd[1]] = "d"
            else:
                vertauschung[bd[1]] = "b"
                vertauschung[bd[0]] = "d"
    eg = []
    for z in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if z not in vertauschung:
            eg.append(z)
    for w in vorn[n]: # 9
        if len(w) == 6 and (eg[0] in w) != (eg[1] in w):
            if eg[0] in w:
                vertauschung[eg[0]] = "g"
                vertauschung[eg[1]] = "e"
            else:
                vertauschung[eg[1]] = "g"
                vertauschung[eg[0]] = "e"
    return vertauschung

def zahl_herausfinden(n):
    zahl = []
    for w in hinten[n]:
        w = list(w)
        if len(w) == 4: # 4
            zahl.append(4)
        elif len(w) == 2: # 1
            zahl.append(1)
        elif len(w) == 3: # 7
            zahl.append(7)
        elif len(w) == 7: # 8
            zahl.append(8)
        elif len(w) == 5: # 2,3,5
            if ist(2,w,n) == True:
                zahl.append(2)
            elif ist(3,w,n) == True:
                zahl.append(3)
            else:
                zahl.append(5)
        elif len(w) == 6: # 0,6,9
            if ist(0,w,n) == True:
                zahl.append(0)
            elif ist(6,w,n) == True:
                zahl.append(6)
            else:
                zahl.append(9)
    return int(''.join([str(x) for x in zahl]))
            
def ist(n,w,liste):
    vertauschung = zahl_entziffern(liste)
    zahlen = {}
    zahlen[2] = ["a","c","d","e","g"]
    zahlen[3] = ["a","c","d","f","g"]
    zahlen[0] = ["a","b","c","e","f","g"]
    zahlen[6] = ["a","b","d","e","f","g"]
    for z in w:
        if vertauschung[z] not in zahlen[n]:
            return False
    return True

vorn = []
hinten = []
for eingabe in stdin:
    if eingabe != '':
        vorn.append([list(x) for x in eingabe.strip().split('|')[0].split(' ') if x != ''])
        hinten.append([list(x) for x in eingabe.strip().split('|')[1].split(' ') if x != ''])

summe = 0
for i in range(len(hinten)):
    summe += zahl_herausfinden(i)

print(summe)