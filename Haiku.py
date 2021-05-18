# Beta Round 70, Div 2, Problem A
# https://codeforces.com/contest/78/problem/A

inp1 = input()
inp2 = input()
inp3 = input()
val1 = inp1.count('a')+inp1.count('e')+inp1.count('i')+inp1.count('o')+inp1.count('u')
val2 = inp2.count('a')+inp2.count('e')+inp2.count('i')+inp2.count('o')+inp2.count('u')
val3 = inp3.count('a')+inp3.count('e')+inp3.count('i')+inp3.count('o')+inp3.count('u')
if val1==5 and val2==7 and val3==5:
    print('YES')
else:
    print('NO')