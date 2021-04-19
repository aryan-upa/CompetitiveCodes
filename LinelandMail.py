# Round Pi, Div 2, Problem A
# https://codeforces.com/contest/567/problem/A

inp = int(input())
ls = list(map(int, input().split()))
for i in range(inp):
    if i != 0 and i != inp-1:
        Mx = max(abs(ls[0]-ls[i]), abs(ls[i]-ls[inp-1]))
        Mn = min(abs(ls[i-1]-ls[i]), abs(ls[i]-ls[i+1]))
    else:
        Mx = abs(ls[0] - ls[inp - 1])
        if i == 0:
            Mn = abs(ls[0] - ls[1])
        else:
            Mn = abs(ls[inp-1]-ls[inp-2])
    print(Mn, Mx)
