# VK Cup 2012 Qualification Round 1, Problem A
# https://codeforces.com/contest/158/problem/A

n, k = map(int, input().split())
ls = list(map(int, input().split()))
_, val = 0, ls[k-1]
for i in ls:
    if i != 0:
        if i >= val:
            _ += 1
        else:
            print(_)
            break
    else:
        print(_)
        break
else:
    print(_)
