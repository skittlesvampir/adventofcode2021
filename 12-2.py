#!/usr/bin/python3
from sys import stdin

def small_cave_checker(node, path):
    if node.islower() and path.count(node) > 0:
        for x in path:
            if x.islower() and path.count(x) > 1:
                return False
    return True

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
            if small_cave_checker(neighbor, popped) and neighbor != "start":
                tmp = popped.copy() # if ".copy()" is not there, then changing "tmp" will also change "popped"
                tmp.append(neighbor)
                q.append(tmp)

print(len(paths))
