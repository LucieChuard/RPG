class personnage :
    class_name = ""
    descr = ""
    def __init__ (self, name,pv,attaque,defense, xp) :
        name=name
        pv=pv
        attaque = attaque
        defense = defense
        xp=xp

class joueur (personnage):
    def __init__(self, name,pv,attaque,defense, xp, niveau):
        joueur.name= name
        joueur.pv=pv
        joueur.attaque=attaque
        joueur.defense=defense 
        joueur.xp= xp
        joueur.niveau=niveau

class ennemi (personnage) :
    def __init__(self, name,pv,attaque,defense, xp):
        ennemi.name = name
        ennemi.pv = pv
        ennemi.attaque = attaque 
        ennemi.defense = defense
        ennemi.xp=xp