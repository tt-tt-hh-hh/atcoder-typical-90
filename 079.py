h, w = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]

cnt = 0

for i in range(h-1):
    for j in range(w-1):
        if a[i][j] == b[i][j]:
            continue
        elif a[i][j] < b[i][j]:
            d = b[i][j] - a[i][j]

            a[i][j] += d
            a[i+1][j] += d
            a[i][j+1] += d
            a[i+1][j+1] += d
            cnt += d
        elif a[i][j] > b[i][j]:
            d = a[i][j] - b[i][j]

            a[i][j] -= d
            a[i+1][j] -= d
            a[i][j+1] -= d
            a[i+1][j+1] -= d
            cnt += d

if a == b:
    print('Yes')
    print(cnt)
else:
    print('No')