# Round 156, Div 2, Problem A
# https://codeforces.com/contest/255/problem/A

inp = int(input())
ls = list(map(int, input().split()))
ch,bi,ba,c = 0,0,0,0
for i in ls:
    if c==0:
        ch+=i
        c+=1
    elif c==1:
        bi+=i
        c+=1
    else:
        ba+=i
        c=0
else:
    m = max(ch,bi,ba)
    if m==ch:
        print('chest')
    elif m==bi:
        print('biceps')
    else:
        print('back')