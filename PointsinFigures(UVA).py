# UVA 476 - Points in Figures: Rectangles
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=417

Rec, Poi = [], []
while True:
    s = input()
    if s!= '*':
        rec = list(map(float,s[2:].split()))
        Rec.append(rec)
    else:
        break
while True:
    poi = list(map(float, input().split()))
    if poi!=[9999.9, 9999.9]:
        Poi.append(poi)
    else:
        break
for i in range(len(Poi)):
    val = Poi[i]
    flag=0
    for q in range(len(Rec)):
        x1, y1, x2, y2 = Rec[q][0],Rec[q][1],Rec[q][2],Rec[q][3]
        if x1<val[0]<x2:
            if y2<val[1]<y1:
                print(f'Point {i+1} is contained in figure {q+1}')
                flag=1
    else:
        if flag!=1:
            print(f'Point {i+1} is not contained in any figure')
