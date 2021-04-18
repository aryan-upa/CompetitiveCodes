# UVA 11231 Black and White Painting
# https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2172

while True:
    n, m, c = list(map(int, input().strip().split()))
    if n == m == c == 0:
        break

    sol = (n - 7) * (m - 7) // 2
    if n % 2 == 0 and m % 2 == 0 and c == 1:
        sol += 1
    print("{}".format(sol))
