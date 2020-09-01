import random

global polje
global polje_prikaz
global stolpci
global vrstice
global zastava
global st_min
global mine
global kuza
global barva

kuza = 400

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
    global zastava
    global st_min
    global mine
    global barva

    zastava = False
    barva = "#231F20"

    stolpci = s
    vrstice = v
    polje = [[0] * stolpci for i in range(vrstice)]
    polje_prikaz = [[-2] * stolpci for i in range(vrstice)]

    st_min = s * v // 10
    mine = s * v // 10
    postavi_mino(st_min)
    prestej_okoli_min()

def odkri_polje(v, s):
    global stolpci
    global vrstice
    global polje
    global polje_prikaz
    global zastava

    if zastava == True:
        if not polje_prikaz[v][s] == -3:
            polje_prikaz[v][s] = -3
            odstrani_mino()
        else:
            polje_prikaz[v][s] = -2
            dodaj_mino()
        return

    if polje_prikaz[v][s] == polje[v][s]:
        return

    if polje_prikaz[v][s] == -3:
        dodaj_mino()

    polje_prikaz[v][s] = polje[v][s]
    p = polje_prikaz[v][s]

    if p == 0:
        if 0 < v:
            if not polje_prikaz[v - 1][s] == -3:
                odkri_polje(v - 1, s)
        if v < vrstice - 1:
            if not polje_prikaz[v + 1][s] == -3:
                odkri_polje(v + 1, s)
        if 0 < s:
            if not polje_prikaz[v][s - 1] == -3:
                odkri_polje(v, s - 1)
        if s < stolpci - 1:
            if not polje_prikaz[v][s + 1] == -3:
                odkri_polje(v, s + 1)
        if 0 < v and 0 < s:
            if not polje_prikaz[v - 1][s - 1] == -3:
                odkri_polje(v - 1, s - 1)
        if 0 < v and s < stolpci - 1:
            if not polje_prikaz[v - 1][s + 1] == -3:
                odkri_polje(v - 1, s + 1)
        if v < vrstice - 1 and 0 < s:
            if not polje_prikaz[v + 1][s - 1] == -3:
                odkri_polje(v + 1, s - 1)
        if v < vrstice - 1 and s < stolpci - 1:
            if not polje_prikaz[v + 1][s + 1] == -3:
                odkri_polje(v + 1, s + 1)

def toggle_zastava():
    global zastava
    global barva

    if zastava == True:
        barva = '#231F20'
        zastava = not zastava
    else:
        barva = '#FF0000'
        zastava = not zastava

def odstrani_mino():
    global st_min
    
    if st_min == 0:
        return
    else:
        st_min -= 1

def dodaj_mino():
    global st_min

    st_min += 1

def preveri_izid():
    global mine
    global polje_prikaz
    global vrstice
    global stolpci

    prestej_mine = 0

    for i in range(vrstice):
        for j in range(stolpci):
            if polje_prikaz[i][j] == -1:
                return 'p'
            if polje_prikaz[i][j] == -3 or polje_prikaz[i][j] == -2:
                prestej_mine += 1
    if prestej_mine == mine:
        return 'z'
    else:
        return 'i'

def dodaj_zalost():
    global kuza

    kuza += 100

def poenostavi_zalost():
    global kuza

    kuza = 100
