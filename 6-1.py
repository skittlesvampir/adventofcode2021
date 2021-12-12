eingabe = input().split(",")
fische = [int(x) for x in eingabe]

for i in range(80):
    print(i)
    for ii in range(len(fische)):
        if fische[ii] == 0:
            fische[ii] =6
            fische.append(8)
        else:
            fische[ii] -=1

print(len(fische))
