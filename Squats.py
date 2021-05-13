# Round 242, Div 2, Problem A
# https://codeforces.com/contest/424/problem/A

n = int(input())
ls = input()
val = abs(ls.count('X')-ls.count('x'))/2
print(int(val))
if val!=0:
    ch = 'X' if ls.count('X')<ls.count('x') else 'x'
    nstr = ''
    for i in ls:
        if val>0:
            if i!=ch:
                nstr+=ch
                val-=1
            else:
                nstr+=ch
        else:
            nstr+=i
    print(nstr)
else:
    print(ls)