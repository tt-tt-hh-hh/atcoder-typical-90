n, m = list(map(int, input().split()))
v = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = list(map(int, input().split()))
    v[a].append(b)
    v[b].append(a)

ans = 0

for i in range(1, len(v)):
    cnt = 0
    for j in range(len(v[i])):
        if v[i][j] < i:
            cnt += 1
    
    if cnt == 1:
        ans += 1

print(ans)
