# VK CUP 2017, Problem A
# https://codeforces.com/contest/791/problem/A

a, b = map(int, input().split())
i = 0
while a <= b: a, b, i = a*3, b*2, i+1
print(i)