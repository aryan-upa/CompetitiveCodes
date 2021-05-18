# Round 398, Div 2, Problem A
# https://codeforces.com/contest/767/problem/A

# There were multiple attempts with TLEs in Python 3.7, but while
# submitting with PyPy 3.7 it worked just under the time constraints.

inp = int(input())
ls = list(map(int,input().split()))
m = inp; app = []
for i in range(inp):
    if m==ls[i]:
        print(m,end=' ')
        m-=1
        while m in app:
            print(m,end=' ')
            m-=1
    else:
        app.append(ls[i])
    print()