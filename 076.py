n = int(input())
a = list(map(int, input().split()))
import bisect

aa = a+a
#print(aa)

#累積和
s = [0]*(n*2+1)
s[0] = 0

for i in range(n*2):
    s[i+1] = s[i] + aa[i]

if s[n]%10 != 0:
    print('No')
    exit()

num = s[n]//10

for i in range(n):
    j = bisect.bisect_left(s, num+s[i])
    if s[j] - s[i] == num:
        print('Yes')
        exit()
print('No')
