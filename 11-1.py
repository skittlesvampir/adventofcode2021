#!/usr/bin/python3
class Octopus:
    def __init__(self, level, x, y):
        self.level = level
        self.x = x
        self.y = y
    def incr(self):
        self.level += 1
        if self.level == 10:
	        if self.x < 9 and self.y > 0:
	            octopi[self.y-1][self.x+1].incr()
	        if self.x < 9:
	            octopi[self.y][self.x+1].incr()
	        if self.x < 9 and self.y < 9:
	            octopi[self.y+1][self.x+1].incr()
	        if self.y < 9:
	            octopi[self.y+1][self.x].incr()
	        if self.x > 0 and self.y < 9:
	            octopi[self.y+1][self.x-1].incr()
	        if self.x > 0:
	            octopi[self.y][self.x-1].incr()
	        if self.x > 0 and self.y > 0:
	            octopi[self.y-1][self.x-1].incr()
	        if self.y > 0:
	            octopi[self.y-1][self.x].incr()

def step():
    global flashes
    for a in octopi:
    	for b in a:
        	b.incr()
    for a in octopi:
        for b in a:
            if b.level > 9:
                flashes += 1
                b.level = 0
octopi =[[None]*10 for x in range(10)]
flashes = 0
for i in range(10):
    line = list(input())
    for ii in range(10):
        octopi[i][ii] = Octopus(int(line[ii]), ii, i)

for i in range(100):
    step()

print(flashes)
