# Beta Round 14, Div 2, Problem A
# http://codeforces.com/contest/14/problem/A

n, m = map(int, input().split())
ls = [input() for i in range(n)]
st1=0;st2=n-1
for i in range(n):
    if ls[i].count('*')!=0:
        st1 = i
        break
for i in range(n-1,-1,-1):
    if ls[i].count('*')!=0:
        st2 = i
        break
pos1 = min([i.find('*') for i in ls if i.count('*')!=0])
pos2 = max([i.rfind('*') for i in ls if i.count('*')!=0])
for i in ls[st1:st2+1]:
    print(i[pos1:pos2+1],sep='')
