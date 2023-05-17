from tkinter import*
from PIL import Image
from tkinter import messagebox
import time
import threading
from random import*
import webbrowser

def BackFromTheDead():
    global Crane, Mort, WhichCrane
    Crane = ca.create_image(500, 250, image=KyleCrane)
    Mort=False
    WhichCrane+=1

def TraitementVaccin():
    global Crane, Vaccin, JeuTerminé
    if JeuTerminé==False:
        xz,yz = ca.coords(Vaccin)
        xc,yc = ca.coords(Crane)
        if xz-20<xc<xz+20 and yz-20<yc<yz+20:
            messagebox.showinfo("Félicitations","Vous avez trouvé le vaccin du Co..euh...du virus d'Harran, bien joué !")
            ca.delete(Vaccin)
            JeuTerminé=True

def Transformation():
    global Zombified, Zombie1, ZombieDead, ZombieBalle1
    xc,yc = ca.coords(Crane)
    ZombieBalle1=False
    if Zombified==True:
        xz1,yz1 = ca.coords(Zombie1)
        ca.delete(Zombie1)                                                # Le corps du dernier zombie à déjà pourri avant que vous ne vous retransformiez
        ZombieDead = ca.create_image(xz1,yz1, image=imageZombieDead)      
    Zombified=True
    ca.delete(Crane)
    Zombie1 = ca.create_image(xc,yc, image=imageZombie) # Le zombie ne "rodera" pas pour la même raison que "LaHorde" est un échec

def VirusTenace():
    global Mort, Infection, Crane, InfectionBase
    if InfectionBase==True and Mort==False and (WhichCrane==ThatCrane0 or WhichCrane==ThatCrane1):                 # Si le timer Infecté n'est pas fini , rien d'autre ne vous tuera d'infection (ça sonne mal mais c'est pas si bête...enfin je crois)
        messagebox.showinfo("Aarrghh","Vous êtes mort! Le virus a fini par avoir raison de vous, l'antizine ne vous aura pas sauvé de la tranformation")
        Mort=True
        Infection=False
        Transformation()
        BackAlive = threading.Timer(5.0,BackFromTheDead)
        BackAlive.start()

def TraitementInfection():
    global Mort, Infection, Crane
    if  WhichCrane==ThatCrane0 or WhichCrane==ThatCrane1:
        if Infection==True and Mort==False:  # Si le timer Infecté n'est pas fini , rien d'autre ne vous tuera d'infection (ça sonne mal mais c'est pas si bête...enfin je crois)
            messagebox.showinfo("Aarrghh","Vous êtes mort! Votre infection était plus rapide que vous ne le pensiez")
            Mort=True
            Infection=False
            Transformation()
            BackAlive = threading.Timer(5.0,BackFromTheDead)
            BackAlive.start()
        else:
            FinalDeath = threading.Timer(60.0, VirusTenace)
            FinalDeath.start()

def ZombieRodeur():
    global CompteurDirection, Zombie, BanMoonwalk
    CompteurDirection+=1
    TraitementDirection()
    if CompteurDirection>=0 and CompteurDirection<=30:      # On ne place pas le temps d'attente ici pour que le zombie se déplace directement à son apparition
        xz,yz = ca.coords(Zombie)
        ca.delete(Zombie)
        Zombie = ca.create_image(xz,yz, image=BanMoonwalk)
        ca.move(Zombie,+2,0)
    if CompteurDirection>=35:
        xz,yz = ca.coords(Zombie)
        ca.delete(Zombie)
        Zombie = ca.create_image(xz,yz, image=BanMoonwalk)
        ca.move(Zombie,-2,0)
    if CompteurDirection==65:
        CompteurDirection=-5                                # Temps avant de repartir vers la droite (en positif ducoup)
    DyingLight.after(80,ZombieRodeur)

def CestBobLeBricoleur():
    global Nuage, Bob, NuageSolide
    Nuage = ca.create_image(865, 355, image=imageNuage)
    messagebox.showinfo("bob","nuage")
    ca.delete(Bob)                                          # Oh noo :(
    Bob = ca.create_image(160, 580, image=BobLePersonnageQuiBricoleToutSurtoutDesNuagesPourKyleCraneLePersonnageControlable)    # Bob is not killable !!
    NuageSolide=True

def Mhhh():
    global QuelGenie
    QuelGenie = threading.Timer(3.0,CestBobLeBricoleur)
    QuelGenie.start()

def TraitementBob():
    global Bob, Mhhh, BobNuage, NuageSolide, NGGYU
    xz1,yz1 = ca.coords(Bob)
    xc,yc = ca.coords(Crane)
    if xz1-20<xc<xz1+20 and yz1-20<yc<yz1+20 and BobNuage==False:
        BobNuage=True
        messagebox.showinfo("Crane","Salut")
        messagebox.showinfo("Bob","bob")
        messagebox.showinfo("Crane","Peux-tu réparer le pont?")
        messagebox.showinfo("Bob","bob pas comprendre")
        messagebox.showinfo("Crane","Peux-tu BRICOLER le pont?")
        messagebox.showinfo("Bob","Bri-co-ler!!!")
        ca.delete(Bob)                                                      # Il reviendra plus fort !
        Bob = ca.create_image(870, 350, image=BobLePersonnageQuiBricoleToutSurtoutDesNuagesPourKyleCraneLePersonnageControlable)
        Mhhh = threading.Timer(2.0,Mhhh)
        Mhhh.start()
    if xz1-20<xc<xz1+20 and yz1-20<yc<yz1+20 and NuageSolide==True and NGGYU==False:
        NGGYU=True
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")      # Lien bonus!

def AntizineUse():
    global Infection, BoutonAntizine, AntizineUsed
    if Infection==True:
        AntizineUsed=True
        Infection=False
        messagebox.showinfo("Sauvé !","Vous avez annihilé l'antizine, vous vous sentez mieux à présent")
        BoutonAntizine.destroy()
    else:
        messagebox.showinfo("Non","Vous n'avez pas besoin d'antizine pour l'instant")

def TraitementAntizine():
    global Crane, Antizine, Infection, AntizinePick, TAntizineOff, BoutonAntizine, Inventaire
    if TAntizineOff==False:
        xz,yz = ca.coords(Antizine)
        xc,yc = ca.coords(Crane)
        if xz-20<xc<xz+20 and yz-20<yc<yz+20 and Infection==True:
            TAntizineOff=True
            messagebox.showinfo("Sauvé !","Vous avez trouvé de l'antizine, vous vous sentez mieux à présent")
            Infection=False
            ca.delete(Antizine)
        elif xz-20<xc<xz+20 and yz-20<yc<yz+20:
            TAntizineOff=True
            messagebox.showinfo("Antizine Ramassée","Vous avez trouvé de l'antizine, elle est déshormais placée dans votre inventaire")
            AntizinePick=True
            BoutonAntizine = Button(Inventaire,text="Antizine",fg="white",bg="brown",command=AntizineUse)
            BoutonAntizine.pack()
            ca.delete(Antizine)

def TraitementZombie():
    global Crane, Zombie, Zombie1, Infection, Infecté, Encerclé, FinalDeath, ThatCrane0, ThatCrane1, InfectionBase, ZombieBalle1
    if Zombified==True:
        xz1,yz1 = ca.coords(Zombie1)
        xc,yc = ca.coords(Crane)
        if xz1-20<xc<xz1+20 and yz1-20<yc<yz1+20 and ZombieBalle1==False:       # Mordu par soi-même
            ThatCrane0 = WhichCrane
            ZombieBalle1=True
            messagebox.showinfo("Grooahh","Un zombie assez familier vous a mordu ! Trouvez de l'antizine pour vous soigner ! ")
            Infection=True
            InfectionBase=True
            Infecté = threading.Timer(15.0, TraitementInfection)
            Infecté.start()
    xz,yz = ca.coords(Zombie)
    xc,yc = ca.coords(Crane)
    if xz-20<xc<xz+20 and yz-20<yc<yz+20:
        ThatCrane1 = WhichCrane
        messagebox.showinfo("Grooahh","Un zombie vous a mordu ! Trouvez de l'antizine pour vous soigner ! Vite !")
        Infection=True
        InfectionBase=True
        Infecté = threading.Timer(15.0, TraitementInfection)
        Infecté.start()

def TraitementBornes():
    global Crane, ca, LienOuvert, AppelDeBob
    xC1,yC1 = ca.coords(Crane)
    if xC1>1042 and JeuTerminé==True and LienOuvert==False:                          # La fin du jeu
        if AppelDeBob==False and NGGYU==False:
            messagebox.showinfo("?","Vous entendez Bob vous appeler, allez le voir !")
            ca.delete(Crane)
            Crane = ca.create_image(xC1-20,yC1, image=listeImageCrane[2][2])
            AppelDeBob=True
        if NGGYU==True:
            DyingLight.destroy()
            webbrowser.open("https://www.youtube.com/watch?v=UwJAAy7tPhE&ab_channel=DyingLight")          # Ad
            LienOuvert=True                                                         # Vous pouvez maintenant entrer dans l'infini
    if yC1>707:
        ca.delete(Crane)
        Crane = ca.create_image(xC1,10, image=listeImageCrane[indiceLigne][compteurImage])
    if xC1<0:
        ca.delete(Crane)
        Crane = ca.create_image(xC1+20,yC1, image=listeImageCrane[3][0])
        messagebox.showinfo("Montagnes","Cette zone est bloquée par des montagnes")
    if yC1<0:
        ca.delete(Crane)
        Crane = ca.create_image(xC1,707, image=listeImageCrane[indiceLigne][compteurImage])
    """Problème : Comment savoir de quel côté le personnage va t'il dans l'eau ? /// On peut passer à travers l'eau en nageant dans les messagebox :)"""
    """Solution : Faire noyer le perso à chaque fois qu'il touche l'eau pour pas le relocaliser !! /// Je vais pas le faire c'est pas gentil"""
    if xC1>840 and yC1<340 and x<850:              # Eau nord
        ca.delete(Crane)
        Crane = ca.create_image(xC1-10,yC1, image=listeImageCrane[2][2])
        messagebox.showinfo("Eau","Vous voulez vous noyez ?")
    if xC1>840 and yC1>350 and x<850:              # Eau sud
        ca.delete(Crane)
        Crane = ca.create_image(xC1-10,yC1, image=listeImageCrane[2][2])
        messagebox.showinfo("Eau","Vous voulez vous noyer ?")
    if 840<xC1<880 and 330<yC1<370 and NuageSolide==False:
        messagebox.showinfo("Trou","Il faut que je trouve un moyen de traverser!")
        ca.delete(Crane)
        Crane = ca.create_image(xC1-10,yC1, image=listeImageCrane[2][2])
    if xC1>840 and yC1<340 and x>840:
        ca.delete(Crane)
        Crane = ca.create_image(xC1,yC1+10, image=listeImageCrane[0][0])
        messagebox.showinfo("Eau","Vous ne survivrez pas à cette chute")
    if xC1>840 and yC1>350 and x>840:
        ca.delete(Crane)
        Crane = ca.create_image(xC1,yC1-10, image=listeImageCrane[1][1])
        messagebox.showinfo("Eau","Vous ne survivrez pas à cette chute")

def BobTheInvincible():
    global Bob
    ca.delete(Bob)
    Bob = ca.create_image(160, 580, image=BobLePersonnageQuiBricoleToutSurtoutDesNuagesPourKyleCraneLePersonnageControlable)

def TraitementBalle():
    global Balle, Bob, BobVenere, Balle, Zombie, ZombieBalle, Zombie1, ZombieBalle1
    xBa,yBa = ca.coords(Balle)
    xBz,yBz = ca.coords(Zombie)
    if Zombie1 != False:
         xBz1,yBz1 = ca.coords(Zombie1)
    if xBa-20<xBz<xBa+20 and yBa-20<yBz<yBa+20:
        ZombieBalle=True
        ca.delete(Balle)
        Balle = ca.create_image(-1000, -1000, image=imageBalleBas)
        ca.delete(Zombie)       # Tirer sur un zombie le force à bouger à une autre position
        x=randrange(300,700)
        y=randrange(200,600)
        Zombie = ca.create_image(x, y, image=imageZombie)
    if Zombie1 != False:
        if xBa-20<xBz1<xBa+20 and yBa-20<yBz1<yBa+20:
            ZombieBalle1=True
            ca.delete(Balle)
            Balle = ca.create_image(-1000, -1000, image=imageBalleBas)
            ca.delete(Zombie1)       # Tirer sur un zombie le force à bouger à une autre position
            Zombie1 = ca.create_image(xBz1, yBz1, image=imageZombieDead)
    if BobVenere==False:
        xBa,yBa = ca.coords(Balle)
        xB,yB = ca.coords(Bob)
        if xBa-20<xB<xBa+20 and yBa-20<yB<yBa+20:
            BobVenere=True
            ca.delete(Balle)
            Balle = ca.create_image(-1000, -1000, image=imageBalleBas)
            ca.delete(Bob)
            Bob = ca.create_image(160, 580, image=BobLeGrand)
            BobBob = threading.Timer(3.0,BobTheInvincible)
            BobBob.start()

def PewPew():
    global Tir, Balle, xBalle, yBalle
    if Tir==True:
        ca.move(Balle,xBalle,yBalle)
        TraitementBalle()
    DyingLight.after(10,PewPew)

def Action(event):
    global compteurImage, indiceLigne, Crane, Zombie, AntizinePick, Inventaire, InventaireOuvert, Bob, Tir, Balle, TirSet, xBalle, yBalle, y, x
    if Mort==False:
        x,y = ca.coords(Crane)
        compteurImage+=1
        if compteurImage==4:
            compteurImage=0
        # Mouvement
        if event.char == "d" or event.char == "D":      # C'est chiant de penser qu'on a tout cassé alors qu'on est juste en majuscule
            ca.delete(Crane)
            indiceLigne=3
            Crane = ca.create_image(x+10, y, image=listeImageCrane[indiceLigne][compteurImage])
        if event.char == "a" or event.char == "A":
            ca.delete(Crane)
            indiceLigne=2
            Crane = ca.create_image(x-10, y, image=listeImageCrane[indiceLigne][compteurImage])
        if event.char == "w" or event.char =="W":
            ca.delete(Crane)
            indiceLigne=1
            Crane = ca.create_image(x, y-10, image=listeImageCrane[indiceLigne][compteurImage])
        if event.char == "s" or event.char =="S":
            ca.delete(Crane)
            indiceLigne=0
            Crane = ca.create_image(x, y+10, image=listeImageCrane[indiceLigne][compteurImage])
        # Tir
        if event.char == "u" or event.char =="U":
            xC,yC = ca.coords(Crane)
            ca.delete(Balle)
            Balle = ca.create_image(xC, yC, image=imageBalleHaut)
            xBalle=0
            yBalle=-10
            Tir=True
        if event.char == "h" or event.char =="H":
            xC,yC = ca.coords(Crane)
            ca.delete(Balle)
            Balle = ca.create_image(xC, yC, image=imageBalleGauche)
            xBalle=-10
            yBalle=0
            Tir=True
        if event.char == "k" or event.char =="K":
            xC,yC = ca.coords(Crane)
            ca.delete(Balle)
            Balle = ca.create_image(xC, yC, image=imageBalleDroite)
            xBalle=+10
            yBalle=0
            Tir=True
        if event.char == "j" or event.char =="J":
            xC,yC = ca.coords(Crane)
            ca.delete(Balle)
            Balle = ca.create_image(xC, yC, image=imageBalleBas)
            xBalle=0
            yBalle=+10
            Tir=True
        TraitementBornes()
        TraitementZombie()
        TraitementAntizine()
        TraitementBob()
        TraitementVaccin()
        #Inventaire
        if InventaireOuvert==False:
            InventaireOuvert=True          # Bob n'est pas un objet (même si il n'a pas de forme d'intelligence) alors l'inventaire n'est utile que pour l'antizine
            Inventaire = Tk()
            Inventaire.geometry("200x200")
            Inventaire.title("Inventaire")
            Inventaire.config(bg="brown")
            Inventaire.mainloop()
    """NE RIEN METTRE ICI"""

def TraitementDirection():
    global BanMoonwalk  # Sorry Michael
    if CompteurDirection<=35:
        BanMoonwalk=imageZombie1
    if CompteurDirection>=36:
        BanMoonwalk=imageZombie

def LaHorde():
    global Zombie, x, y
    x=randrange(300,700)
    y=randrange(200,600)
    ca.delete(Zombie)
    TraitementDirection()
    Zombie = ca.create_image(x,y, image=BanMoonwalk)
    DyingLight.after(5200,LaHorde)

def InventaireD():
    global Inventaire, InventaireOuvert
    Inventaire.destroy()
    InventaireOuvert=False

def Spawn(event):
    global Crane, Zombie, Mort, x, y, Spawned, Antizine, AntizinePick, Bob, Vaccin, Balle
    if Spawned==False:
        Crane = ca.create_image(500, 250, image=KyleCrane)
        Antizine = ca.create_image(840, 175, image=imageSeringue)
        Bob = ca.create_image(160, 580, image=BobLePersonnageQuiBricoleToutSurtoutDesNuagesPourKyleCraneLePersonnageControlable)
        Vaccin = ca.create_image(1000, 350, image=imageVaccin)
        Balle = ca.create_image(10000, 3500, image=imageBalleBas)      # Anti Bug
        PewPew()        # La balle balle bouge directement à sa premiere apparition, tirer ne la fait qu'apparaitre devant le personnage
        print("Kyle Crane a été parachuté dans Harran !")
        TAntizineOff=False
        x=100
        y=200
        Zombie = ca.create_image(x, y, image=imageZombie)
        ZombieRodeur()
        LaHorde()       # Enlevez "Spawned" et la ligne 4 de "LaHorde" du code et regardez la horde envahir la map !
        Spawned=True

"""Bool"""
WhichCrane = 0
ThatCrane0 = 0
ThatCrane1 = 0
Zombie1 = False
ZombieBalle1=False
BobVenere=False
Tir=False
AppelDeBob=False
LienOuvert=False
NGGYU=False
JeuTerminé=False
NuageSolide=False
BobNuage=False
Zombified=False
AntizineUsed=False
Infection=False
InfectionBase=False
InventaireOuvert=False
TAntizineOff=False
AntizinePick=False
CraneIsAlive=False          # Oh noo! Crane is ded :(
Spawned=False
Zombie1spawned=False
Mort=False
Infection=False      
compteurImage=0
indiceLigne=0
CompteurDirection=0
"""Bool End"""              # Oui y a autre chose que du bool mais je savais pas où le mettre.

DyingLight = Tk()
DyingLight.title("Dying Light")
DyingLight.geometry("1042x707")

img = Image.open(r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/SpriteDL.png")
listeImageCrane = []        # Le nom se prononce Crayne pour info
for i in range(0,4):        
    xg=i*40
    xd=xg+40
    listeTemp = []
    for j in range(0,4):    # 4 colonnes
        yg=j*35
        yd=yg+35
        img2 = img.crop([yg,xg,yd,xd])
        img2.save(r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/Crane.png")
        Crane = PhotoImage(file=r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/Crane.png")
        listeTemp.append(Crane)
    listeImageCrane.append(listeTemp)

imageMap = PhotoImage(file=r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/DyingLightMap.png")
KyleCrane = PhotoImage(file=r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/KyleCrane.png")         # Le perso n'est pas Kyle Crane de Dying Light mais Frisk de Undertale 
imageZombie = PhotoImage(file=r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/Zombie.png")
imageZombie1 = PhotoImage(file=r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/ZombieTourne.png")
imageZombieDead = PhotoImage(file=r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/ZombieDead.png")
imageSeringue = PhotoImage(file=r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/Antizine.png")
imageVaccin = PhotoImage(file=r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/Vaccin.png")
imageNuage = PhotoImage(file=r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/Nuage.png")
imageBalleBas = PhotoImage(file=r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/BalleBas.png")
imageBalleHaut = PhotoImage(file=r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/BalleHaut.png")
imageBalleDroite = PhotoImage(file=r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/BalleDroite.png")
imageBalleGauche = PhotoImage(file=r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/BalleGauche.png")
BobLeGrand = PhotoImage(file=r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/GrosBob.png")
BobLePersonnageQuiBricoleToutSurtoutDesNuagesPourKyleCraneLePersonnageControlable = PhotoImage(file=r"c:\Users\aaron\Documents\All the past Python shit\NSI\Save Python\images/BobLeBricoleur.png")   # Bob

ca = Canvas (width=1042,height=707)
ca.place(x=0,y=0)
map = ca.create_image(524, 353 , image=imageMap)

DyingLight.bind("<Double-Button-1>", Spawn)
DyingLight.bind("<Any-KeyPress>", Action)

DyingLight.mainloop()

DyingLight.after(100,ZombieRodeur)
DyingLight.after(5200,LaHorde)
DyingLight.after(10,PewPew)