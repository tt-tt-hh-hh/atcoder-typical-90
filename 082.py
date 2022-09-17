L, R = list(map(int, input().split()))
MOD = 10**9+7
ans = 0

def cnt(a,b):
    if b < a:return 0
    return (a+b)*(b-a+1)//2

for i in range(1, 20):
    l, r = 10**(i-1), (10**i)-1

    ans += i*cnt(max(l,L), min(r,R))

print(ans%MOD)