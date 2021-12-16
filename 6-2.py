eingabe = input().split(",")
eingabe = [int(x) for x in eingabe]

fische = [0] * 9
for zahl in eingabe:
    fische[zahl] += 1

for i in range(256):
    temp = [0] * 9
    for i in range(1,9):
        temp[i-1] = fische[i]
    temp[6] += fische[0]
    temp[8] += fische[0]
    fische = temp

print(sum(fische))
