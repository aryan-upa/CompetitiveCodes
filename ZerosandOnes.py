# Round 310, Div 2, Problem A
# http://codeforces.com/contest/556/problem/A

from math import fabs
inp = int(input())
st = input()
print(int(fabs(st.count('1')-st.count('0'))))