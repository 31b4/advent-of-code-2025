ids = open("i.txt").read().split(',')

ans = 0

for id in ids:
    first, last = list(map(int, id.split('-')))
    for n in range(first, last+1):
        s = str(n)
        for i in range(1,(len(s)//2)+1):
            if s == (s[:i]*(len(s)//len(s[:i]))):
                ans += n
                break
        
print(ans)