p=50;a=b=0
for s in open('i.txt'):L=s<'R';d=int(s[1:])*(1-L*2);p+=d;b+=abs((p-L)//100-(p-d-L)//100);a+=p%100<1
print(a,b)