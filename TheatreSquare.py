# Beta Round 1, Problem A
# https://codeforces.com/contest/1/problem/A

from math import ceil
n, m, a = map(int, input().split())
print(ceil(n/a)*ceil(m/a))