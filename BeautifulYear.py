# Round 166, Div 2, Problem A
# https://codeforces.com/contest/271/problem/A

inp = int(input())+1
while True:
    st = str(inp)
    if st.count(st[0]) + st.count(st[1]) + st.count(st[2]) + st.count(st[3]) == 4:
        print(st)
        break
    else:
        inp+=1