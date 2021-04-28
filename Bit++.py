# Round 173, Div 2, Problem A
# http://codeforces.com/contest/282/problem/A

inp, _ = int(input()), 0
for i in range(inp):
    s = input()
    if '++' in s:
        _ += 1
    else:
        _ -= 1
else:
    print(_)
