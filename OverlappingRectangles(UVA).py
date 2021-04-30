# UVA 460 - Overlapping Rectangles
# https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=401

# -- Personal Input--
# Before seeing the solution, I want you to think of all possible cases that overlapping rectangles can have
# (there are 13) because only after that you'll be able to understand, why code is long and has so many ifs and else.
# Secondly, making the output exactly by format is very crucial in UVA submissions.

inp = int(input())
Rec = []
for i in range(inp):
    s = input()
    ls1 = list(map(int,input().split()))
    ls2 = list(map(int,input().split()))
    ls = [ls1,ls2]
    Rec.append(ls)
_=len(Rec)-1
for a in Rec:
    ML = min(a[0][0],a[1][0])
    if ML == a[0][0]:
        r1, r2 = a[0], a[1]
    else:
        r1, r2 = a[1], a[0]
    r1llx,r1lly,r1urx,r1ury = map(int,r1)
    r2llx,r2lly,r2urx,r2ury = map(int,r2)
    if not r1llx <= r2llx < r1urx:
        print('No Overlap')
    else:
        if r2lly>=r1ury:
            print('No Overlap')
        elif r2lly<r1lly:
            if r2ury<=r1lly:
                print('No Overlap')
            else:
                c = [r2llx,r1lly]
                if r2urx<r1urx:
                    c.append(r2urx)
                else:
                    c.append(r1urx)
                if r2ury>r1ury:
                    c.append(r1ury)
                else:
                    c.append(r2ury)
                print(*c)
        else:
            if r2urx>r1urx:
                c = [r2llx,r2lly,r1urx]
                if r2ury>r1ury:
                    c.append(r1ury)
                else:
                    c.append(r2ury)
                print(*c)
            else:
                c = [r2llx,r2lly,r2urx]
                if r2ury > r1ury:
                    c.append(r1ury)
                else:
                    c.append(r2ury)
                print(*c)
    if _>0:
        print()
        _-=1
