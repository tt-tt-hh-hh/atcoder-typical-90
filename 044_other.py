n, q = map(int,input().split())
a = list(map(int,input().split()))

shift = 0

for i in range(q):
    t,x,y = map(int, input().split())
    x, y = x-1, y-1

    X = (x-shift)
    Y = (y-shift)

    if t == 1:
        a[X],a[Y] = a[Y],a[X]
    elif t == 2:
        shift += 1
        shift %= n
    elif t == 3:
        print(a[X])