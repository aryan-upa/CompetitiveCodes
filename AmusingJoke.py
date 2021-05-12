# Round 101, Div 2, Problem A
# https://codeforces.com/contest/141/problem/A

n1 = input()
n2 = input()
pi = input()
if len(n1+n2)!=len(pi):
    print('NO')
else:
    _ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for q in _:
        if pi.count(q)!=(n1+n2).count(q):
            print('NO')
            break
    else:
        print('YES')