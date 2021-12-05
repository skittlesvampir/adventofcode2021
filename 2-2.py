# Mit Befehen (up, down, forward) die finale Position des Uboots bestimmen
# up und down verändern nur aim, die zu der Tiefe wird x*aim hinzuaddiert
hor = 0
dep = 0
aim = 0
while True:
	zeile = str(input())
	if zeile != "":
		zeile = zeile.split(' ')
		command = zeile[0]
		x = int(zeile[1])
		if command == 'forward':
			hor += x
			dep += aim*x
		elif command == 'down':
			aim += x
		elif command == 'up':
			aim -= x
	else:
		break
print(hor*dep)