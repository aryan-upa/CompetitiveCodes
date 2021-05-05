# Round 369, Div 2, Problem A
# https://codeforces.com/contest/711/problem/A

inp = int(input())
ls, flag = [],0
while inp>0:
    p1,p2 = input().split('|')
    if p1=='OO' and flag==0:
        p1='++'
        flag=1
    elif p2=='OO' and flag==0:
        p2='++'
        flag=1
    else:
        pass
    ls.append(f'{p1}|{p2}')
    inp-=1
else:
    if flag!=1:
        print('NO')
    else:
        print('YES')
        print(*ls,sep='\n')
