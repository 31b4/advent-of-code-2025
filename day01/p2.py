rotations = open("i.txt").read().splitlines()
STATE = 50
ans = 0

for x in rotations:
    d, n = x[0], int(x[1:])
    if d == "R":
        rotations = (STATE + n) // 100
        ans += rotations
        STATE = (STATE + n) % 100 
    else:
        rotations = abs((STATE - n)) // 100
        if STATE - n <= 0 and STATE != 0:
            ans += 1
        ans += rotations
        STATE = (STATE - n) % 100 

print(ans)