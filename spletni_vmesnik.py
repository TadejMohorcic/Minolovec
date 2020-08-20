import bottle

x = 0
y = 0

@bottle.get("/")
def GlavnaStran():
    return bottle.template("glavna_stran.html")

@bottle.post("/")
def GlavnaStranPost():
    x = bottle.request.forms.get("x")
    y = bottle.request.forms.get("y")
    print(x)
    print(y)
    bottle.redirect("/igra")

@bottle.get("/igra")
def Igra():
    return str(x) + " " + str(y)


bottle.run()