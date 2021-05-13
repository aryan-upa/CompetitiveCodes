# Round 103, Div 2, Problem A
# https://codeforces.com/contest/144/problem/A

n = int(input())
ls = list(map(int,input().split()))
M = max(ls); m = min(ls)
if ls[0]==M and ls[-1]==m:
    print(0)
else:
    pos = ls.index(M); _=0
    _ = pos
    if pos!=0:
        while pos!=0:
            ls[pos],ls[pos-1] = ls[pos-1],ls[pos]
            pos-=1
    pos2 = 0
    for q in ls[::-1]:
        if q == m:
            break
        else:
            pos2+=1
    print(_ + pos2)