# Round 134, Div 2, Problem A
# https://codeforces.com/contest/218/problem/A

n, k = map(int, input().split())
ls = list(map(int, input().split()))
ind, C = list(range(1, 2*n+1, 2)), 0
while k > 0:
    pos = ind[C]
    if ls[pos]-1 > ls[pos-1] and ls[pos]-1 > ls[pos+1]:
        ls[pos] -= 1
        k -= 1
    C += 1
print(*ls)