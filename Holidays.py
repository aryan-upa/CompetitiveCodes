# Round 350, Div 2, Problem A
# https://codeforces.com/contest/670/problem/A

n = int(input())
x = n//7*2
rem = n-(n//7)*7
if rem>5:
    print(x+1,x+2)
else:
    if rem>2:
        print(x,x+2)
    else:
        print(x,x+rem)
