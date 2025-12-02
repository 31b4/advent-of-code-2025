p=q=0
for r in open('i.txt').read().split(','):
 for i in range(*map(int,r.split('-')),1):
  s=str(i);l=len(s)
  for d in range(2,l+1):
   if s==s[:l//d]*d:p+=d<3and i;q+=i;break
print(p,q)