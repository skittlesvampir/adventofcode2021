# Mit Befehen (up, down, forward) die finale Position des Uboots bestimmen
hor = 0
dep = 0
while True:
	zeile = str(input())
	if zeile != "":
		zeile = zeile.split(' ')
		command = zeile[0]
		x = int(zeile[1])
		if command == 'forward':
			hor += x
		elif command == 'down':
			dep += x
		elif command == 'up':
			dep -= x
	else:
		break
print(hor*dep)