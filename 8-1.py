from sys import stdin

woerter = []
for eingabe in stdin:
    if eingabe != '':
        zeile = eingabe.strip().split('|')[1].split(' ')
        for wort in zeile:
           woerter.append(wort) 
    else:
        break
eindeutig = 0
for wort in woerter:
    if len(wort) == 2 or len(wort) == 4 or len(wort) == 3 or len(wort) == 7:
        eindeutig += 1

print(eindeutig)
