from sys import stdin
numbers = []
low_points = []
for line in stdin:
	numbers.append([int(x) for x in list(line.strip())])

len_line = len(numbers[0])
len_rows = len(numbers)
for i in range(len_rows):
	for ii in range(len_line):
		neighbor = []
		if ii > 0:
			neighbor.append(numbers[i][ii-1])
		if ii < len_line-1:
			neighbor.append(numbers[i][ii+1])
		if i > 0:
			neighbor.append(numbers[i-1][ii])
		if i < len_rows-1:
			neighbor.append(numbers[i+1][ii])
		low_point = True
		for a in neighbor:
			if a <= numbers[i][ii]:
				low_point = False
		if low_point == True:
			low_points.append(numbers[i][ii])

summe = 0
for point in low_points:
    summe += 1
    summe += point

print(summe)
