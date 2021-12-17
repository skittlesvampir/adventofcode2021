#!/usr/bin/python3
from sys import stdin
import numpy as np

def expand_cave(cave_old):
    # expand to the right first
    cave_new = []
    for l in cave_old:
        tmp = [l]
        for i in range(4):
            tmmp = []
            for ii in tmp[-1]:
                if ii < 9:
                    tmmp.append(ii+1)
                else:
                    tmmp.append(1)
            tmp.append(tmmp)
        finished_line = []
        for a in tmp:
            for b in a:
                finished_line.append(b)
        cave_new.append(finished_line)
    # expand it to the bottom
    for i in range(len(cave_new),len(cave_new)*5):
        tmp_old = cave_new[i-len(cave)]
        tmp_new = []
        for ii in tmp_old:
            if ii < 9:
                tmp_new.append(ii+1)
            else:
                tmp_new.append(1)
        cave_new.append(tmp_new)
    return cave_new
def find_min(l):
    min = np.inf
    for a in range(height):
        for b in range(width):
            if l[a][b] < min and visited[a][b] == False:
                min = l[a][b]
                element = (a,b)
    return element

def find_adjacents(node): # "adjacent" heißt angrenzen oder benachbart
    y, x = node
    adjacents = set()
    if node[0] > 0:
        adjacents.add((y-1,x))
    if node[0] < height-1:
       	adjacents.add((y+1,x))
    if node[1] > 0:
        adjacents.add((y,x-1))
    if node[1] < width-1:
        adjacents.add((y,x+1))
    return adjacents

def is_every_node_visited(l):
    all_visited = True
    for a in visited:
        if a.count(False) > 0:
            all_visited = False
    return all_visited

cave = []
for line in stdin:
    cave.append([int(x) for x in list(line.strip())])
cave = expand_cave(cave)
width = len(cave[0])
height = len(cave)
visited = [[False]*width for x in range(height)]
distance = [[np.inf]*width for x in range(height)]
distance[0][0] = 0
while True:
    current = find_min(distance)
    visited[current[0]][current[1]] = True
    for a in find_adjacents(current):
        if distance[current[0]][current[1]]+cave[a[0]][a[1]] < distance[a[0]][a[1]]:
            distance[a[0]][a[1]] = distance[current[0]][current[1]]+cave[a[0]][a[1]]
    if is_every_node_visited(visited):
    	break
print(distance[height-1][width-1])
