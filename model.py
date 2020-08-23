import random

x = #se dobimo spremeljivke
y = #se dobimo spremeljivke

Polje = [[0] * x for i in range(y)]

m = x * y // 5 #stevilo min

for n in range(0, m + 1):
    PostaviMino(c)


def PostaviMino(c):
    v = random.randint(0, y)
    s = random.randint(0, x)
    Vrsta = Polje[v]
    if not Vrsta[s] == "-1":
        Vrsta[s] == "-1"
    else:
        PostaviMino(c)

for i in range(Polje):
    for j in range(len(Polje[0])):
        if Polje[i][j] == "-1":
            for a in range(-1, 0, 1):
                for b in range(-1, 0, 1):
                    if (0 <= i+a <= y and 0 <= j+b <= x and Polje[i+a][j+b] != "-1"):
                        Polje[i+a][j+b] += 1







