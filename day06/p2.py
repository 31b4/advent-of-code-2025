m = open("i.txt").read().splitlines()
ans = 0
block = 0

for i in range(len(m[-1])):
    if m[-1][i] != ' ': # if we found a new operator
        ans += block
        block = 0
        if m[-1][i] == '*':
            block = 1

    column = ""
    for j in range(len(m)-1):
        if m[j][i] != ' ':
            column += m[j][i]
            
    if column != "":
        if m[-1][i] == '*':
            block *= int(column)
        else:
            block += int(column)

ans += block
print(ans)