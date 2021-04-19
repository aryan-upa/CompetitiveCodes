# Round 271, Div 2, Problem A
# https://codeforces.com/contest/474/problem/A

S = input()
inp = list(input())
S = -1 if S == 'R' else 1
l1 = 'qwertyuiop'
l2 = 'asdfghjkl;'
l3 = 'zxcvbnm,./'
for i in range(len(inp)):
    if inp[i] in l1:
        inp[i] = l1[l1.index(inp[i]) + S]
    elif inp[i] in l2:
        inp[i] = l2[l2.index(inp[i]) + S]
    else:
        inp[i] = l3[l3.index(inp[i]) + S]
print(*inp, sep='')
