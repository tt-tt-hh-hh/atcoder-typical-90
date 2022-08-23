n = int(input())
cp = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

c1 = [0]*n
c2 = [0]*n

for i in range(n):
    if cp[i][0] == 1:
        c1[i] = cp[i][1]
    else:
        c2[i] = cp[i][1]

s1 = [0]*(n+1)
s2 = [0]*(n+1)

for i in range(0,n):
    s1[i+1] = s1[i]+c1[i]

for i in range(0,n):
    s2[i+1] = s2[i]+c2[i]

for i in range(q):
    print(s1[lr[i][1]]-s1[lr[i][0]-1], end=' ')
    print(s2[lr[i][1]]-s2[lr[i][0]-1])

