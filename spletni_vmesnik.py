import bottle

import model

@bottle.get("/")
def glavna_stran():
    return bottle.template("glavna_stran.html")

@bottle.post("/")
def glavna_stran_post():
    Vrstice = bottle.request.forms.get("vrstice", type = int)
    Stolpci = bottle.request.forms.get("stolpci", type = int)
    model.zacni_igro(Vrstice, Stolpci)
    model.poenostavi_zalost()
    bottle.redirect("/igra")

@bottle.get("/Slike/<slika>")
def vrni_sliko(slika):
    return bottle.static_file(slika, root="./Slike")


@bottle.get("/igra")
def igra():
    return bottle.template("Igra.tpl", Stolpec = model.stolpci, Vrstica = model.vrstice, Polje = model.polje_prikaz, Mine = model.st_min)

@bottle.post("/igra")
def igra_post():
    v = bottle.request.forms.get("vrstica", type = int)
    s = bottle.request.forms.get("stolpec", type = int)
    if v == None:
        model.toggle_zastava()
    else:
        model.odkri_polje(v, s)
    rezultat = model.preveri_izid()
    if rezultat == 'p':
        bottle.redirect("/poraz")
    if rezultat == 'z':
        bottle.redirect("/zmaga")
    if rezultat == 'i':
        return bottle.template("Igra.tpl", Stolpec = model.stolpci, Vrstica = model.vrstice, Polje = model.polje_prikaz, Mine = model.st_min)

@bottle.get("/zmaga")
def zmaga_stran():
    return bottle.template("zmaga.html")

@bottle.post("/zmaga")
def zmaga_post():
    if bottle.request.forms.get("igraj") == 'znova':
        bottle.redirect("/")
    elif bottle.request.forms.get("igraj") == 'ne':
        bottle.redirect("/kaj")

@bottle.get("/poraz")
def poraz_stran():
    return bottle.template("poraz.html")

@bottle.post("/poraz")
def zmaga_post():
    if bottle.request.forms.get("igraj") == 'znova':
        bottle.redirect("/")
    elif bottle.request.forms.get("igraj") == 'ne':
        bottle.redirect("/kaj")

@bottle.get("/kaj")
def kaj_stran():
    return bottle.template("kaj.html", Kuza = model.kuza)

@bottle.post("/kaj")
def zmaga_post():
    if bottle.request.forms.get("igraj") == 'znova':
        bottle.redirect("/")
    elif bottle.request.forms.get("igraj") == 'ne':
        model.dodaj_zalost()
        bottle.redirect("/kaj")

bottle.run(debug=True, reloader=True)