# Beta Round 84, Div 2, Problem A
# https://codeforces.com/contest/110/problem/A

inp = input()
c = inp.count('7')+inp.count('4')
if c==7 or c==4:
    print('YES')
else:
    print('NO')
