# Round 291, Div 2, Problem A
# https://codeforces.com/contest/514/problem/A

inp = input()
ls = [int(x) for x in inp]
if ls[0] < 5 or ls[0] == 9:
    pass
else:
    ls[0] = 9-ls[0]
for i in range(1, len(ls)):
    if ls[i] < 5:
        pass
    else:
        ls[i] = 9-ls[i]
ls = [str(x) for x in ls]
print(*ls, sep='')