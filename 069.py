n, k = list(map(int, input().split()))

if n == 1:
    print(k)
    exit()

mod = 10**9 + 7

ans = k%mod * (k-1)%mod * pow((k-2), (n-2), mod)

print(ans%mod)