from sys import stdin

def is_lowpoint(i,ii):
	neighbor = []
	if ii > 0:
		neighbor.append(numbers[i][ii-1])
	if ii < len_line-1:
		neighbor.append(numbers[i][ii+1])
	if i > 0:
		neighbor.append(numbers[i-1][ii])
	if i < len_rows-1:
		neighbor.append(numbers[i+1][ii])
	for a in neighbor:
		if a <= numbers[i][ii]:
			return False
	return True

def find_basin(i,ii):
	if numbers[i][ii] == 9:
		return
	while True:
		if is_lowpoint(i,ii):
			basin[(i,ii)] += 1
			return
		directions = {}
		if ii > 0:
			directions["left"] = numbers[i][ii-1]
		if ii < len_line-1:
			directions["right"] = numbers[i][ii+1]
		if i > 0:
			directions["up"] = numbers[i-1][ii]
		if i < len_rows-1:
			directions["down"] = numbers[i+1][ii]
		minimum = min(directions.values())
		for x in directions:
			if directions[x] == minimum:
				go = x
				break
		if go == "down":
			i += 1
		elif go == "up":
			i -= 1
		elif go == "left":
			ii -= 1
		elif go == "right":
			ii += 1
				
numbers = []
low_points = []
for line in stdin:
	numbers.append([int(x) for x in list(line.strip())])

len_line = len(numbers[0])
len_rows = len(numbers)
basin = {}
for i in range(len_rows):
	for ii in range(len_line):
		if is_lowpoint(i,ii) == True:
			basin[(i,ii)] = 0
			low_points.append((i,ii))

for i in range(len_rows):
	for ii in range(len_line):
		find_basin(i,ii)

list = []
for e in basin:
	list.append(basin[e])
list.sort(reverse = True)
print(list[0] * list[1] * list[2])
