# Round 180, Div 2, Problem A
# http://codeforces.com/contest/298/problem/A

inp = int(input())
st = input()
dist = 0
pos = 0
for i in range(inp):
    if st[i] != '.':
        pos = dist = i
        break
for i in range(inp-1,0,-1):
    if st[i]!='.':
        dist = (i+1) - dist
        break
if st.count('L')==0:
    print(pos+1,pos+1+dist)
else:
    disp = dist -1 - st.count('L')
    print(pos+1,pos+disp+1)
