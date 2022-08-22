h, w = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(h)]

row = []
col = []
b = []

for i in range(h):
    row.append(sum(a[i]))

for i in range(w):
    buf = 0
    for j in range(h):
        buf += a[j][i]
    col.append(buf)

for i in range(h):
    buf = []
    for j in range(w):
        buf.append(row[i]+col[j]-a[i][j])
    b.append(buf)

for i in range(h):
    print(*b[i])