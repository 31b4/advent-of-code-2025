S={(i,j)for i,l in enumerate(open('i.txt'))for j,c in enumerate(l)if'@'==c};N=lambda p:sum((p[0]+x,p[1]+y)in S for x in(-1,0,1)for y in(-1,0,1)if x|y);p=sum(N(q)<4for q in S);t=0
while(R:=[q for q in S if N(q)<4]):t+=len(R);S-=set(R)
print(p,t)