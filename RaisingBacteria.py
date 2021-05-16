# Round 320, Div 2, Problem A
# https://codeforces.com/contest/579/problem/A

inp = int(input())
c=0
while True:
    val=2
    while val<inp:
        val*=2
    if inp==0:
        break
    elif inp==1:
        c+=1
        break
    else:
        val/=2
        inp%=val
        c+=1
print(c)