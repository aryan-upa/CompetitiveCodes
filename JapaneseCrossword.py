# Round 374, Div 2, Problem A
# https://codeforces.com/contest/721/problem/A

k = int(input())
inp = input()
c,ls = 0,list()
for i in range(k):
    if inp[i] == 'B':
        c+=1
    else:
        if c==0:
            pass
        else:
            ls.append(c)
        c=0
else:
    if c==0:
        pass
    else:
        ls.append(c)
print(len(ls))
print(*ls)