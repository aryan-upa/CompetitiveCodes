# Round 165, Div 2, Problem A
# https://codeforces.com/contest/270/problem/A

inp = int(input())
while inp>0:
    x = int(input())
    if 360/(180-x) == 360//(180-x):
        print('YES')
    else:
        print('NO')
    inp-=1
