# Round 176, Div 2, Problem A
# https://codeforces.com/contest/287/problem/A

ls = []
for i in range(4):
    st = input()
    ls.append(st)
for i in range(4):
    if i == 0 or i == 3:
        if i==0:
            if '##' in ls[i]:
                pos = ls[i].index('##')
                if ls[i + 1][pos] == '#' or ls[i + 1][pos + 1] == '#':
                    print('YES')
                    break
        else:
            if '##' in ls[i]:
                pos = ls[i].index('##')
                if ls[i - 1][pos] == '#' or ls[i - 1][pos + 1] == '#':
                    print('YES')
                    break
    else:
        if '##' in ls[i]:
            pos = ls[i].index('##')
            if ls[i-1][pos] == '#' or ls[i-1][pos+1] == '#':
                print('YES')
                break
            elif ls[i+1][pos] == '#' or ls[i+1][pos+1] == '#':
                print('YES')
                break
    if i == 0 or i == 3:
        if i==0:
            if '..' in ls[i]:
                pos = ls[i].index('..')
                if ls[i + 1][pos] == '.' or ls[i + 1][pos + 1] == '.':
                    print('YES')
                    break
        else:
            if '..' in ls[i]:
                pos = ls[i].index('..')
                if ls[i - 1][pos] == '.' or ls[i - 1][pos + 1] == '.':
                    print('YES')
                    break
    else:
        if '..' in ls[i]:
            pos = ls[i].index('..')
            if ls[i-1][pos] == '.' or ls[i-1][pos+1] == '.':
                print('YES')
                break
            elif ls[i+1][pos] == '.' or ls[i+1][pos+1] == '.':
                print('YES')
                break
else:
    print('NO')