n = int(input())
s = input()

S = [0]*(n+1)
S[0] = 0

for i in range(n):
    if s[i] == 'o':
        buf = 1
    else:
        buf = 0

    S[i+1] = S[i]+buf

