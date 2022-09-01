n, k = list(map(int, input().split()))
ab = []
ans = 0

for _ in range(n):
    a, b = list(map(int, input().split()))
    ab.append(a-b)
    ab.append(b)

ab.sort(reverse=True)

for i in range(k):
    ans += ab[i]

print(ans)

