m=open('i.txt').read().splitlines();n=[[*map(int,m[i].split())]for i in range(len(m)-1)];o=m[-1].split();r=range(len(n));print(sum(sum(n[j][i]for j in r)if o[i]=='+'else eval('*'.join(map(str,[n[j][i]for j in r])))for i in range(len(o))))
a=b=0
for i in range(len(m[0])):
 if m[-1][~i]>' ':a+=b;b=1if m[-1][~i]=='*'else 0
 c=''.join(m[j][~i]for j in r if m[j][~i]>' ')
 if c:b=b*int(c)if m[-1][~i]=='*'else b+int(c)
print(a+b)
