n = int(input())
s = [input() for _ in range(n)]

l = set()
cnt = 0

for i in range(n):
    user = s[i]
    cnt += 1
    if user in l:
        continue
    else:
        l.add(user)
        print(cnt)