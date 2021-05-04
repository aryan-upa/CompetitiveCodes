# Round 304, Div 2, Problem A
# https://codeforces.com/contest/546/problem/A

k,n,w = map(int, input().split())
want = k*w*(w+1)/2
if want-n<0:
    print(0)
else:
    print(int(want-n))