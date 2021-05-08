# Round 210, Div 2, Problem A
# https://codeforces.com/contest/361/problem/A

n, k = map(int, input().split())
Mat = [[k if j==p else 0 for j in range(n)] for p in range(n)]
for q in Mat: print(*q)

# Alternate Solution
# n, k = map(int,input().split())
# if k<n:
#     Mat = [[1 for q in range(n)] for i in range(n)]
#     rem_zero = n-k
#     for q in range(n):
#         for j in range(n):
#             if q+j==n-1:
#                 for i in range(rem_zero):
#                     Mat[q][j-i]=0
# else:
#     Mat = [[1 for q in range(n)] for i in range(n)]
#     rem = k - (n-1)
#     for q in range(n):
#         for j in range(n):
#             if q+j==n-1:
#                 Mat[q][j]=rem
#
# for j in Mat:
#     print(*j)
