n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

ok = n
ng = -1

while abs(ok-ng) > 1:
    mid = (ok + ng) // 2

    if a[mid] >= k:
        ok = mid
    else:
        ng = mid

if ok != n:
    print(ok)
else:
    print(-1)