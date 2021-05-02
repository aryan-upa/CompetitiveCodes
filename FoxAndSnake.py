# Round 290, Div 2, Problem A
# https://codeforces.com/contest/510/problem/A

n, m = map(int, input().split())
c = 0
for i in range(1, n+1):
    if i%2!=0:
        print('#'*m)
    else:
        if c==0:
            print('.' * (m - 1) + "#")
            c+=1
        else:
            print('#'+'.'*(m-1))
            c-=1