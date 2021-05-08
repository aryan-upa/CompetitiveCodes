# Round 160, Div 2, Problem A
# https://codeforces.com/contest/262/problem/A3

n, k = map(int, input().split())
_ = 0
ls = list(map(str,input().split()))
for s in ls:
    if len(s)<=k:
        _+=1
    else:
        if s.count('7')+s.count('4')<=k:
            _+=1
print(_)