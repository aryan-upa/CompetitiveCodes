# Round 277, Div 2, Problem A
# https://codeforces.com/contest/486/problem/A

inp = int(input())
if inp % 2 == 0:
    s = 1
    print(int(s*inp/2))
else:
    s = -1
    print(s*int((inp + 1) / 2))