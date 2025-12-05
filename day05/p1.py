m = open("i.txt").read().split("\n\n")
id_ranges = m[0].splitlines()
available_ids = list(map(int,m[1].splitlines()))
ans = 0
for idx in available_ids:
    for id_range in id_ranges:
        x,y = list(map(int,id_range.split("-")))
        if idx >= x and idx<=y:
            ans +=1
            break

print(ans)