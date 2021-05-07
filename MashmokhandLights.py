# Round 240, Div 2, Problem A
# https://codeforces.com/contest/415/problem/A

n, s = map(int,input().split())
ps = list(map(int, input().split()))
ls = [0 for i in range(n)]
for q in ps:
    if q == 1:
        for j in range(len(ls)):
            if ls[j]==0:
                ls[j]=1
        break
    else:
        for j in range(q-1,len(ls)):
            if ls[j]==0:
                ls[j] = q
print(*ls)