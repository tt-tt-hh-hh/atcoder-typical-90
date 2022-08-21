n = int(input())
ans = []

if n % 2 == 1:
    print()
    exit()

def isvalid(S):
    score = 0
    for c in S:
        if c == '(':
            score += 1
        else:
            score -= 1
        
        if score < 0:
            return False
    
    if score == 0:
        return True

for i in range(2**n):
    obj = ''
    l = 0
    r = 0
    for j in range(n):
        if ((i >> j) & 1):
            obj = '(' + obj
        else:
            obj = ')' + obj
    
    if isvalid(obj):
        ans.append(obj)
ans.sort()
print(*ans, sep='\n')



