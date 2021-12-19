#!/usr/bin/python3
from sys import stdin

connection = {}

for line in stdin:
    line = line.strip().split("-")
    if line[0] not in connection:
        connection[line[0]] = []
    if line[1] not in connection:
        connection[line[1]] = []
    connection[line[0]].append(line[1])
    connection[line[1]].append(line[0])

q = [["start"]]
paths = []
while q:
    popped = q.pop(0)
    if popped[-1] == "end":
        paths.append(popped)
    else:
        for neighbor in connection[popped[-1]]:
            if neighbor != "start" :
                if neighbor.islower() and neighbor in popped:
                    continue
                tmp = popped.copy()
                tmp.append(neighbor)
                q.append(tmp)

print(len(paths))
