# Beta Round 94, Div 2, Problem A
# https://codeforces.com/contest/129/problem/A

inp,_ = int(input()),0
ls = list(map(int, input().split()))
if sum(ls)%2==0:
    for i in ls:
        if i%2==0:
            _+=1
    else:
        print(_)
else:
    for i in ls:
        if i%2!=0:
            _+=1
    else:
        print(_)