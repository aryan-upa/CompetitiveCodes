# Beta Round 25, Div 2, Problem A
# https://codeforces.com/contest/25/problem/A

inp = int(input())
ls = list(map(int, input().split()))
for i in range(1,inp,2):
    if i==inp-1:
        print(inp)
        break
    if ls[i-1] % 2==ls[i] % 2==ls[i+1] % 2:
        pass
    else:
        if ls[i-1] % 2==ls[i+1] % 2:
            print(i+1)
            break
        elif ls[i] % 2==ls[i+1] % 2:
            print(i)
            break
        else:
            print(i+2)
            break
