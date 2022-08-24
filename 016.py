n = int(input())
a, b, c = list(map(int, input().split()))
ans = 10**9

for i in range(10**4):
    for j in range(10**4):
        k = n - (a*i+b*j)
        if k%c == 0 and k>=0:
            ans = min(ans, i+j+k//c)
print(ans)



""" for i in range(9999):
    for j in range(0,9999-i):
        if (n-a*i-b*i)%c == 0:
            ans = min(ans, a+b+(n-a*i-b*i)%c)

print(ans) """
