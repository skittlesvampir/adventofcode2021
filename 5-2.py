from sys import stdin
def print_karte(karte):
    for i in range(len(karte)):
        liste = [str(x) for x in karte[i]]
        print(''.join(liste))
zeilen = []
max_x = 0
max_y = 0
for line in stdin:
    eingabe = line.strip() 
    eingabe = eingabe.split(" ")
    eins = [int(x) for x in eingabe[0].split(",")]
    zwei = [int(x) for x in eingabe[2].split(",")]
    #if eins[0] == zwei[0] or eins[1] == zwei[1]:
    zeilen.append([eins[0], eins[1], zwei[0], zwei[1]])
    if eins[0] > max_x:
        max_x = eins[0]
    if eins[1] > max_y:
        max_y = eins[1]
    if zwei[0] > max_x:
        max_x = zwei[0]
    if zwei[1] > max_y:
        max_y = zwei[1]


max_x += 1
max_y += 1
karte = [["."]*max_x for x in range(max_y)]
for zeile in zeilen:
    if zeile[0] == zeile[2]:
        if zeile[1] < zeile[3]:
            incrementer = 1
            zahl = zeile[3]+1
        else:
            incrementer = -1
            zahl = zeile[3]-1
        for i in range(zeile[1],zahl,incrementer):
            if karte[i][zeile[0]] == ".":
                karte[i][zeile[0]] = 1
            else:
                karte[i][zeile[0]] += 1
    elif zeile[1] == zeile[3]:
        if zeile[0] < zeile[2]:
            incrementer = 1
            zahl = zeile[2]+1
        else:
            incrementer = -1
            zahl = zeile[2]-1
        for i in range(zeile[0],zahl,incrementer):
            if karte[zeile[1]][i] == ".":
                karte[zeile[1]][i] = 1
            else:
                karte[zeile[1]][i] += 1
    else:
        pos_x = zeile[0]
        pos_y = zeile[1]
        if karte[pos_y][pos_x] == ".":
            karte[pos_y][pos_x] = 1
        else:
            karte[pos_y][pos_x] += 1
        if zeile[0] < zeile[2]:
            pos_x += 1
        else:
            pos_x -= 1
        if zeile[1] < zeile[3]:
            pos_y += 1
        else:
            pos_y -= 1
        while True:
            if karte[pos_y][pos_x] == ".":
                karte[pos_y][pos_x] = 1
            else:
                karte[pos_y][pos_x] += 1
            if zeile[0] < zeile[2]:
                pos_x += 1
            else:
                pos_x -= 1
            if zeile[1] < zeile[3]:
                pos_y += 1
            else:
                pos_y -= 1
            if zeile[0] < zeile[2]:
                if pos_x > zeile[2]:
                    break
            else:
                if pos_x < zeile[2]:
                    break

gefahren_punkte = 0
for i in range(max_y):
    for ii in range(max_x):
        if karte[i][ii] != ".":
            if karte[i][ii] > 1:
                gefahren_punkte += 1

print(gefahren_punkte)
