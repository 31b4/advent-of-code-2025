m = open("i.txt").read().split("\n\n")
id_ranges = m[0].splitlines()

id_ranges = [tuple(map(int, r.split("-"))) for r in id_ranges]
id_ranges = sorted(id_ranges, key=lambda x: x[0])
ans = 0
new_ranges= []

i = 0
while i < len(id_ranges):
    start,end = id_ranges[i]
    j = i + 1
    while j < len(id_ranges):
        newstart,newend = id_ranges[j]
        if end >= newstart and newend < end: # if (1,10) and (2,5)
            i = j
        elif end >= newstart and newend>=end: # if (1,10) and (2,15)
            end = newend
            i = j
        elif end < newstart: # if (1,10) and (11,15)
            break
        j += 1

    new_ranges.append((start,end))
    i += 1

for r in new_ranges:
    ans += r[1]-r[0]+1
    
print(ans)