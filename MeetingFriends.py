# Round 375, Div 2, Problem A
# https://codeforces.com/contest/723/problem/A

ls = list(map(int, input().split()))
ls.sort()
print(ls[1]-ls[0] + ls[2] - ls[1])