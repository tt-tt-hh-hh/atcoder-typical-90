import itertools

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
xy = [list(map(int, input().split())) for _ in range(m)]

kenaku = {}
for i in range(m):
    kenaku[str(xy[i][0]-1)+str(xy[i][1]-1)]=True
    kenaku[str(xy[i][1]-1)+str(xy[i][0]-1)]=True


ans = 10**5
odr = list(itertools.permutations(range(n), n))

for i in odr:
    Bool = True
    for j in range(n-1):
        if kenaku.get(str(i[j])+str(i[j+1]), False):
            Bool = False
            break
    
    cnt = 0
    if Bool:
        for j in range(n):
            cnt += a[i[j]][j]
        ans = min(ans, cnt)

if ans == 10**5:
    print(-1)
else:
    print(ans)



