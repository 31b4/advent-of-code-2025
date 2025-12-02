ids = open("i.txt").read().split(',')

ans = 0

for id in ids:
    first, last = list(map(int, id.split('-')))
    for n in range(first, last+1):
        s = str(n)
        
        if s[:len(s)//2] == s[len(s)//2:]:
            ans += n

print(ans)