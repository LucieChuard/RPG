import random

# liste des items
loot=["lampe" , "allumettes", "nourriture" , "pistolet 10mm", "pistolet .44", "carabine de combat", "fusil de chasse", "fusil de fortune", "fusil à double canon", "fusil de combat", "mitraillette", "lance flamme", "lance missiles", "pistolet laser", "fusil laser", "mousquet laser", "pistolet plasma", "laser gatling", "fat man", "minigun","fusil plasma", "fusil d'assaut","batte de baseball en bois", "batte de baseball en metal", "canne", "cle a molette", "demonte pneu", "masse", "matraque", "planche en bois", "queue de billard", "rouleau a patisserie", "tuyau en plomb", "couteau de combat", "katana", "epee de la guerre d'independance (rouillee)", "hache", "machette", "poing americain", "gant de boxe"]
amelioration_tap=["cloute", "renforce", "aucune amelioration"]
amelioration_visée=["grand chargeur", "canon scie", "compensateur" , "crosse"]
deterioration_tap=["cassé", "pourri ou rouille", "aucune deterioration"]
deterioration_visée=["rouillé", "déformé"]

#liste par catégorie (contondant, visée, arme de poing...)
tap= "batte de baseball en bois" , "batte de baseball en fer" , "planche en bois", "queue de billard" , "canne", "tuyau en plomb", "cle a molette", "baton de bois"
visee= "pistolet 10mm", "pistolet .44", "carabine de combat","fusil de chasse", "fusil de fortune", "fusil à double canon", "fusil de combat", "mitraillette", "lance flamme", "lance missiles", "pistolet laser", "fusil laser", "mousquet laser", "pistolet plasma", "laser gatling", "fat man", "minigun","fusil plasma", "fusil d'assaut"
stuff = "lampe","allumettes", "nourriture"

#Création fonction loot
def fctloot():


#Connaitre le nombre d'item looté, en fonction d'un maximum donné par le MJ#
    nb_loot=random.randint(0, 3)

    if nb_loot==0 :
        print ("Aucun item n'est tombé.")
    else :
        print ("Des items viennent de tomber: " + str(nb_loot))

#loot
    b=0

    while b < nb_loot:
        x=random.choice (loot)
        b=b+1
        print(" -------------------------------- ")
        print (x)

        if x in tap :
            a=random.choice (amelioration_tap)
            c=random.choice (deterioration_tap)
            print ("amélioration : "+a)
            print ("détérioration:" +c)
        elif x in visee :
            a=random.choice (amelioration_visée)
            c=random.choice(deterioration_visée)
            print ("amélioration : "+a)
            print ("déterioration : "+c)
        elif x in stuff:
            a=random.randint(1,10)
            print(a)
        else:
            print ("aucune amélioration n'est sur l'arme")
        loot.remove(x)

    