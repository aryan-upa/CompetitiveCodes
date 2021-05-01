# 10242 - Fourth Point!!
# https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1183

Ans = list()
while True:
    try:
        ls = list(map(float,input().split()))
        if ls[0]==ls[4] and ls[1]==ls[5]:
            # [ABAC]
            a, b, c = [ls[2],ls[3]],[ls[0],ls[1]],[ls[6],ls[7]]
        elif ls[0]==ls[6] and ls[1]==ls[7]:
            # [ABCA]
            a, b, c = [ls[2],ls[3]],[ls[0],ls[1]],[ls[4],ls[5]]
        elif ls[2]==ls[4] and ls[3]==ls[5]:
            # [BAAC]
            a, b, c = [ls[0],ls[1]],[ls[2],ls[3]],[ls[6],ls[7]]
        else:
            # [BACA]
            a, b, c = [ls[0],ls[1]],[ls[2],ls[3]],[ls[4],ls[5]]

        p = a[0]+c[0]-b[0]
        q = a[1]+c[1]-b[1]
        ls = [format(p,'.3f'),format(q,'.3f')]
        Ans.append(ls)
    except IndexError:
        for ls in Ans:
            print(*ls)
        break
