raw = open("i.txt").read().splitlines()
batteries = [list(map(int, x)) for x in raw]
ans = 0

for b in batteries:
    sv = b
    battery = ""
    for x in range(11,-1,-1):
        if x == 0:
            battery += str(max(sv))
            break
        first_max = max(sv[:-x])
        battery += str(first_max)
        i_first_max = sv.index(first_max)
        sv = sv[i_first_max+1::]
    ans += int(battery)
print(ans)