# Round 197, Div 2, Problem A
# http://codeforces.com/contest/339/problem/A

ls = list(map(int, input().split('+')))
ls = sorted(ls)
for i in range(len(ls)-1):
    print(ls[i], end='+')
else:
    print(ls[len(ls)-1])
