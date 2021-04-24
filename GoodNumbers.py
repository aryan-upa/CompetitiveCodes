# Round 213, Div 2, Problem A
# https://codeforces.com/contest/365/problem/A

n, k = map(int, input().split())
_ = 0
for i in range(n):
    inp = input()
    for q in range(k+1):
        if inp.count(str(q)) == 0:
            break
    else:
        _ += 1
else:
    print(_)