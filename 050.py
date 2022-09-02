n, l = list(map(int, input().split()))

#i段目に到達するまでの移動方法の数をdp[i]とする

dp = [0]*(n+1)
dp[0] = 1

for i in range(1, n+1):
    if i < l:
        dp[i] = dp[i-1]
    elif i >= l:
        dp[i] = dp[i-1] + dp[i-l]
    
    dp[i] %= (10**9+7)

print(dp[n])