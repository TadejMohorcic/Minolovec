import bottle

import model

@bottle.get("/")
def GlavnaStran():
    return bottle.template("glavna_stran.html")

@bottle.post("/")
def GlavnaStranPost():
    Vrstice = bottle.request.forms.get("vrstice", type = int)
    Stolpci = bottle.request.forms.get("stolpci", type = int)
    model.zacni_igro(Vrstice, Stolpci)
    bottle.redirect("/igra")

@bottle.get("/igra")
def Igra():
    return bottle.template("Igra.tpl", Stolpec = model.stolpci, Vrstica = model.vrstice, Polje = model.polje_prikaz, Mine = model.st_min)

@bottle.post("/igra")
def IgraPost():
    v = bottle.request.forms.get("vrstica", type = int)
    s = bottle.request.forms.get("stolpec", type = int)
    if v == None:
        model.toggle_zastava()
    else:
        model.odkri_polje(v, s)
    return bottle.template("Igra.tpl", Stolpec = model.stolpci, Vrstica = model.vrstice, Polje = model.polje_prikaz, Mine = model.st_min)


bottle.run(debug=True, reloader=True)