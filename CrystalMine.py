# Round 259, Div 2, Problem A
# https://codeforces.com/contest/454/problem/A

inp = int(input())
c = 0
Mat = ['' for q in range(inp)]
for i in range(1,inp+1):
    if i<inp/2:
        Mat[i-1] = '*'*int(((inp-(2*i-1))/2))+'D'*(2*i-1)+'*'*int(((inp-(2*i-1))/2))
    elif i==int((inp+1)/2):
        Mat[i-1] = 'D'*inp
    else:
        Mat[i-1] = Mat[inp-i]
print(*Mat,sep='\n')