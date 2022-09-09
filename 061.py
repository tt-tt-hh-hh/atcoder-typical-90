from collections import deque
q = int(input())
tx = [list(map(int, input().split())) for _ in range(q)]

d = deque()

for i in range(q):
    t = tx[i][0]
    x = tx[i][1]

    if t == 1:
        d.appendleft(x)
    elif t == 2:
        d.append(x)
    elif t == 3:
        print(d[x-1])
