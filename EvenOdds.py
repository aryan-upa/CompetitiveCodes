# Round 188, Div 2, Problem A
# https://codeforces.com/contest/318/problem/A

n, k = map(int, input().split())
p = n/2 if n % 2 == 0 else (n+1)/2
print(f'{2*k-1 if k<=p else 2*int(k-p)}')