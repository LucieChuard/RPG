import random
import personnage
import ennemi 
import loot

a=personnage.joueur(input("Nom du personnage : "),50,10,5,0,1)    
def fct():
    1==1

#Fct pour lvl up
def lvl():
    xp_necessaire=10
    if a.xp >= xp_necessaire :
        a.niveau+=1
        print (a.name + " gagne un niveau et est maintenant niveau " + str(a.niveau))
        xp_necessaire=round(xp_necessaire*1.8)
        print ("Il faudra maintenant " +str(xp_necessaire)+" points d'expérience pour passer un nouveau niveau!")

#ennemi aléatoire
mobid=random.randint(0,len(ennemi.typeennemi)-1) 
#récupp les stats du mob selon page ennemi
mobcbt=personnage.ennemi(ennemi.typeennemi[mobid][0],int(ennemi.typeennemi[mobid][1]),int(ennemi.typeennemi[mobid][2]),int(ennemi.typeennemi[mobid][3]), int(ennemi.typeennemi[mobid][4])) 
print ("L'ennemi aura "+str(mobcbt.pv)+"pv.")

while fct  :
      
    #Tour joueur#
        #dégats infligés entre 1 et attaque max du perso
    x=random.randint(1,a.attaque) 
    print ("Dégats infligés par " +a.name+ ": "+str(x))
    atkinfl=x-mobcbt.defense 
    if atkinfl > 0 :
        mobcbt.pv=mobcbt.pv-atkinfl 
        print(mobcbt.name+" reçoit " + str(atkinfl) +" dégats.")
    print ("Il reste à l'ennemi "+str(mobcbt.pv)+" pv")

    if mobcbt.pv <=0 :
        print (mobcbt.name +" est mort, vous avez gagné!")
        print("Vous gagnez "+ str(mobcbt.xp)+ " points d'expérience!")
        a.xp=a.xp+mobcbt.xp
        print ("Vous avez un total de "+str(a.xp) +" points d'expérience!")
        lvl()
        loot.fctloot()
        break
    else :
    
    #tour mob
         #dégats infligés par le mob
        atkmob=random.randint(1,mobcbt.attaque) 
        print (str(mobcbt.name)+ " inflige "+ str(atkmob))

         #prise en compte défense du joueur
        atkrecu=atkmob-a.defense 
        if atkrecu > 0 :
            a.pv=a.pv-atkrecu 
            print(a.name+" reçoit " + str(atkrecu) +" dégats.")
    #PV du perso restant       
        print (str(a.name) + " a encore "+ str(a.pv))  
        if a.pv <=0 :
            print ("Vous êtes mort! Game Over!") 
            break
        
    