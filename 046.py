n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

cnt_a, cnt_b, cnt_c = [0]*46, [0]*46, [0]*46

for i in range(n):
    cnt_a[a[i]%46] += 1
    cnt_b[b[i]%46] += 1
    cnt_c[c[i]%46] += 1

ans = 0

for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k)%46 == 0:
                ans += cnt_a[i]*cnt_b[j]*cnt_c[k]

print(ans)