from tkinter import messagebox
from random import*

class Epee:
    __nom = ""
    __atk = 0

    def __init__(self,nom="",atk=0):
        self.__nom = nom
        self.__atk = atk

    def __str__(self):
        return "L'arme : "+self.__nom+" (niveau d'attaque : "+str(self.__atk)+")"

    def getNomE(self):
        return self.__nom
    def getAtk(self):
        return self.__atk

class Objet:
    __nom = ""
    __soin = 0

    def __init__(self,nom="",soin=0):
        self.__nom = nom
        self.__soin = soin

    def __str__(self):
        return "L'objet : "+self.__nom+" (Vous redonnera : "+str(self.__soin)+" points de vie)"

    def getNomO(self):
        return self.__nom
    def getSoin(self):
        return self.__soin

class Guerrier:
    __nom = ""
    __vie = 0
    __armeEnMain = ""

    def __init__(self,nom="",vie=0):
        self.__nom = nom
        self.__vie = vie
        self.__listeArme = []
        self.__listeObjet = []

    def setVie(self,vie):
        self.__vie = vie
    def getNomG(self):
        return self.__nom
    def getVie(self):
        return self.__vie
    def getListeArme(self):
        return self.__listeArme
    def getListeObjet(self):
        return self.__listeObjet
    def getArmeEnMain(self):
        return self.__armeEnMain

    def ajouterObjet(self,Obj):
        self.__listeObjet.append(Obj)

    def ajouterArme(self,Arme):
        if len(self.__listeArme) >= 5:
            return None
        else:
            self.__listeArme.append(Arme)

    def choisirArme(self,Choix):
        for i in range(0,len(self.__listeArme)):
            if str.lower(Choix) == str.lower(self.__listeArme[i].getNomE()):
                self.__armeEnMain = self.__listeArme[i]

    def used(self,Obj):
        if Obj in self.__listeObjet:
            messagebox.showinfo("","Vous avez utilisé l'objet : "+str(Obj.getNomO())+" vous obtenez "+str(Obj.getSoin())+" points de vie")
            self.__vie += Obj.getSoin()
            self.__listeObjet.remove(Obj)

    def attacked(self,Guerrier):
        arme = Guerrier.__armeEnMain
        degats = arme.getAtk()

        if str.lower(Guerrier.getNomG()) == "lannister" and str.lower(arme.getNomE()) == "durandal":
            degats *= 2
        if str.lower(Guerrier.getNomG()) == "conan" and str.lower(arme.getNomE()) == "excalibur":
            degats *= 2
        criticalHit = randrange(0,5)
        if criticalHit == 0 and str.lower(Guerrier.getNomG()) != "méchant":
            messagebox.showinfo("Woah !","Vous attaquez l'ennemi sur un point critique : x3 dégats infligés")
            degats *= 3

        if degats < self.__vie:
            self.__vie -= degats
        else:
            self.__vie = 0
        return degats

    def __str__(self):
        text = ""
        if self.__armeEnMain == "":
            text = "Le guerrier : "+self.__nom+" a un niveau de vie de "+str(self.__vie)
            if self.__vie <= 10 and self.__vie > 0:
                text += " (critique)"
            if self.__vie == 0:
                text = "Le guerrier : "+self.__nom+" est mort"
        else:
            if self.__vie <= 10 and self.__vie > 0:
                text = "Le guerrier : "+self.__nom+" a un niveau de vie de "+str(self.__vie) +" (critique) et a "+str(self.__armeEnMain)+" d'équipée"
            elif self.__vie == 0:
                text = "Le guerrier : "+self.__nom+" est mort"
            else:
                text = "Le guerrier : "+self.__nom+" a un niveau de vie de "+str(self.__vie)+" et a "+str(self.__armeEnMain)+" d'équipée"
        return text