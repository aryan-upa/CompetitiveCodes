# Round 162, Div 2, Problem A
# https://codeforces.com/contest/265/problem/A

pos, ins, C = input(), input(), 0
for i in range(len(ins)):
    if ins[i] == pos[C]:
        C += 1
    else:
        pass
print(C+1)