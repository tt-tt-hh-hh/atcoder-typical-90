from collections import deque

n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
t = [list(map(int, input().split())) for _ in range(q)]
d = deque(a)

for i in range(q):
    ti = t[i][0]
    x = t[i][1]
    y = t[i][2]
    
    if ti == 1:
        d[x-1], d[y-1] = d[y-1], d[x-1]
    elif ti == 2:
        d.rotate()
    elif ti == 3:
        print(d[x-1])
