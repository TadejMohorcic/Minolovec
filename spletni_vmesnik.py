import bottle

@bottle.get("/")
def GlavnaStran():
    return bottle.template("glavna_stran.html")

bottle.run()