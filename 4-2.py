ziehungen = input().split(",")
ziehungen = [int(x) for x in ziehungen]

boards = []

while True:
    leer = input()
    zeile = [input().split(" ")]
    zeile[0] = [int(x) for x in zeile[0] if x != '']
    if zeile[0] != []:
        for i in range(1,5):
            zeile.append(input().split(" "))
            zeile[i] = [int(x) for x in zeile[i] if x != '']
        boards.append([zeile[0], zeile[1], zeile[2], zeile[3], zeile[4]])
    else:
        break

freie_bretter = [x for x in range(len(boards))]
for n in range(len(ziehungen)):
    if len(freie_bretter) == 1:
        break
    for i in range(len(boards)):
        for ii in range(5):
            for iii in range(5):
                if boards[i][ii][iii] == ziehungen[n]:
                    boards[i][ii][iii] = "x"
    for i in range(len(boards)):
        if len(freie_bretter) == 1:
            break
        for ii in range(5):
            nicht_x = False
            for iii in range(5):
                if boards[i][ii][iii] != "x":
                    nicht_x = True
            if nicht_x == False and (i in freie_bretter):
                freie_bretter.remove(i)
                break

    for i in range(len(boards)):
        if len(freie_bretter) ==  1:
            break
        for ii in range(5):
            nicht_x = False
            for iii in range(5):
                if boards[i][iii][ii] != "x":
                    nicht_x = True
            if nicht_x == False and (i in freie_bretter):
                freie_bretter.remove(i)
                break
laufend = True
while laufend == True:
    for i in range(5):
        for ii in range(5):
            if boards[freie_bretter[0]][i][ii] == ziehungen[n]:
                boards[freie_bretter[0]][i][ii] = "x"
    for i in range(5):
        nicht_x = False
        for ii in range(5):
            if boards[freie_bretter[0]][i][ii] != "x":
                nicht_x = True
        if nicht_x == False:
            laufend = False
    for i in range(5):
        nicht_x = False
        for ii in range(5):
            if boards[freie_bretter[0]][ii][i] != "x":
                nicht_x = True
        if nicht_x == False:
            laufend = False
    n += 1
summe_unmarkierter = 0
for i in range(5):
    for ii in range(5):
        if boards[freie_bretter[0]][i][ii] != "x" :
            summe_unmarkierter += boards[freie_bretter[0]][i][ii]

print(summe_unmarkierter * ziehungen[n-1])
