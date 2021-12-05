# In einer Liste mit Binärzahlen, auf komische Art und Weisen Werte auslesen
report = []
while True:
	zeile = input()
	if zeile != "":
		report.append(list(map(int, list(zeile))))
	else:
		break

gamma = ""
epsilon = ""
for i in range(len(report[0])):
	nullen = 0
	einsen = 0
	for ii in range(len(report)):
		if report[ii][i] == 0:
			nullen += 1
		else:
			einsen += 1
	if nullen > einsen:
		gamma = gamma + "0"
		epsilon = epsilon + "1"
	else:
		gamma = gamma + "1"
		epsilon = epsilon + "0"
print(int(gamma,2)*int(epsilon,2))