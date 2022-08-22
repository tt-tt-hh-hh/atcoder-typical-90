n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]

def binary_search(ok, ng, th):
    while ok - ng > 1:
        mid = (ok+ng) // 2
        if a[mid] > th:
            ok = mid
        else:
            ng = mid
    
    return ok

a.sort()

for i in range(q):
    ok = n
    ng = -1
    th = b[i]

    idx = binary_search(ok, ng, th)
    if idx == 0:
        print(a[0]-th)
    elif idx == n:
        print(th-a[n-1])
    else:
        ans=min(a[idx]-th, th-a[idx-1])
        print(ans)

