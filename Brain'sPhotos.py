# Round 368, Div 2, Problem A
# https://codeforces.com/contest/707/problem/A

l, b = map(int, input().split())
for i in range(l):
    inp = input()
    if 'C' in inp or 'M' in inp or 'Y' in inp:
        print("#Color")
        break
else:
    print("#Black&White")