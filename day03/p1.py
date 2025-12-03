raw = open("i.txt").read().splitlines()
batteries = [list(map(int, x)) for x in raw]
ans = 0

for b in batteries:
    first_max = max(b[:-1])
    i_first_max = b.index(first_max)
    second_max = max(b[i_first_max+1:]) # second max after the index of first max
    ans += int(str(first_max)+str(second_max))

print(ans)