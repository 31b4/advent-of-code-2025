R,I=open("i.txt").read().split("\n\n");M=[]
for s,e in sorted(tuple(map(int,r.split("-")))for r in R.split()):M=M+[(s,e)]if not M or s>M[-1][1]else M[:-1]+[(M[-1][0],max(M[-1][1],e))]
print(sum(any(s<=int(i)<=e for s,e in M)for i in I.split()),sum(e-s+1for s,e in M))
