# In einer Liste mit Binärzahlen, auf komische Art und Weisen Werte auslesen
def concat(liste):
	neu = ""
	for i in range(len(liste)):
		for ii in range(len(liste[0])):
			#neu.append(str(liste[i][ii]))
			neu = neu + str(liste[i][ii])
	return neu
report = []
while True:
	zeile = input()
	if zeile != "":
		report.append(list(map(int, list(zeile))))
	else:
		break

zahlen = report
for i in range(len(report[0])):
	zahlen_neu = []
	nullen = 0
	einsen = 0
	for ii in range(len(zahlen)):
		if zahlen[ii][i] == 0:
			nullen += 1
		else:
			einsen += 1
	if einsen >= nullen:
		for ii in range(len(zahlen)):
			if zahlen[ii][i] == 1:
				zahlen_neu.append(zahlen[ii])
	else:
		for ii in range(len(zahlen)):
			if zahlen[ii][i] == 0:
				zahlen_neu.append(zahlen[ii])
	zahlen = zahlen_neu
	if len(zahlen) == 0:
		break

oxygen = zahlen

zahlen = report
for i in range(len(report[0])):
	zahlen_neu = []
	nullen = 0
	einsen = 0
	for ii in range(len(zahlen)):
		if zahlen[ii][i] == 0:
			nullen += 1
		else:
			einsen += 1
	if nullen <= einsen:
		for ii in range(len(zahlen)):
			if zahlen[ii][i] == 0:
				zahlen_neu.append(zahlen[ii])
	else:
		for ii in range(len(zahlen)):
			if zahlen[ii][i] == 1:
				zahlen_neu.append(zahlen[ii])
	zahlen = zahlen_neu
	if len(zahlen) == 1:
		break

co2 = zahlen
oxygen = concat(oxygen)
co2 = concat(co2)
print(int(oxygen, 2)*int(co2, 2))