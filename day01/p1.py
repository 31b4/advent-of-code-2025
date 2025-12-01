rotations = open("i.txt").read().splitlines()
STATE = 50
ans = 0

for x in rotations:
    d, n = x[0], int(x[1:])
    if d == "R":
        STATE = (STATE + n)%100
    else:
        STATE = (STATE - n)%100
    if STATE == 0:
        ans += 1

print(ans)