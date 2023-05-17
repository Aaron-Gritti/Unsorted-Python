from Classes import*
from tkinter import*
from tkinter import messagebox
from random import*
import webbrowser #

liste = []
listeEpees = []
listeObjets = []
coffreCache = False
coffreDecache = False
listeGuerriers = []
persoChoisi = ""
armeValider = False
objetValider = False
inventaireShowing = ""
found = False
yes = False
etape = 1
notSoFriendly = False
compteurDead = 0

def ahBahSuper():
    global yes
    if yes == True:
        LaGuerreDeOuiOui.attributes('-alpha',1)
        yes = False
    else:
        LaGuerreDeOuiOui.attributes('-alpha',0.5)
        yes = True

def histoire():
    global liste
    file = open("histoire.txt", "r")
    liste = file.readlines()
    file.close()
histoire()

def quitter():
    messagebox.showinfo("Peureux","Ce n'est pas très courageux")
    LaGuerreDeOuiOui.destroy()

def showNormalInfos(event):
    textE=""
    textO=""
    for i in range(0,len(persoChoix1.getListeArme())):
        textE += str(persoChoix1.getListeArme()[i].getNomE())
        if persoChoix1.getArmeEnMain() != "":
            if str.lower(persoChoix1.getArmeEnMain().getNomE()) == str.lower(persoChoix1.getListeArme()[i].getNomE()):
                textE +=" (équipé)"
        textE +="\n\n"
    for i in range(0,len(persoChoix1.getListeObjet())):
        textO += str(persoChoix1.getListeObjet()[i].getNomO())+"\n\n"
    if textE != "":
        labelInvArmes.config(text=textE)
    if textO != "":
        labelInvObjets.config(text=textO)

def showOtherInfos(event):
    textE=""
    textO=""
    for i in range(0,len(persoChoix1.getListeArme())):
        textE += str(persoChoix1.getListeArme()[i].getAtk())+" atk \n\n"
    for i in range(0,len(persoChoix1.getListeObjet())):
        textO += str(persoChoix1.getListeObjet()[i].getSoin())+" pv+ \n\n"
    if textE != "":
        labelInvArmes.config(text=textE)
    if textO != "":
        labelInvObjets.config(text=textO)

def validerInv():
    global armeValider, objetValider, found
    entryInvChoix = str.lower(entryInv.get())
    entryInv.delete(0, 'end')
    if armeValider == True:
        armeValider = False
        for i in range(0,len(persoChoix1.getListeArme())):
            if str.lower(entryInvChoix) == str.lower(persoChoix1.getListeArme()[i].getNomE()):
                found = True
                if str.lower(persoChoix1.getListeArme()[i].getNomE()) == str.lower(persoChoix1.getArmeEnMain().getNomE()):
                    if str.lower(persoChoix1.getArmeEnMain().getNomE()) == "poings":
                        messagebox.showinfo("Hein ?","Vous ne pouvez pas déséquiper vos poings")
                    else:
                        persoChoix1.choisirArme("poings")
                        messagebox.showinfo("Arme rangée","Votre arme a bien étée déséquipée")
                else:
                    persoChoix1.choisirArme(str.lower(persoChoix1.getListeArme()[i].getNomE()))
                    messagebox.showinfo("Arme équipée","Votre arme a bien étée équipée")
            if i+1 == len(persoChoix1.getListeArme()) and found == False:
                messagebox.showinfo("?","Cette arme est introuvable")
    if objetValider == True:
        objetValider = False
        for i in range(0,len(persoChoix1.getListeObjet())):
            if str.lower(entryInvChoix) == str.lower(persoChoix1.getListeObjet()[i].getNomO()):
                persoChoix1.used(persoChoix1.getListeObjet()[i])
                found = True
            if i+1 == len(persoChoix1.getListeObjet()) and found == False:
                messagebox.showinfo("?","Cet objet est introuvable")

    found = False
    entryInv.place_forget()
    boutonInvValider.place_forget()
    boutonInventaire.config(state=NORMAL)
    boutonInvActionArme.config(state=NORMAL)
    boutonInvActionObjet.config(state=NORMAL)
    inventaireSetup()
    labelAnnonce.config(text=str(persoChoix1))

def inventaireChoixA():
    global armeValider
    boutonInventaire.config(state=DISABLED)
    boutonInvActionArme.config(state=DISABLED)
    boutonInvActionObjet.config(state=DISABLED)
    entryInv.place(x=700,y=500)
    boutonInvValider.place(x=740,y=525)
    armeValider = True

def inventaireChoixO():
    global objetValider
    if persoChoix1.getListeObjet() == []:
        messagebox.showinfo("?","Vous n'avez aucun objet")
        return None
    boutonInventaire.config(state=DISABLED)
    boutonInvActionArme.config(state=DISABLED)
    boutonInvActionObjet.config(state=DISABLED)
    entryInv.place(x=700,y=500)
    boutonInvValider.place(x=740,y=525)
    objetValider = True


def inventaireSetup():
    textE = ""
    textO = ""
    for i in range(0,len(persoChoix1.getListeArme())):
        textE += str(persoChoix1.getListeArme()[i].getNomE())
        if persoChoix1.getArmeEnMain() != "":
            if str.lower(persoChoix1.getArmeEnMain().getNomE()) == str.lower(persoChoix1.getListeArme()[i].getNomE()):
                textE +=" (équipé)"
        textE +="\n\n"
    if persoChoix1.getListeObjet() == []:
            labelInvObjets.config(text="-vide-")
    else:
        for i in range(0,len(persoChoix1.getListeObjet())):
            textO += str(persoChoix1.getListeObjet()[i].getNomO())+"\n\n"
    if textE != "":
        labelInvArmes.config(text=textE)
    if textO != "":
        labelInvObjets.config(text=textO)

def inventaireShow():
    global inventaireShowing
    if inventaireShowing == True:
        boutonInventaire.config(bg="green", activebackground="lightgreen")
        labelInvInfos.place_forget()
        labelInvArme.place_forget()
        labelInvArmes.place_forget()
        labelInvObjet.place_forget()
        labelInvObjets.place_forget()
        boutonInvActionArme.place_forget()
        boutonInvActionObjet.place_forget()
        inventaireShowing = False
    else:
        inventaireSetup()
        boutonInventaire.config(bg="lightgreen", activebackground="green")
        labelInvInfos.place(x=800,y=193)
        labelInvArme.place(x=665,y=250)
        labelInvArmes.place(x=665,y=290)
        labelInvObjet.place(x=800,y=250)
        labelInvObjets.place(x=800,y=290)
        boutonInvActionArme.place(x=640,y=450)
        boutonInvActionObjet.place(x=780,y=450)
        inventaireShowing = True

def riposteEnnemi():
    if mechant.getVie() == 0:
        messagebox.showinfo("Incroyable !","L'ennemi a été terrassé par votre puissance !")
    else:
        persoChoix1.attacked(mechant)
        if persoChoix1.getVie() == 0:
            messagebox.showinfo("Défaite","L'ennemi vous a tué, dommage!")
        else:
            messagebox.showinfo("Ouch","L'ennemi vous attaque, il ne vous reste que "+str(persoChoix1.getVie())+" points de vie.")
            valider()

def persoChoix():
    global persoChoix1
    entryPerso = str.lower(entrySaisie.get())
    entrySaisie.delete(0, 'end')
    for i in range(0,len(listeGuerriers)):
        if entryPerso == str.lower(listeGuerriers[i].getNomG()):
            if listeGuerriers[i].getVie() == 0:
                messagebox.showinfo("...",str(listeGuerriers[i].getNomG())+" a déjà été défait par l'ennemi !")
                return None
            persoChoix1 = listeGuerriers[i]
            persoChoix1.ajouterArme(poings)
            persoChoix1.choisirArme("poings")
            labelAnnonce.config(text=str(persoChoix1))
            labelAnnonceEnnemi.config(text=str(mechant))
            labelChoix.config(text=liste[1])
            if coffreCache == True:
                labelChoix.config(text=liste[4])
            messagebox.showinfo("Nice","Vous avez choisi "+str(persoChoix1.getNomG()))
            boutonInventaire.config(state=NORMAL)
            boutonInventaire.place(x=710,y=200)
            boutonValider.config(command=valider)

def valider():
    global etape, noSoFriendly, compteurDead, coffreCache, coffreDecache
    entryPerso = str.lower(entrySaisie.get())
    entrySaisie.delete(0, 'end')

    if etape == 1  and coffreCache == False:
        if entryPerso == "a" or entryPerso == "ouvrir":
            etape += 1
            chestPosNeg = randrange(0,2)
            if chestPosNeg == 0 :
                randomPositive = randrange(0,2)
                if randomPositive == 0:
                    messagebox.showinfo("Nice","Vous avez trouvé une banane dans le coffre")
                    persoChoix1.ajouterObjet(banane)
                else:
                    randomWeapon = randrange(0,3)
                    persoChoix1.ajouterArme(listeEpees[randomWeapon])
                    which = listeEpees.pop(randomWeapon)
                    messagebox.showinfo("Nice","Vous avez ouvert le coffre et avez récupéré : "+str(which))
            else:
                randomNegative = randrange(0,2)
                if randomNegative == 0 :
                    messagebox.showinfo("Ouch","Le coffre était piégé ! Vous perdez 15 points de vie !")
                    persoChoix1.setVie(persoChoix1.getVie()-15)
                    if persoChoix1.getVie() == 0:
                        messagebox.showinfo("mdr","Vous êtes mort par un coffre, UN COFFRE!")
                        LaGuerreDeOuiOui.destroy()
                        return None
                if randomNegative == 1 :
                    messagebox.showinfo("Aïe !","Vous vous faites mal en essayant d'ouvrir le coffre, vous perdez 1 point de vie mais vous pouvez retenter votre chance")
                    persoChoix1.setVie(persoChoix1.getVie()-1)
                    etape-=1
                    if coffreDecache == True:
                        labelChoix.config(text=liste[5])
                        inventaireSetup()
                        labelAnnonce.config(text=str(persoChoix1))
                        labelAnnonceEnnemi.config(text=str(mechant))
                        return None
                    if persoChoix1.getVie() == 0:
                        messagebox.showinfo("mdr","Vous êtes mort par un coffre, UN COFFRE!")
                        LaGuerreDeOuiOui.destroy()
                        return None
        if entryPerso == "b" or entryPerso == "laisser" :
            etape += 1
            messagebox.showinfo("Sûreté","Vous n'ouvrez pas le coffre, vous vous demandez si c'est une bonne idée en vous éloignant.")

        if entryPerso == "c" or entryPerso == "cacher" :
            etape += 1
            coffreCache = True
            messagebox.showinfo("Précautionneux","Vous avez caché le coffre dans un buisson, si c'est un piège, personne ne tombera dedans.")
        coffreDecache = False
        if etape == 2:
            labelAnnonceEnnemi.place(x=400,y=160)

    elif etape == 1 and coffreCache == True:
        if entryPerso == "a" or entryPerso == "regarder":
            coffreCache = False
            coffreDecache = True
            labelChoix.config(text=liste[5])
            inventaireSetup()
            labelAnnonce.config(text=str(persoChoix1))
            labelAnnonceEnnemi.config(text=str(mechant))
            if etape == 2:
                labelAnnonceEnnemi.place(x=400,y=160)
            return None
        if entryPerso == "b" or entryPerso == "peureux":
            messagebox.showinfo("Sûreté","Vous ne regardez pas dans les buissons, il faut faire attention dans cette forêt.")
        if etape == 2:
            labelAnnonceEnnemi.place(x=400,y=160)

    elif etape == 2:
        if entryPerso == "a":
            friendlyMechant = randrange(0,5)
            if friendlyMechant == 1 and notSoFriendly == False:
                messagebox.showinfo("Surprise","Avec vos talents d'orateur, vous avez convaincu le méchant de prendre une bière avec vous")
                persoChoix1.ajouterObjet(bière)
                messagebox.showinfo("...","Vous avez récupéré une bière")
                messagebox.showinfo("...","Bourré, le méchant vous frappe, vous allez devoir vous battre !")
                notSoFriendly = True
            elif friendlyMechant == 1 and notSoFriendly == True:
                messagebox.showinfo("...","Vous tentez de parler au méchant mais il est trop occupé à essayer de vous frapper")
            elif friendlyMechant != 1:
                persoChoix1.setVie(0)
                messagebox.showinfo("Arf","On ne parle pas avec un méchant : "+str(persoChoix1))
        if entryPerso == "b":
            patateDenfer = randrange(0,10)
            if patateDenfer == 0 and persoChoix1.getArmeEnMain() == poings:
                messagebox.showinfo("Ouah !","Une soudaine force vous envahit et vous foncez sur l'ennemi le défonçant avec vos poings")
                mechant.setVie(0)
            elif len(persoChoix1.getListeArme()) != 1:
                messagebox.showinfo("Bien joué","Vous attaquez "+str(mechant.getNomG())+" avec "+str(persoChoix1.getArmeEnMain().getNomE())+" infligeant "+str(mechant.attacked(persoChoix1))+" dégats")
            else:
                mechant.attacked(persoChoix1)
                messagebox.showinfo("Arf","Vous n'avez pas d'arme! Vous vous lancez avec vos poings et infligez 1 point de dégat à votre adversaire ("+str(mechant.getNomG())+")")
            riposteEnnemi()
        if entryPerso == "c":
            pierreMort = randrange(0,2)
            if pierreMort == 1:
                messagebox.showinfo("Arf","Le guerrier :"+mechant.getNomG()+" vous lance une pierre dans la tête et vous mourrez")
            else:
                messagebox.showinfo("Arf","Le guerrier :"+mechant.getNomG()+" vous lance une pierre mais rate, vous trébuchez dessus et mourrez à votre chute")
            persoChoix1.setVie(0)

    elif etape == 3:
        if entryPerso == "oui":
            for i in range(0,len(listeGuerriers)):
                if listeGuerriers[i].getVie() == 0:
                    compteurDead += 1
                    if compteurDead == 4:
                        messagebox.showinfo("Fin","Il ne vous reste aucun guerrier pour vaincre le méchant, vous perdez la partie !")
                        LaGuerreDeOuiOui.destroy()
                        return None
            labelChoix.config(text=liste[0][3:])
            etape = 1
            boutonValider.config(command=persoChoix)
            return None
        if entryPerso == "non":
            messagebox.showinfo("Fin","Merci d'avoir joué !")
            LaGuerreDeOuiOui.destroy()
            return None

    if mechant.getVie() == 0:
        messagebox.showinfo("Fin","Merci d'avoir joué !")
        LaGuerreDeOuiOui.destroy()
        return None
    if persoChoix1.getVie() == 0:
        if inventaireShowing == True:
            inventaireShow()
        boutonInventaire.config(state=DISABLED)
        etape = 3
    labelChoix.config(text=liste[etape])
    inventaireSetup()
    labelAnnonce.config(text=str(persoChoix1))
    labelAnnonceEnnemi.config(text=str(mechant))

excalibur = Epee("Excalibur",20)
durandal = Epee("Durandal",15)
aiguille = Epee("Aiguille",3)
canif = Epee("Canif",2)
poings = Epee("Poings",1)

listeEpees.append(excalibur)
listeEpees.append(durandal)
listeEpees.append(aiguille)
listeEpees.append(canif)
listeEpees.append(poings)

ouioui = Guerrier("Oui-Oui",20)
lannister = Guerrier("Lannister",30)
conan = Guerrier("Conan",25)
mechant = Guerrier("méchant",175)

mechant.ajouterArme(aiguille)
mechant.choisirArme("aiguille")

listeGuerriers.append(ouioui)
listeGuerriers.append(lannister)
listeGuerriers.append(conan)
listeGuerriers.append(mechant)

bière = Objet("Bière",20)
banane = Objet("Banane",10)

listeObjets.append(bière)
listeObjets.append(banane)

LaGuerreDeOuiOui = Tk()
LaGuerreDeOuiOui .title("La Guerre De Oui-Oui")
LaGuerreDeOuiOui .geometry("1000x600")
LaGuerreDeOuiOui.config(bg="lightgrey")

labelChoix = Label(LaGuerreDeOuiOui, text=liste[0][3:], bg="grey", fg="white")
labelChoix.place(x=20,y=20)

labelSaisir = Label(LaGuerreDeOuiOui, text="Saisir votre choix",bg="grey",fg="white")
labelSaisir.place(x=20,y=60)

labelAnnonce = Label(LaGuerreDeOuiOui, text="Pas de personnage",bg="grey",fg="white")
labelAnnonce.place(x=400,y=120)

labelAnnonceEnnemi = Label(LaGuerreDeOuiOui, text=str(mechant),bg="grey",fg="white")

entrySaisie = Entry(LaGuerreDeOuiOui)
entrySaisie.place(x=200,y=120)

boutonValider = Button(LaGuerreDeOuiOui, text="Valider", bg="lightgreen", activebackground="green", command=persoChoix)
boutonValider.place(x=20,y=150)

boutonInventaire = Button(LaGuerreDeOuiOui, text="Voir l'inventaire", bg="green", activebackground="lightgreen", command=inventaireShow)
labelInvInfos = Label(LaGuerreDeOuiOui, text="?", bg="lightgreen")
labelInvArme = Label(LaGuerreDeOuiOui, text="Armes", bg="lightgrey")
labelInvArmes = Label(LaGuerreDeOuiOui, text="-vide-", bg="lightgrey") # Ici on a toujours les poings donc on verra jamais ce "-vide-" là
labelInvObjet = Label(LaGuerreDeOuiOui, text="Objets", bg="lightgrey")
labelInvObjets = Label(LaGuerreDeOuiOui, text="-vide-", bg="lightgrey")
boutonInvActionArme = Button(LaGuerreDeOuiOui,  text="Equiper une arme?", command=inventaireChoixA)
boutonInvActionObjet = Button(LaGuerreDeOuiOui,  text="Utiliser un objet?", command=inventaireChoixO)
entryInv = Entry(LaGuerreDeOuiOui)
boutonInvValider = Button(LaGuerreDeOuiOui, text="Valider", bg="lightgreen", activebackground="green", command=validerInv)

boutonQuitter = Button(LaGuerreDeOuiOui, text="Quitter", bg="orange", activebackground="red", command=quitter)
boutonQuitter.place(x=20,y=500)

boutonMalin = Button(LaGuerreDeOuiOui, text="", command=ahBahSuper)
boutonMalin.place(x=0,y=-10)

labelInvInfos.bind('<Enter>', showOtherInfos) # Quand on entre dans le "?", l'attaque des armes et la vie que redonne les objets s'affiche
labelInvInfos.bind('<Leave>', showNormalInfos) # Quand on sort on repasse à l'affichage des noms

LaGuerreDeOuiOui.mainloop()