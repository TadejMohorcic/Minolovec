import random

global polje
global polje_prikaz
global stolpci
global vrstice

def postavi_mino(m):
    global polje
    global stolpci
    global vrstice

    while m > 0:
        v = random.randint(0, vrstice - 1)
        s = random.randint(0, stolpci - 1)
        if not polje[v][s] == -1:
            polje[v][s] = -1
            m = m - 1

def prestej_okoli_min():
    global polje
    global stolpci
    global vrstice

    for i in range(vrstice):
        for j in range(stolpci):
            if polje[i][j] == -1:
                for a in [-1, 0, 1]:
                    for b in [-1, 0, 1]:
                        if (0 <= i+a < vrstice and 0 <= j+b < stolpci and polje[i+a][j+b] != -1):
                            polje[i+a][j+b] += 1


def zacni_igro(v, s):
    global stolpci
    global vrstice
    global polje
    global polje_prikaz

    stolpci = s
    vrstice = v
    polje = [[0] * stolpci for i in range(vrstice)]
    polje_prikaz = [[-2] * stolpci for i in range(vrstice)]

    st_min = s * v // 10
    postavi_mino(st_min)
    prestej_okoli_min()

def odkri_polje(v, s):
    global stolpci
    global vrstice
    global polje
    global polje_prikaz

    if polje_prikaz[v][s] == polje[v][s]:
        return

    polje_prikaz[v][s] = polje[v][s]
    p = polje_prikaz[v][s]

    if p == 0:
        if 0 < v:
            odkri_polje(v - 1, s)
        if v < vrstice - 1:
            odkri_polje(v + 1, s)
        if 0 < s:
            odkri_polje(v, s - 1)
        if s < stolpci - 1:
            odkri_polje(v, s + 1)
        if 0 < v and 0 < s:
            odkri_polje(v - 1, s - 1)
        if 0 < v and s < stolpci - 1:
            odkri_polje(v - 1, s + 1)
        if v < vrstice - 1 and 0 < s:
            odkri_polje(v + 1, s - 1)
        if v < vrstice - 1 and s < stolpci - 1:
            odkri_polje(v + 1, s + 1)
