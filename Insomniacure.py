# Round 105, Div 2, Problem A
# https://codeforces.com/contest/148/problem/A

ls = []
for q in range(5): ls.append(int(input()))
d = ls.pop(4); _ = 0
if 1 in ls:
    print(d)
else:
    p = list(range(1,d+1))
    for q in ls:
        for i in range(len(p)):
            if p[i] % q==0:
                p[i] = 0
                _+=1
        p = [j for j in p if j!=0]
        # print(p)
    else:
        print(_)
