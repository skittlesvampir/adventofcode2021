def incrementer(krabbe,i):
    if krabbe > i:
        incr = -1
    else:
        incr = 1
    return incr

eingabe = input().split(",")
krabben = [int(x) for x in eingabe]

max = 0
for krabbe in krabben:
    if krabbe > max:
        max = krabbe
min = max
for krabbe in krabben:
    if krabbe < min:
        min = krabbe

min_fuel = 0
for krabbe in krabben:
    min_fuel += (abs(krabbe-1)**2+abs(krabbe-1))//2

for i in range(1,max+1):
    tmp = 0
    for krabbe in krabben:
        tmp += ((abs(krabbe-i))**2+abs(krabbe-i))//2
    if tmp < min_fuel:
        min_fuel = tmp

print(min_fuel)
