# Round 295, Div 2, Problem A
# https://codeforces.com/contest/520/problem/A

from string import ascii_lowercase
n = int(input())
inp = input()
inp = inp.lower()
if len(inp) < 26:
    print('NO')
else:
    for i in ascii_lowercase:
        if i in inp:
            pass
        else:
            print('NO')
            break
    else:
        print('YES')