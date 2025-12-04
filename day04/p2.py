m = open("i.txt").read().splitlines()
ans = 0
m = [list(x) for x in m]
DIRS = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
sv = m

while True:
    r = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            counter = 0
            if m[i][j] != '@':
                continue
            for x,y in DIRS:
                if i+x == len(m) or i+x == -1 or  j+y == len(m[i]) or j+y == -1:
                    continue
                if m[i+x][j+y] == '@':
                    counter += 1
            if counter < 4:
                sv[i][j] = 'x'
                r+=1
    if r == 0:
        break

    ans += r
    m = sv

print(ans)