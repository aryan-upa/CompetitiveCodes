# Beta Round 40, Div 2, Problem A
# http://codeforces.com/contest/41/problem/A

t, s = input(), input()
if t[::] == s[::-1]:
    print('YES')
else:
    print('NO')