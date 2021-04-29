# Beta Round 89, Div 2, Problem A
# http://codeforces.com/contest/118/problem/A

ls = list(map(str, input()))
for i in ls:
    if i.lower() not in ['a', 'o', 'y', 'e', 'u', 'i']:
        print('.'+i.lower(), end='')
    else:
        pass
