# Round 139, Div 2, Problem A
# https://codeforces.com/contest/225/problem/A

n = int(input())
x = int(input())
hid = 7-x
for i in range(n):
    hid = 7-x
    a, b = map(int, input().split())
    if hid in [7-a, 7-b, a, b]:
        print("NO")
        break
    else:
        x = hid
else:
    print('YES')