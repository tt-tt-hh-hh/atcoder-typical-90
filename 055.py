from re import X


import itertools

n, p, q = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0

for i in itertools.combinations(a,5):    
    if i[0]%p * i[1]%p * i[2]%p * i[3]%p * i[4]%p == q:
        ans += 1

print(ans)

