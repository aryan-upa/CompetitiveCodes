# Round 279, Div 2, Problem A
# https://codeforces.com/contest/490/problem/A

n = int(input())
ls = list(map(int, input().split()))
o1 = ls.count(1)
o2 = ls.count(2)
o3 = ls.count(3)
if o1 and o2 and o3 == 0:
    print('0')
else:
    t = min(o1, o2, o3)
    print(t)  # Number of teams
    nls = []
    for i in range(t):
        T = []
        T.append(ls.index(1)+1)
        T.append(ls.index(2)+1)
        T.append(ls.index(3)+1)

        ls[ls.index(1)] = 0
        ls[ls.index(2)] = 0
        ls[ls.index(3)] = 0
        nls.append(T)
    for i in nls:
        for p in i:
            print(p, end=' ')
        print()
