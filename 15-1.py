#!/usr/bin/python3
# Credits (in no specific order) to:
# u/RoughMedicine on Reddit (https://topaz.github.io/paste/#XQAAAQAIBwAAAAAAAAA0m0pnuFI8c/fBNAn6x25rtjB4jtldKRL87i//mqAHVHSbTT7z0TG5tgM7yMqCN/z2UtIUEhLFdHNHQSoP4tFmXkflYNQ6xKd2m+BFwAzA5wDCEnTpvsAA8O0Qj9h1WFI6kFSkVbBj2Z7IGmkJPr3wUUHP+mUNQAwqLwQrfuwLC46kPFEGKoOSu+4ijcc75b8AiMi1O7J8Zzhk0xwtUY4feiMOmfXSrL6ysDTK+aI3uFp/RX8xn06E7pG4aeIlR5wecoRqOOsXe5bCLAwSERfQ4tIlgEROGlNcyk0pZrW5RHdRceXqV78M3Ld2uuLvb3MFgv9TPB5dsRwatVWjVrF7KgDZGf5Na2wSHW8jx5RX0YT9SVFUusRYph0DZtQp0lgmMMxD5W4TpBtrMH4U810qlXaGpexlCOCg0aUnho1IIZETPjPGr+c7w7kZjeQP/YwECQ17wTP6lH3niXLmMipsSjvn13SCnz6MujWW31zqxuTlOC9RnZO8FeFAmkBSz+EGNqxoM2aC/51RgkKTV3cRQMHzoc4RA9b56YbmahWDb8V93UNRqzZqJkY6JMoCSHLJcKgqazd+CrWmmwvCjkxIVTB08kllLzni9qyWOSYT8q0tUH7OaNat5hqUxK8O3YgHAP4xy3Lo6WoRJJF6xq1fHZXX/zdu0huMac08ZcbocBijrJYcPXQDPWoIgc5oyJFzshCwjpA/nl9i6aXcI07VwhAmy7PjqiR0xA6IxB+lSyQ48G88k2su0BRJZN0//EuUKP6ZBejNpoogFrrreTypUkK+kaY2UEnkAiTol/y3k2/Kak8qj5FfntVS9Q0lXq24swInHX8h9NS+HLVrey7bTnvaISLx+dnJ70HUe5l1HEkudO8y0IOzrtiU7bztzY8ePkeOjMBhexDE1E1Rb5sKmybUbPFWSdPreTWmBqDeI30hKUQ1lnd8jq5aHOEs2RFOSkYQYiR5zYcv54AVOzzHP3p6d5ZsHdFvtrcnxXYn5Wy/eIjRMBPyqP9PkWwA)
# https://www.youtube.com/watch?v=KiOso3VE-vI
# https://www.youtube.com/watch?v=GazC3A4OQTE
# https://github.com/statneutrino/AdventOfCode/blob/main/2021/python/day15.py
 
from sys import stdin
from math import inf
from heapq import heapify, heappush, heappop

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

cave = []
for line in stdin:
    cave.append([int(x) for x in list(line.strip())])

width = len(cave[0])
height = len(cave)
visited = [[False]*width for x in range(height)]
queue = [(0, (0,0))]
heapify(queue)
distance = [[inf]*width for x in range(height)]
distance[0][0] = 0

while queue:
    cur_val, cur_pos = heappop(queue)
    if visited[cur_pos[0]][cur_pos[1]] == True:
        continue
    visited[cur_pos[0]][cur_pos[1]] = True
    for a in find_adjacents(cur_pos):
        if distance[cur_pos[0]][cur_pos[1]]+cave[a[0]][a[1]] < distance[a[0]][a[1]]:
            distance[a[0]][a[1]] = distance[cur_pos[0]][cur_pos[1]]+cave[a[0]][a[1]]
            heappush(queue, (distance[cur_pos[0]][cur_pos[1]]+cave[a[0]][a[1]], a))
print(distance[height-1][width-1])
