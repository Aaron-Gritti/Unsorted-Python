"""Gritti Aaron"""

    # Imports
import PIL.Image
from PIL import Image, ImageTk
from tkinter import*
import threading                  # Timers pour bouton
import time                       # Timer dans l'execution du code ( aurait pu être utilisé dans l'easter egg mais code pas très lisible et trop d'erreurs après essai )
import tkinter.font as tkFont
from random import*

    # Dictionnaire des données
DicoCouleurs = {0:"green",1:"blue",2:"red",3:"pink",4:"purple"}
Dico = {"ScoreJ":0,"NbM":0,"ScoreO":0,"CoupJ":"Pas encore joué","CoupO":"Pas encore joué","Resultat":"Inconnu"}
ActionsPossibles = ["Pierre","Feuille","Ciseaux"]

##########################################################################################################################################################################################################################################################################
"""EASTER EGG : LE JEU BONUS ! (oui) /// Terminé !!!"""

def EasterLose():
    LabelRègles.place(x=100,y=20)
    LabelRègles.config(text="Vous avez découvert mais perdu l'easter egg... \r Vous pouvez appuyer sur le bouton pour aller sur le jeu !")
    Mhhh.place(x=275,y=300)
    Mhhh.config(text="Perdu !",command=Jouer)   # La fenêtre n'a pas changé, on peut appeler la transition de base comme si on avait pas fait l'easter egg
# Vous avez perdu !

def JouerAEgg():
    Jeu.deiconify()                 # On retourne sur le jeu comme si on avait appuyé sur Commencer dès le début (Sauf qu'il y a OhYeah a destroy (pas de withdraw car jamais réappelée))
    OhYeah.destroy()                # Oh No
# Transition de l'Easter egg au Jeu (laissée ici car sert uniquement à l'Easter egg)

def EasterWin():
    global OhYeah, BoutonYeah, LabelYeah2, EasterEggGagné
    EasterEggGagné="Oui"
    print("- Le bouton a réalisé "+str(i)+" mouvement(s) avant que vous ne l'attrapiez -")      # Une indication sympa
    if Dico["ScoreJ"]==0:
        Dico["ScoreJ"]=1                # Petite Récompense
    JeuRègles.withdraw()
    OhYeah = Tk()
    OhYeah.geometry("625x150")
    OhYeah.title("Bien Joué!")
    OhYeah.config(bg="pink")
    LabelYeah = Label(OhYeah, text="Vous avez découvert et fini l'easter egg ! \r En récompense, votre première manche gagnée vous apportera 2 points si vous n'êtes pas déja en pleine partie \r Appuyez sur le bouton pour aller sur le jeu !",bg="lightblue",fg="green")
    LabelYeah.pack()
    BoutonYeah = Button(OhYeah, text="GO !",fg="red",bg="white",font=25,command=JouerAEgg)
    BoutonYeah.pack()
    OhYeah.mainloop()
# Fenêtre optionelle : La Fin de l'easter egg (en cas de victoire) /// Terminée

def Easter6():
    global i, EasterEggGagné
    LabelRègles.config(text="Essayez d'attraper le bouton !")
    Mhhhbg="orange"
    if PartieRapide=="Oui":             # Si on a relancé une partie à partir de BoutonEaster
        Mhhhbg="white"
    Mhhh.config(bg=Mhhhbg,relief="groove",command=EasterWin)
    i=1
    print(i)
    EasterEggGagné="Non"                # Si on avait mis -if EasterEggGagné=="Non"- ici, Mhhh aurait continué de se déplacer et on l'aurait vu si on avait réouvert JeuRègles avant la fin des 15 mouvements de Mhhh
    for i in range(1,16):
        if EasterEggGagné=="Non":       # La boucle ne continuera pas si l'easter egg est gagné
            i+1
            X=randrange(20,500)
            Y=randrange(40,500)
            Mhhh.place(x=X,y=Y)
            time.sleep(0.85)            # Rapidité de changement de position de Mhhh
        if EasterEggGagné=="Non":       # Evite un dernier print après avoir appuyé sur le bouton (car appuyé loiymlkpendant le time.sleep)
            print(i+1)                  # Voir le nombre de mouvements de Mhhh depuis le début du jeu (dans la console)
    if EasterEggGagné=="Non":           # Si on a pas gagné, on perd (c'est logique...non ?)
        print("- Easter egg perdu -")   # Au cas où vous étiez pas sûr
        EasterLose()                    # On rend le code plus clair
# Code du jeu de l'easter egg

def Easter51():
    JeuRègles.config(bg="green")
# Disponible jusqu'à l'éxecution de Easter6 (1,9 secondes)

def Easter5():
    JeuRègles.geometry("600x600")
    LabelRègles.config(text="...",font=25)
    Mhhh.config(text="",command=Easter51)
    Mhhh.place(x=300,y=300)         # Mhhh Réapparait
    LabelRègles1.destroy()
    Egg4 = threading.Timer(1.9, Easter6)
    Egg4.start()

def Easter4():
    Mhhh.place_forget()             # Equivalent d'un withdraw pour un widget /// Replacer pour réafficher /// Si .pack utilisé - Variable.pack_forget()
    Egg3 = threading.Timer(2.0, Easter5)
    Egg3.start()

def Easter3():
    LabelRègles1.config(text="...", bg="red", fg="white",font=15)
    time.sleep(2)
    Mhhh.place(x=290,y=100)
    Mhhh.config(text="   ",command=Easter4)

def Easter2():
    JeuRègles.config(bg="magenta")
# Disponible jusqu'à l'execution de Easter3 (3 secondes)

def Easter1():
    JeuRègles.title("?")
    LabelRègles.config(text="Comment vous m'avez trouvé !?", bg="black", fg="white",font=20)

def PasDeJeuSansEasterEgg():
    global EasterEggTrouvé
    EasterEggTrouvé="Oui"
    GO.destroy()
    Mhhh.config(command=Easter2)
    Egg1 = threading.Timer(1.0, Easter1)        # Execute Easter1 après 1 seconde
    Egg1.start()
    Egg2 = threading.Timer(3.0, Easter3)        # Execute Easter2 après 3 secondes ( 2 secondes après l'execution de Easter1 )
    Egg2.start()
# L'easter egg commence

##########################################################################################################################################################################################################################################################################
"""TRANSITIONS"""

def QuitConf():
    JeuRègles.destroy()
    Jeu.destroy()
    JeuQuitF.destroy()
# Utilisé dans la fenêtre Jeu

def QuitConfTerminé():
    JeuTerminé.destroy()
    QuitConf()
# Utilisé dans la fenêtre JeuTerminé

def QuitterAnnuler():
    global QuitterAnnulé
    JeuQuitF.withdraw()
    QuitterAnnulé="Oui"
# Quand vous êtes pas sûr

def Recommencer():
    global Terminé, Dico
    Dico = {"ScoreJ":0,"NbM":0,"ScoreO":0,"CoupJ":"Pas encore joué","CoupO":"Pas encore joué","Resultat":"Inconnu"}
    if QuitterAnnulé=="Oui":
        JeuQuitF.withdraw()
    JeuTerminé.destroy()
    Terminé="Non"
    Jeu.deiconify()
    LabelJ.config(text="Joueur\r"+str(Dico["ScoreJ"]))
    LabelM.config(text="Manche\r"+str(Dico["NbM"]))
    LabelO.config(text="Ordinateur\r"+str(Dico["ScoreO"]))
    LabelAnnonces.config(text="Cliquez sur un des boutons en bas pour jouer !")
    BoutonPierre.config(state=NORMAL)
    BoutonFeuille.config(state=NORMAL)
    BoutonCiseaux.config(state=NORMAL)
    LabelAnnonces.place(x=100,y=210)
    BoutonRésultat.destroy()
# Redéfinition de Dico et de Jeu

def Jouer():
    Jeu.deiconify()                 # Jeu est affiché une première fois après son mainloop
    JeuRègles.withdraw()            # JeuRègles n'est pas destroy afin d'être utilisé plus tard
# Transition de JeuRègles à Jeu

def JeVoulaisUnTimer():
    GO.config(state=NORMAL)
    Mhhh.config(state=NORMAL)
    if EasterEggTrouvé=="Oui":
        BoutonEaster.config(state=NORMAL)
# Placement de la transtion si dessus

def EasterJeuRapide():
    global PartieRapide
    PartieRapide="Oui"
    Easter5()
    LabelRègles.config(bg="black",fg="white")
    JeuRègles.config(bg="grey")
    BoutonEaster.destroy()
    GO.destroy()
# Patient 1 fois mais pas 2

##########################################################################################################################################################################################################################################################################
"""CONFIG PRINCIPALE DES FENETRES SECONDAIRES (+ PLACEMENT EASTER EGG)"""

def JeuQuitConf():
    global JeuQuitF, LeMauvaisChoix, LeBonChoix, QuitterAnnulé
    QuitterAnnulé="Non"
    JeuQuitF = Tk()
    JeuQuitF.title("Quitter ?")
    JeuQuitF.geometry("250x100")
    JeuQuitF.config(bg="green")
    LabelQuit = Label(JeuQuitF,text="Voulez vous vraiment quitter ?",fg="white",bg="black")
    LeMauvaisChoix = Button(JeuQuitF,text="Oui",fg="white",bg="red",command=QuitConf)
    if Terminé=="Oui":
        LeMauvaisChoix.config(command=QuitConfTerminé)
    if Terminé=="Non":
        LeMauvaisChoix.config(command=QuitConf)
    LeBonChoix = Button(JeuQuitF,text="Annuler",command=QuitterAnnuler)
    LabelQuit.pack()
    LeMauvaisChoix.pack(pady=10)
    LeBonChoix.pack()
    JeuQuitF.mainloop()
# Dernière fenêtre affichée et réaffichable en passant par Jeu et JeuTerminé : La Porte de sortie !(suuuuper :\) /// Terminée

def JeuTerminéDef():
    global JeuTerminé, Terminé
    Terminé="Oui"
    JeuTerminé = Tk()
    JeuTerminé.geometry("500x150")
    JeuTerminé.title(str(titre))
    JeuTerminé.config(bg=str(couleurbg))
    if EasterEggTrouvé=="Oui":
        LabelFinal = Label(JeuTerminé,text=str(label)+"\r ...et vous avez découvert l'easter egg, félicitations !",font=30)
    else:
        LabelFinal = Label(JeuTerminé,text=str(label)+"\r Il vous reste peut être encore des secrets à découvrir",font=30)
    BoutonFinalRecommencer = Button(JeuTerminé,text="Recommencer ?",bg="green",fg="white",command=Recommencer)
    BoutonFinalQuitter = Button(JeuTerminé,text="Quitter ?",bg="orange",fg="white",command=JeuQuitConf)
    LabelFinal.pack(pady=10)
    BoutonFinalRecommencer.pack(pady=10)
    BoutonFinalQuitter.pack(pady=10)
    JeuTerminé.mainloop()
# Fenêtre affichée lors de la fin de la partie (appui du bouton BoutonVerdict), modifiée selon les résultats /// Terminée

def JeuRèglesDef():
    global JeuRègles , GO , LabelRègles , LabelRègles1 , Mhhh, BoutonEaster
    Jeu.withdraw()                  # On applique un withdraw à Jeu pour qu'il ne s'affiche pas du tout ( Car avant son mainloop )
    JeuRègles = Tk()
    JeuRègles.geometry("600x200")
    JeuRègles.title("Les Règles")
    JeuRègles.config(bg="lightblue")
    LabelRègles = Label(JeuRègles,text="Il s'agit d'un jeu de pierre feuille ciseaux",bg="lightblue")
    LabelRègles1 = Label(JeuRègles,text="Le joueur ayant le plus de points en 10 manches gagne \r Une 11ème manche sera ajoutée si égalité",bg="lightblue")
    Mhhh = Button(JeuRègles,command=PasDeJeuSansEasterEgg,text="\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", state=DISABLED)  # Oui ça fait beaucoup
    GO = Button(JeuRègles,text="Commencer !",command=Jouer,font=30,state=DISABLED) # Voir Jouer /// Est packé dans JeVoulaisUnTimer
    BoutonEaster = Button(JeuRègles,text="Partie Rapide",bg="brown",fg="yellow",command=EasterJeuRapide,state=DISABLED)
    LabelRègles.pack(pady=10)
    LabelRègles1.pack()
    if EasterEggTrouvé=="Non":
        Mhhh.place(x=-10,y=100)
    GO.place(x=250,y=150)
    TimerGO = threading.Timer(2.0, JeVoulaisUnTimer)    # C'est mieux de lire les règles, non ? ( A partir de 2 secondes, JeVoulaisUnTimer est exécuté )
    TimerGO.start()
    if EasterEggTrouvé=="Oui":
        JeuRègles.geometry("600x230")                  # C'était pas assez grand
        BoutonEaster.place(x=265,y=200)
    JeuRègles.mainloop()
# 1ere fenêtre affichée et réaffichable en passant par Jeu : Les Règles du jeu ! /// Terminée

##########################################################################################################################################################################################################################################################################
"""FONCTIONS DE CONFIG SELON DEROULEMENT DU JEU OU ACTIONS DE L'UTILISATEUR"""

def JeuVictoire():
    global titre
    global couleurbg
    global label
    titre="Bien Joué !"
    couleurbg="blue"
    label="Vous avez remporté ce match de Pierre Feuille Ciseaux !"
    Jeu.withdraw()
    JeuTerminéDef()
# Déclenché lors d'une victoire de partie (trop d'la chance !)

def JeuDéfaite():
    global titre
    global couleurbg
    global label
    titre="Dommage !"
    couleurbg="pink"
    label="Vous avez perdu ce match de Pierre Feuille Ciseaux..."
    Jeu.withdraw()
    JeuTerminéDef()
# Déclenché lors d'une défaite de partie (ahah)

def JeuCouleur2():
    Jeu.config(bg=couleur)
    ImgJ.config(bg=couleur)
    ImgM.config(bg=couleur)
    ImgO.config(bg=couleur)
    LabelAnnonces.config(bg=couleur)
    BoutonPierre.config(bg=couleur,activebackground=couleur)
    BoutonFeuille.config(bg=couleur,activebackground=couleur)
    BoutonCiseaux.config(bg=couleur,activebackground=couleur)
    JeuCouleur()
# Applique la couleur indiquée sur le bouton sur la plupart des labels/boutons

def JeuCouleur():
    global couleur
    CouleurAl = randrange(0,5)
    couleur = DicoCouleurs[CouleurAl]
    BoutonCouleur.config(bg=couleur,activebackground=couleur)
# Choisit une couleur aléatoire (dans DicoCouleurs) et l'applique à BoutonCouleur pour indiquer la couleur suivante

##########################################################################################################################################################################################################################################################################
"""CONFIG TOUR JOUEUR/TOUR ORDINATEUR + ACTIONS LIEES AU POINTS"""

# Fonction Ordinateur
def TourOrdinateur():
    global BoutonRésultat
    gras = tkFont.Font(weight="bold",size=20)
    Dico["CoupO"] = ActionsPossibles[randrange(0,3)]
    if Dico["CoupO"]=="Pierre":
        ImgO.config(image=ImgPierre)
    if Dico["CoupO"]=="Feuille":
        ImgO.config(image=ImgFeuille)
    if Dico["CoupO"]=="Ciseaux":
        ImgO.config(image=ImgCiseaux)
    # Affichage du coup joué par l'ordinateur

    if Dico["CoupO"]=="Ciseaux"and Dico["CoupJ"]=="Pierre" or Dico["CoupO"]=="Feuille"and Dico["CoupJ"]=="Ciseaux" or Dico["CoupO"]=="Pierre"and Dico["CoupJ"]=="Feuille":
        Dico["ScoreJ"]+=1
        LabelJ.config(text="Joueur\r"+str(Dico["ScoreJ"]))
        LabelAnnonces.config(text="Manche gagnée")
        LabelAnnonces.place(x=205,y=210)
    # Victoire de manche

    if Dico["CoupO"]=="Pierre"and Dico["CoupJ"]=="Ciseaux" or Dico["CoupO"]=="Ciseaux"and Dico["CoupJ"]=="Feuille" or Dico["CoupO"]=="Feuille"and Dico["CoupJ"]=="Pierre":
        Dico["ScoreO"]+=1
        LabelO.config(text="Ordinateur\r"+str(Dico["ScoreO"]))
        LabelAnnonces.config(text="Manche perdue")
        LabelAnnonces.place(x=205,y=210)
    # Défaite de manche

    if Dico["CoupO"]==Dico["CoupJ"]:
        LabelAnnonces.config(text="Match nul!")
        LabelAnnonces.place(x=220,y=210)
    # Egalité de manche
#Changements selon l'issue de la manche

    Dico["NbM"]+=1
    LabelM.config(text="Manche\r"+str(Dico["NbM"]))
    if Dico["NbM"]>=10:
        BoutonPierre.config(state=DISABLED)
        BoutonFeuille.config(state=DISABLED)
        BoutonCiseaux.config(state=DISABLED)
        if Dico["ScoreJ"]>Dico["ScoreO"]:
            Dico["Resultat"]="Gagné"
            BoutonRésultat = Button(Jeu,text="Résultat",command=JeuVictoire,font=gras,bg="blue")
            BoutonRésultat.place(x=197.5,y=205)
        # Victoire de partie
        if Dico["ScoreJ"]<Dico["ScoreO"]:
            Dico["Resultat"]="Perdu"
            BoutonRésultat = Button(Jeu,text="Résultat",command=JeuDéfaite,font=gras,bg="blue")
            BoutonRésultat.place(x=197.5,y=205)
        # Défaite de partie
        if Dico["ScoreJ"]==Dico["ScoreO"]:
            LabelAnnonces.config(text="Egalité ! Qui va se démarquer et gagner cette partie ?")
            LabelAnnonces.place(x=70,y=210)
            BoutonPierre.config(state=NORMAL)
            BoutonFeuille.config(state=NORMAL)
            BoutonCiseaux.config(state=NORMAL)
        # Scores à égalité à l'issue de la dernière manche
# Changements selon l'issue de la partie

def PierreJouée():
    Dico["CoupJ"] = "Pierre"
    ImgJ.config(image=ImgPierre)
    TourOrdinateur()
# Quand la pierre est jouée

def FeuilleJouée():
    ImgJ.config(image=ImgFeuille)
    Dico["CoupJ"] = "Feuille"
    TourOrdinateur()
# Quand la feuille est jouée

def CiseauxJoués():
    ImgJ.config(image=ImgCiseaux)
    Dico["CoupJ"] = "Ciseaux"
    TourOrdinateur()
# Quand les ciseaux sont joués

##########################################################################################################################################################################################################################################################################
"""CONFIG PRINCIPALE DU JEU"""

Terminé="Non"
QuitterAnnulé="Non"
EasterEggTrouvé="Non"
EasterEggGagné="Non"
PartieRapide="Non"
# Points de passage

Jeu = Tk()
Jeu.geometry("525x500")
Jeu.config(bg="purple")
Jeu.title("Pierre - Feuille - Ciseaux")
# Config fenêtre

ImgVersus = PhotoImage(file='versus.png')
ImgPierre = PhotoImage(file='pierre.png')
ImgCiseaux = PhotoImage(file='ciseaux.png')
ImgFeuille = PhotoImage(file='feuille.png')
# Definition des images

LabelJ = Label(Jeu,text="Joueur\r"+str(Dico["ScoreJ"]),font=30)
LabelM = Label(Jeu,text="Manche\r"+str(Dico["NbM"]),font=30)
LabelO = Label(Jeu,text="Ordinateur\r"+str(Dico["ScoreO"]),font=30)
ImgJ = Label(Jeu, image=ImgVersus,bg="purple")
ImgM = Label(Jeu, image=ImgVersus,bg="purple")                                 # Ne sera pas changée de tout le jeu
ImgO = Label(Jeu, image=ImgVersus,bg="purple")
LabelAnnonces = Label(Jeu,text="Cliquez sur un des boutons en bas pour jouer !",font=30,bg="purple",fg="white")
# Création des Labels

BoutonPierre = Button(Jeu,image=ImgPierre,bg="purple",activebackground="purple",relief="flat",command=PierreJouée)
BoutonFeuille = Button(Jeu,image=ImgFeuille,bg="purple",activebackground="purple",relief="flat",command=FeuilleJouée)
BoutonCiseaux = Button(Jeu,image=ImgCiseaux,bg="purple",activebackground="purple",relief="flat",command=CiseauxJoués)
# Création des boutons de jeu /// bg , activebackground (bg quand appuyé) et relief rendent le contour des boutons invisible

BoutonCouleur = Button(Jeu, text="Changer de couleur",command=JeuCouleur2)
JeuCouleur()
Règles = Button(Jeu,text="Revoir les règles",command=JeuRèglesDef)
Quitter = Button(Jeu,text="Quitter",fg="white",bg="orange",command=JeuQuitConf)
# Création des autres boutons

LabelJ.place(x=50,y=20)
LabelM.place(x=230,y=20)
LabelO.place(x=410,y=20)
ImgJ.place(x=20,y=80)
ImgM.place(x=205,y=80)
ImgO.place(x=390,y=80)
LabelAnnonces.place(x=100,y=210)
# PLacement des labels

BoutonPierre.place(x=20,y=270)
BoutonFeuille.place(x=205,y=270)
BoutonCiseaux.place(x=390,y=270)
# Placement des boutons de jeu

BoutonCouleur.place(x=205,y=425)
Règles.place(x=215,y=450)
Quitter.place(x=240,y=475)
# Placement des autres boutons

JeuRèglesDef()                  # On aurait pu mettre ces fenêtres à la suite (sans mettre JeuRègles dans une def) mais les withdraws auraient étés beaucoup plus compliqué à mettre en place
Jeu.mainloop()
# Ceci est la 2eme fenêtre affichée : Le Jeu ! /// Grâce à une technique incroyable, la 1ere fenêtre est celle de JeuRèglesDef /// Terminée


