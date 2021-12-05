# Immer drei Zahlen der Eingabe zusammenaddieren, dann mit einen versetzt
# weitermachen

eingabe = []

while True:
    zeile = input()
    if zeile.isdigit():
        eingabe.append(int(zeile))
    else:
        break

summen = 0
for i in range(len(eingabe)-3):
	if eingabe[i]+eingabe[i+1]+eingabe[i+2] < eingabe[i+1] + eingabe[i+2] + eingabe[i+3]:
		summen += 1
print(summen)