m = open("i.txt").read().splitlines()
nums = []
for i in range(len(m)-1):
    nums.append(list(map(int, m[i].split())))
operators = m[-1].split()
ans = 0

for i in range(len(nums[0])):
    s = 0
    if operators[i] == '*':
        s = 1
    for j in range(len(nums)):
        if operators[i] == '*':
            s *= nums[j][i]
        else:
            s += nums[j][i]
    ans += s

print(ans)