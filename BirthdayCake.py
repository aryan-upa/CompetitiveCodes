# Round 343, Div 2, Problem A
# https://codeforces.com/contest/629/problem/A

inp, ls = int(input()), list()
inp1, val = inp, 0
while inp>0:
    s = input()
    ls.append(s)
    _ = s.count('C')
    if _>1:
        val += int(((_)*(_-1))/2)
    inp-=1
nls = list()
for i in range(inp1):
    st = ''
    for q in ls:
        st += q[i]
    _ = st.count('C')
    if _>1:
        val += int(((_)*(_-1))/2)
    nls.append(st)
print(val)