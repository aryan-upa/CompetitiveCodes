# Beta Round 9, Div 2, Problem A
# https://codeforces.com/contest/9/problem/A


a, b = map(int, input().split())
lar = a if a > b else b
if lar == 6:
    print("1/6")
elif lar == 5:
    print("1/3")
elif lar == 4:
    print("1/2")
elif lar == 3:
    print("2/3")
elif lar == 2:
    print("5/6")
else:
    print("1/1")