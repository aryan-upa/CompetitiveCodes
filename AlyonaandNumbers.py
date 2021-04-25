# Round 358, Div 2, Problem A
# https://codeforces.com/contest/682/problem/A

m, n = map(int, input().split())
A = [0 for x in range(5)]
B = [0 for p in range(5)]
for i in range(1, m+1):
    A[i % 5] += 1
for i in range(1, n+1):
    B[i % 5] += 1
print(f'{A[0]*B[0]+A[1]*B[4]+A[2]*B[3]+A[3]*B[2]+A[4]*B[1]}')