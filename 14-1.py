#!/usr/bin/python3
from sys import stdin

def step():
    tmp = []
    prev = ''
    for p in polymer:
        for s in steps:
            if s[0][0] == prev and s[0][1] == p:
                tmp.append(s[1])
        tmp.append(p)
        prev = p
    return tmp

count = 0
steps = []
for line in stdin:
    if count == 0:
        polymer = list(line.strip())
        count += 1
        continue
    elif count == 1:
        count += 1
        continue
    line = line.strip().split(' -> ')
    steps.append((tuple(line[0]), line[1]))

for i in range(10):
    polymer = step()

polymer_counts = []
for _ in ["N","C","H","B"]:
    polymer_counts.append(polymer.count(_))

polymer_counts.sort()
print(polymer_counts[-1]-polymer_counts[0])
