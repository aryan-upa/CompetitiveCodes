# UVA 10110 Light, more light!
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1051

import math


def persq(x):
    sq = math.sqrt(x)
    return 1 if sq - math.floor(sq) == 0 else 0


ls = [1]
for i in ls:
    inp = int(input())
    if inp != 0:
        ls.append(inp)
    else:
        break
ls.remove(1)

for i in ls:
    if persq(i):
        print("yes")
    else:
        print("no")
