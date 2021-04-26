# Round 102, Div, Problem A
# https://codeforces.com/contest/143/problem/A

r1, r2 = map(int, input().split())
c1, c2 = map(int, input().split())
d1, d2 = map(int, input().split())
g1 = int((r1-c2+d1)/2)
g2 = int((r1-c1+d2)/2)
g3 = int((c1-r1+d2)/2)
g4 = int((c2-r1+d1)/2)
ls = [g1, g2, g3, g4]
if ls.count(g1) > 1 or ls.count(g2) > 1 or ls.count(g3) > 1 or ls.count(g4) > 1:
    print(-1)
elif g1 > 9 or g2 > 9 or g3 > 9 or g4 > 9:
    print(-1)
elif g1+g2 != r1 or g3+g4 != r2 or g1+g3 != c1 or g2+g4 != c2 or g1+g4 != d1 or g2+g3 != d2:
    print(-1)
elif g1 and g2 and g3 and g4:
    print('{0} {1}'.format(g1, g2))
    print('%d %d' % (g3, g4))
else:
    print(-1)
