import math

a, b = list(map(int, input().split()))

def my_lcm(x, y):
    return (x*y)//math.gcd(x,y)

ans = my_lcm(a,b)

if ans > 10**18:
    print('Large')
else:
    print(ans)