# Round 283, Div 2, Problem A
# http://codeforces.com/contest/496/problem/A

n = int(input())
a = list(map(int,input().split()))
dif = [int(a[q+1]-a[q-1]) for q in range(1,n-1)]
a.pop(dif.index(min(dif))+1)
a = [a[q]-a[q-1] for q in range(1,n-1)]
print(max(a))
