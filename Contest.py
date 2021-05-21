# Round 285, Div 2, Problem A
# http://codeforces.com/contest/501/problem/A

a,b,c,d = map(int,input().split())
p1 = max(3*a/10,a - (a/250)*c)
p2 = max(3*b/10,b - (b/250)*d)
if p1>p2:
    print('Misha')
elif p2>p1:
    print('Vasya')
else:
    print('Tie')
