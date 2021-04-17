# Round 359, Div 2, Problem A
# http://codeforces.com/contest/686/problem/A

a, b = input().split()
a, b = [int(a), int(b)]
distress = 0
total = b
for i in range(a):
    inp = eval(input())
    if total + inp < 0:
        distress = distress + 1
    else:
        total = total + inp
print(f'{total} {distress}')