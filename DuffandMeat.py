# Round 326, Div 2, Problem A
# https://codeforces.com/contest/588/problem/A

n = int(input())
if n!=1:
    a = []; p = []
    for i in range(n):
        ai, pi = map(int,input().split())
        a.append(ai); p.append(pi)
    _=0; pri = p[0]; quan = a[0]
    for q in range(1,n):
        if p[q]>pri:
            quan+=a[q]
            if q==n-1:
                _+=pri*quan
        else:
            _+=pri*quan
            pri=p[q]; quan=a[q]
            if q==n-1:
                _+=pri*quan
    else:
        print(_)
else:
    a,b = map(int,input().split())
    print(a*b)