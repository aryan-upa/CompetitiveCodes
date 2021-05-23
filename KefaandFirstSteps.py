# Round 21, Div 2, Problem A
# http://codeforces.com/contest/580/problem/A

inp = int(input())
ls = list(map(int, input().split()))
val = 1; ans = []
for i in range(1,inp):
    if ls[i]>=ls[i-1]:
        val+=1
    else:
        ans.append(val)
        val = 1
else:
    ans.append(val)
    print(max(ans))
