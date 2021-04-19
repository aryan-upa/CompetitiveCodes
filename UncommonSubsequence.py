# Round 396, Div 2, Problem A
# https://codeforces.com/contest/766/problem/A

inp1 = input()
inp2 = input()
if inp1 == inp2:
    print(-1)
else:
    print(max(len(inp1), len(inp2)))