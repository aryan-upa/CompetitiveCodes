# Beta Round 57, Div 2, Problem A
# https://codeforces.com/contest/61/problem/A

inp1 = input()
inp2 = input()
res = eval('0b'+inp1)^eval('0b'+inp2)
print(bin(res)[2:].rjust(len(inp1),'0'))