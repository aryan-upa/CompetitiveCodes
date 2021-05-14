# Round 194, Div 2, Problem A
# https://codeforces.com/contest/334/problem/A

inp = int(input())
ls = [i for i in range(1,inp*inp+1)]
for i in range(0,int((inp*inp)/2),int(inp/2)):
    for j in range(int(inp/2)):
        print(ls[j+i],ls[inp*inp-j-1-i],end=' ')
    print()
