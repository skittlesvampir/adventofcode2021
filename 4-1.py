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

gewinn_brett = ''
for n in range(len(ziehungen)):
    letzte_zahl = ziehungen[n-1]
    if gewinn_brett != '':
        break
    for i in range(len(boards)):
        for ii in range(5):
            for iii in range(5):
                if boards[i][ii][iii] == ziehungen[n]:
                    boards[i][ii][iii] = "x"
    for i in range(len(boards)):
        if gewinn_brett != '':
            break
        for ii in range(5):
            nicht_x = False
            for iii in range(5):
                if boards[i][ii][iii] != "x":
                    nicht_x = True
            if nicht_x == False:
                gewinn_brett = i
                break

    for i in range(len(boards)):
       if gewinn_brett != '':
           break
       for ii in range(5):
           nicht_x = False
           for iii in range(5):
               if boards[i][iii][ii] != "x":
                   nicht_x = True
           if nicht_x == False:
                gewinn_brett = i
                break

summe_unmarkierter = 0
for i in range(5):
    for ii in range(5):
        if boards[gewinn_brett][i][ii] != "x":
            summe_unmarkierter += boards[gewinn_brett][i][ii]

print(summe_unmarkierter * letzte_zahl)
