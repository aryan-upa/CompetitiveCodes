# Round 399, Div 1 + Div2 (Combined), Problem A
# https://codeforces.com/contest/768/problem/A

inp = int(input())
ls = list(map(int, input().split()))
mi = min(ls)
mx = max(ls)
if mi != mx:
    print(len(ls)-ls.count(min(ls))-ls.count(max(ls)))
else:
    print(0)