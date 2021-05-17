# Round 581, Div 2, Problem A
# https://codeforces.com/contest/1204/problem/A

from math import ceil
st = input()
st = st[::-1]
val = len(st)-1
if st!='0' or st!='1':
    if st.count('1')>1:
        print(int(val/2)+1)
    else:
        print(ceil(val/2))
else:
    print(0)