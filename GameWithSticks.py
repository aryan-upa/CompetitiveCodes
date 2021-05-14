# Round 258, Div 2, Problem A
# https://codeforces.com/contest/451/problem/A

r,c=  map(int,input().split())
if r==c:
    if r%2==0:
        print("Malvika")
    else:
        print("Akshat")
else:
    if min(r,c)%2==0:
        print("Malvika")
    else:
        print("Akshat")
