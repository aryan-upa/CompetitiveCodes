# Round 268, Div 2, Problem A
# https://codeforces.com/contest/469/problem/A

inp = int(input())
ls1, ls2 = input(), input()
ls = ls1[1:]+' '+ls2[1:]
ls = list(map(int, ls.split()))
ls.sort()
for i in range(1, inp+1):
    if i in ls:
        pass
    else:
        print('Oh, my keyboard!')
        break
else:
    print('I become the guy.')