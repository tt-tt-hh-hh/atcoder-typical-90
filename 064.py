n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
lrv = [list(map(int, input().split())) for _ in range(q)]
b = []
now = 0

for i in range(n-1):
    b.append(a[i+1]-a[i])
    now += abs(a[i+1]-a[i])

for i in range(q):
    l, r, v = lrv[i]

    if l > 1:
        l -= 2
        now -= abs(b[l])
        b[l] += v
        now += abs(b[l])
    if r < n:
        r -= 1
        now -= abs(b[r])
        b[r] -= v
        now += abs(b[r])
    print(now)