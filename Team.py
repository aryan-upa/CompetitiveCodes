# Round 143, Div 2, Problem A
# https://codeforces.com/contest/231/problem/A

inp, _ = int(input()), 0
while inp > 0:
    s = input()
    if s.count('1') > 1:
        _ += 1
    inp -= 1
print(_)