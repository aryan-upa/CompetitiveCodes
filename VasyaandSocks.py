# Round 262, Div 2, Problem A
# https://codeforces.com/contest/460/problem/A

n,m = map(int,input().split())
stock = n; day = 0
while stock!=0:
    day+=1
    stock-=1
    if day%m==0:
        stock+=1
    if stock==0:
        break
print(day)