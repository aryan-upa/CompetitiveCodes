# (VK Cup Round 3) Round 412, Div 2, Problem A
# https://codeforces.com/contest/807/problem/A

inp, ls = int(input()), []
for i in range(inp):
    st, su = map(int, input().split())
    if st != su:
        print('rated')
        break
    else:
        ls.append(st)
else:
    for i in range(inp-1):
        if ls[i+1]<=ls[i]:
            pass
        else:
            print('unrated')
            break
    else:
        print('maybe')