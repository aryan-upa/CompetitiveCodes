# Round 144, Div 2, Problem A
# https://codeforces.com/contest/228/problem/A


ls, count = list(map(int, input().split())), 0
for i in range(4):
    for q in range(i+1, 4):
        if ls[i] == ls[q]:
            count += 1
            break
        else:
            pass
print(count)