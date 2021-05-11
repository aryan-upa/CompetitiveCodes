# Round 280, Div 2, Problem A
# https://codeforces.com/contest/492/problem/A

inp,j = int(input()),0
while inp>0:
    j+=1
    inp -= j*(j+1)/2
    if inp<0: j-=1
print(j)
