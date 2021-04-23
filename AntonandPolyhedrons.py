# Round 404, Div 2, Problem A
# https://codeforces.com/contest/785/problem/A

_ = 0
for i in range(int(input())):
    s = input()
    if s == 'Tetrahedron':
        _ += 4
    elif s == 'Cube':
        _ += 6
    elif s == 'Octahedron':
        _ += 8
    elif s == 'Dodecahedron':
        _ += 12
    else:
        _ += 20
print(_)