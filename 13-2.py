#!/usr/bin/python3
from sys import stdin

def fold_y(line):
	global paper
	line -= 1
	paper_new = [paper[x] for x in range(line+1)]
	for i in range(len(paper)-1,line,-1):
		for ii in range(len(paper[0])):
			if paper[i][ii] == "#":
				paper_new[len(paper)-1-i][ii] = "#"
	paper = paper_new

def fold_x(line):
	global paper
	paper_new = [x[:line] for x in paper]	
	for i in range(len(paper)):
		for ii in range(line+1,len(paper[0])):
			if paper[i][ii] == "#":
				paper_new[i][len(paper[0])-1-ii] = "#"
	paper = paper_new

lines = []
folds = []
max_x = 0
max_y = 0
phase = 0
for line in stdin:
	line = line.strip()
	if phase != 1 and line == '':
		phase = 1
		continue
	if phase != 1:	
		splitted = [int(x) for x in line.split(',')]
		lines.append(splitted)
		if splitted[0] > max_x:
			max_x = splitted[0]
		if splitted[1] > max_y:
			max_y = splitted[1]
	else:
		a,b = line.split(' ')[2].split('=')
		b = int(b)
		folds.append([a,b])
max_x += 1
max_y += 1
paper = [["."]*max_x for x in range(max_y)]
for x,y in lines:
	paper[y][x] = "#"
for f in folds:
	if f[0] == "x":
		fold_x(f[1])
	else:
		fold_y(f[1])
for p in paper:
	tmp = ""
	for pp in p:
		if pp == ".":
			tmp = tmp + " "
		else:
			tmp = tmp + "█"
	print(tmp)
