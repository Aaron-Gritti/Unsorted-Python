#Mini projet par Gritti Aaron , Mary Flavien et Khiev Célia

#Imports
from tkinter import*
from tkinter import messagebox
from random import*
import threading

#Destroy global

def Destroyall():
    Jeu.destroy()
    Jeu2.destroy()
    JeuVictoire.destroy()

#Annonces trop grand/petit + 6eme Fenêtre : Victoire

def Recommencer():
    Jeu2.deiconify()
    BoutonDuFaible.config(text="Quitter le Jeu (Essayez peut être une autre difficulté)")
    JeuVictoire.destroy()

def Comparaison():
    global SaisieJeuu
    global JeuVictoire
    global BoutonDuFaible1
    SaisieJoueur=SaisieJeuu.get()
    if str(SaisieJoueur)>str(NbM):
        messagebox.showinfo(title="Raté !", message="Trop Grand !")
    elif str(SaisieJoueur)<str(NbM):
        messagebox.showinfo(title="Raté !", message="Trop Petit !")
    elif str(SaisieJoueur)==str(NbM):
        Jeuu.destroy()
        messagebox.showinfo(title="Bravo !", message="Bien Joué ! Appuyez sur Ok pour continuer")
        JeuVictoire =Tk()
        JeuVictoire.geometry("300x300")
        JeuVictoire.config(bg="pink")
        JeuVictoire.title("Félicitations")
        LabelVictoire = Label(JeuVictoire, text="C'est une belle victoire !", bg="red", fg="white")
        LabelVictoire.pack(ipady=20, ipadx=20, pady=20)
        BoutonRecommencer = Button(JeuVictoire, text="RECOMMENCER", bg="orange", fg="white", command=Recommencer)
        BoutonRecommencer.pack(ipady=10, ipadx=10, pady=20)
        BoutonDuFaible1 = Button(JeuVictoire, text="Quitter le jeu", command=Destroyall)
        BoutonDuFaible1.pack()
        JeuVictoire.mainloop()

#5eme Fenêtre : Jeu (il est trop bien   ͆͆͜  ) + Variations selon la difficulté choisie

def Abandon():
    Jeu.destroy()
    Jeu2.destroy()
    Jeuu.destroy()

def JeuTropDurN():
    Jeuu.destroy()
    JeuFacile()

def JeuTropDurD():
    Jeuu.destroy()
    JeuNormal()

def RetourFacile():
    Jeuu.destroy()
    JeuSuivant()

def JeuMain():
    global Jeuu
    global SaisieJeuu
    Jeu2.withdraw()
    Jeuu = Tk()
    if JeuFacile:
        Jeuu.title("Jeu Bien : "+titre)
        Jeuu.configure(bg=couleur)
        LabelJeuu = Label(Jeuu, text="Le nombre mystère se situe entre "+possibilites , bg="purple", fg="white")
        BoutonRetour = Button(Jeuu, text=text ,command=command)
    elif JeuNormal:
        Jeuu.title("Jeu Bien : "+titre)
        Jeuu.configure(bg=couleur)
        LabelJeuu = Label(Jeuu, text="Le nombre mystère se situe entre "+possibilites , bg="purple", fg="white")
        BoutonRetour = Button(Jeuu, text=text ,command=command)
    elif JeuDifficile:
        Jeuu.title("Jeu Bien : "+titre)
        Jeuu.configure(bg=couleur)
        LabelJeuu = Label(Jeuu, text="Le nombre mystère se situe entre "+possibilites , bg="purple", fg="white")
        BoutonRetour = Button(Jeuu, text=text ,command=command)
    Jeuu.geometry("400x400")
    LabelJeuu.pack(ipady=20, ipadx=50)
    SaisieJeuu = Entry (Jeuu)
    SaisieJeuu.pack(ipady=20, ipadx=50, padx=50, pady=50)
    BoutonValider = Button(Jeuu, text="Valider", command=Comparaison)
    BoutonValider.pack(pady=10)
    BoutonRetour.pack(pady=10)
    BoutonRageQuit = Button(Jeuu, text="Abandonner (ahah)", command=Abandon)
    BoutonRageQuit.pack(pady=10)
    Jeuu.mainloop()

#Variations Facile
def JeuFacile():
    global NbM
    global titre
    global possibilites
    global couleur
    global text
    global command
    command=RetourFacile
    text="Retour"
    couleur="yellow"
    possibilites="0 et 10"
    titre="Facile"
    NbM = randrange(0,10)
    print(NbM)
    JeuMain()

#Variations Normal
def JeuNormal():
    global NbM
    global titre
    global possibilites
    global couleur
    global text
    global command
    text="Aller à : Facile"
    command=JeuTropDurN
    couleur="orange"
    possibilites="0 et 100"
    titre="Normal"
    NbM = randrange(0,100)
    print(NbM)
    JeuMain()

#Variations Difficile
def JeuDifficile():
    global NbM
    global titre
    global possibilites
    global couleur
    global text
    global command
    text="Aller à : Normal"
    command=JeuTropDurD
    couleur="red"
    possibilites="0 et 1000"
    titre="Difficile"
    NbM = randrange(0,1000)
    print(NbM)
    JeuMain()

#4eme Fenêtre : Choix de la difficulté

def JeuSuivant():
    global Jeu2
    global BoutonDuFaible
    Jeu.withdraw()
    Jeu2 = Tk()
    Jeu2.geometry("400x650")
    Jeu2.title("Jeu Bien : Difficulté ")
    Jeu2.config(bg="lightblue")
    LabelDiff = Label(Jeu2, text="Choisissez votre difficulté", bg="black", fg="white")
    LabelDiff.pack_configure(pady=30, ipady=25, ipadx=40)
    BoutonFacile = Button(Jeu2, text=" Facile ", bg="yellow", fg="black", font=30, command=JeuFacile)
    BoutonFacile.pack(pady=20, ipady=35, ipadx=60)
    BoutonNormal = Button(Jeu2, text=" Normal ", bg="orange", fg="black", font=30, command=JeuNormal)
    BoutonNormal.pack(pady=20, ipady=35, ipadx=60)
    BoutonDifficile = Button(Jeu2, text=" Difficile ", bg="red", fg="black", font=30, command=JeuDifficile)
    BoutonDifficile.pack(pady=20, ipady=35, ipadx=60)
    BoutonDuFaible = Button(Jeu2, text="Quitter le jeu", command=Destroyall)
    BoutonDuFaible.pack()
    Jeu2.mainloop()

#3eme Fenêtre : Annonce des règles (transition auto.)

def DefRules():
    LabelRules = Label(Jeu, text="Vous devez trouver le nombre mystère", bg="yellow", fg="black")
    LabelRules.pack(pady=10)
    LabelRules1 = Label(Jeu, text="Vous aurez un certain nombre d'essai selon la difficulté", bg="lightgreen", fg="black")
    LabelRules1.pack(pady=10)

def DefGo():
    LabelGo = Label(Jeu, text="C'EST PARTI !", bg="blue", fg="black", font=50)
    LabelGo.pack(pady=10, ipadx=30, ipady=30)

def JeuAccueil():
    global Jeu
    global BoutonCommencer
    Jeu = Tk()
    Jeu.geometry("400x350")
    Jeu.title("Jeu Bien : Acceuil ")
    Jeu.config(bg="lightblue")
    LabelAccueil = Label(Jeu, text="Bienvenue sur le Jeu", bg="black", fg="white",font=50)
    LabelAccueil.pack(pady=10,ipady=20,ipadx=20)
    timer = threading.Timer(1.0, DefRules)
    timer.start()
    timer = threading.Timer(3.0, DefGo)
    timer.start()
    timer = threading.Timer(4.0, JeuSuivant)
    timer.start()
    Jeu.mainloop()

#Paramètres Connexion + 2eme Fenêtre: Accès au Jeu

def JeuEntree():
    fenetre2.destroy()
    JeuAccueil()

def Erreur():
    saisieid.config(bg="white")
    saisiemdp.config(bg="white")

def login ():
    global labelcc
    global labelab
    a=saisieid.get()
    b=saisiemdp.get()
    if a =="grp" and b =="grp":
        global fenetre2
        fenetre.destroy()
        fenetre2=Tk()
        fenetre2.geometry("400x400")
        fenetre2.config(bg="lightblue")
        fenetre2.title("login")
        labelco =Label(fenetre2,text ="Connexion réussie !")
        labelco.pack(ipady=20, ipadx=20, pady=20)
        boutonjeu = Button(fenetre2, text="Acceder au jeu",bg="blue", fg="white", command=JeuEntree,font=50)
        boutonjeu.pack(ipady=50, ipadx=70, pady=30)
        BoutonQuitter = Button(fenetre2, text="Quitter", command=fenetre2.destroy)
        BoutonQuitter.pack(pady=10)
        fenetre2.mainloop()
    elif a == "" or b =="":
        saisieid.config(bg="red")
        saisiemdp.config(bg="red")
        cc="Erreur: Aucun mot de passe et/ou identifiant renseigné(s)"
        labelcc = Label(fenetre,text=str(cc))
        labelcc.pack()
        TimerVide = threading.Timer(2.0, Erreur)
        TimerVide.start()
        TimerVide1 = threading.Timer(2.0, labelcc.destroy)
        TimerVide1.start()
    elif a !="grp" or b !="grp":
        saisieid.config(bg="red")
        saisiemdp.config(bg="red")
        ab="Erreur: Identifiant et/ou Mot de passe incorrect"
        labelab = Label(fenetre,text=str(ab))
        labelab.pack()
        TimerErreur = threading.Timer(2.0, Erreur)
        TimerErreur.start()
        TimerErreur1 = threading.Timer(2.0, labelab.destroy)
        TimerErreur1.start()

#1ere Fenetre : Login

fenetre=Tk()
fenetre.geometry("350x400")
fenetre.config(bg="magenta")
fenetre.title("Jeu Bien : Login")
labellogin = Label(fenetre,text="Saisir login",bg="grey",fg ="white")
labellogin.pack(ipadx=20, ipady=10)
saisieid=Entry(fenetre)
saisieid.pack(ipadx=30,ipady=10 ,pady=20)
labelmdp = Label(fenetre,text="Saisir le mot de passe",bg="grey",fg ="white")
labelmdp.pack(ipadx=20, ipady=10, pady=10)
saisiemdp=Entry(fenetre)
saisiemdp.pack(ipadx=30, ipady=10, pady=10)
boutonentrer =Button(fenetre,text="Se Connecter",command =login )
boutonentrer.pack()
boutonfermer = Button(fenetre,text="Quitter",command =fenetre.destroy)
boutonfermer.pack(pady=10)
fenetre.mainloop()
