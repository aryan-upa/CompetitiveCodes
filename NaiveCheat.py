# Round 383, Div 2, Problem A
# https://codeforces.com/contest/742/problem/A

inp = int(input())
if inp == 0 or inp == 10:
    if inp == 0:
        print(1)
    else:
        print(4)
else:
    rem = int(inp/10) % 2
    inp %= 10
    if inp in [2, 4, 6, 8]:
        if inp == 2 or inp == 6:
            if rem == 1:
                print(6)
            else:
                print(4)
        else:
            if rem == 1:
                print(4)
            else:
                print(6)
    elif inp in [1, 3, 5, 7, 9]:
        if inp in [3, 7]:
            if rem == 1:
                print(8)
            else:
                print(2)
        else:
            if rem == 1:
                print(2)
            else:
                print(8)
    else:
        print(6)