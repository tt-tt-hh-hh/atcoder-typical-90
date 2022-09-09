n, k = list(map(int, input().split()))

def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)


def DeciamlToNine(num):
    "10進数を9進数に変換する"
    nine_number = ""
    while num > 0:
        nine_number += str(num % 9)
        num //= 9
    return int(nine_number[::-1])

m = str(n)

if n == 0:
    print(0)
    exit()

for i in range(k):
    n10 = int(m,8)
    n9 = DeciamlToNine(n10)
    ans = str(n9).replace('8', '5') #string

    m = ans

print(ans)