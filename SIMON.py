from tkinter import*
from random import*
from tkinter import messagebox

listUser = []
listOrdi = []
speed = 1250 # normal
parties = 0
points = 0
highScore = 0
couleur = 0
visuEnCours = True
firstTry = True

def gestionTempo():
    global labelOrdi, couleur, visuEnCours
    if visuEnCours ==True:
        maxi = len(listOrdi)
        if couleur == 0:
            labelOrdi.config(bg=listOrdi[0])
            labelCount.config(bg=listOrdi[0],text=str(couleur))
            quitter.config(bg=listOrdi[0])
            labelScore.config(text = "Score : "+str(points), bg = listOrdi[0])
            labelHighScore.config(text = "Record : "+str(highScore), bg = listOrdi[0])
            labelParties.config(text = "Parties : "+str(parties), bg = listOrdi[0])
            couleur += 1
        elif couleur < maxi:
            labelOrdi.config(bg=listOrdi[couleur])
            labelCount.config(bg=listOrdi[couleur],text=str(couleur))
            quitter.config(bg=listOrdi[couleur])
            labelScore.config(text = "Score : "+str(points), bg = listOrdi[couleur])
            labelHighScore.config(text = "Record : "+str(highScore), bg = listOrdi[couleur])
            labelParties.config(text = "Parties : "+str(parties), bg = listOrdi[couleur])
            couleur += 1
        elif couleur == maxi:
            visuEnCours = False
            valider.config(state=NORMAL)
            labelOrdi.config(bg="black")
            labelCount.config(text="-", bg="lightgrey")
            quitter.config(bg="red")
            labelScore.config(text = "Score : "+str(points), bg ="lightgrey")
            labelHighScore.config(text = "Record : "+str(highScore), bg ="lightgrey")
            labelParties.config(text = "Parties : "+str(parties), bg ="lightgrey")
    SIMON.after(speed,gestionTempo)

def ajouterUneCouleur():
    randomNumber = randint(1,4)
    if randomNumber == 1:
        randomColor="red"
    if randomNumber == 2:
        randomColor="blue"
    if randomNumber == 3:
        randomColor="green"
    if randomNumber == 4:
        randomColor="yellow"
    listOrdi.append(randomColor)
    print("Ordi : "+ str(listOrdi))

def validation():
    global points, listUser, listOrdi, couleur, buttonCommencer, visuEnCours, highScore
    if listOrdi == listUser:
        messagebox.showinfo("Bien joué","Vous avez répété la séquence correctement")
        listUser = []
        annuler.config(state = DISABLED)
        valider.config(state = DISABLED)
        print("User : "+ str(listUser))
        ajouterUneCouleur()
        points += 1
        if points > highScore:
            highScore = points
            labelHighScore.config(text="Record : "+str(highScore))
        labelScore.config(text = "Score : "+str(points), bg ="lightgrey")
        couleur = 0
        visuEnCours = True
    else:
        highScore = points
        labelScore.config(text = "Score : 0", bg ="lightgrey")
        messagebox.showinfo("Perdu","Vous n'avez pas réussi à répéter la séquence correctement, vous avez marqué "+str(points)+" points")
        points = 0
        listOrdi = []
        listUser = []
        red.config(state=DISABLED)
        blue.config(state=DISABLED)
        green.config(state=DISABLED)
        yellow.config(state=DISABLED)
        buttonCommencer.config(state=NORMAL)
        valider.config(state = DISABLED)
        annuler.config(state = DISABLED)
        print("User : "+ str(listUser))
        couleur = 0

def commencer():
    global buttonCommencer, red, blue, green, yellow, visuEnCours, firstTry, parties, labelParties
    visuEnCours = True
    parties+=1
    labelParties.config(text= "Parties : "+str(parties))
    red.config(state=NORMAL)
    blue.config(state=NORMAL)
    green.config(state=NORMAL)
    yellow.config(state=NORMAL)
    ajouterUneCouleur()
    if firstTry == True:
        firstTry = False
        gestionTempo()
    buttonCommencer.config(state=DISABLED)

def annulation():
    del listUser[-1]
    print("User : " + str(listUser))
    if listUser == []:
        annuler.config(state = DISABLED)

def addRed():
    listUser.append("red")
    print("User : " + str(listUser))
    annuler.config(state = NORMAL)

def addBlue():
    listUser.append("blue")
    print("User : " + str(listUser))
    annuler.config(state = NORMAL)

def addGreen():
    listUser.append("green")
    print("User : " + str(listUser))
    annuler.config(state = NORMAL)

def addYellow():
    listUser.append("yellow")
    print("User : " + str(listUser))
    annuler.config(state = NORMAL)

def goEz():
    global speed
    speed = 1250

def goNormal():
    global speed
    speed = 1000

def goHard():
    global speed
    speed = 750

SIMON = Tk()
SIMON.title("SIMON")
SIMON.geometry("1000x600")
SIMON.config(bg = "lightgrey")

red = Button(text = "", bg = "red", activebackground="red" , height=5, width=12, command = addRed, state=DISABLED)
red.place(x=150,y=200)

blue = Button(text = "", bg = "blue", activebackground="blue" , height=5, width=12, command = addBlue, state=DISABLED)
blue.place(x=150,y=290)

green = Button(text = "", bg = "green", activebackground="green" , height=5, width=12, command = addGreen, state=DISABLED)
green.place(x=50,y=200)

yellow = Button(text = "", bg = "yellow", activebackground="yellow" , height=5, width=12, command = addYellow, state=DISABLED)
yellow.place(x=50,y=290)

annuler = Button(text = "Annuler", command = annulation, state = DISABLED)
annuler.place(x=300,y=250)

valider = Button(text = "Valider", command = validation, state=DISABLED)
valider.place(x=400,y=250)

quitter = Button(text = "Quitter", fg = "white", bg = "red", command = SIMON.destroy)
quitter.place(x=940,y=560)

labelCount = Label(text = "0", bg = "lightgrey", fg = "black")
labelCount.place(x=667.5,y=150)

labelParties = Label(text = "Parties : 0", bg ="lightgrey", fg = "black")
labelParties.place(x=645,y=50)

labelHighScore = Label(text = "Record : 0", bg ="lightgrey", fg = "black")
labelHighScore.place(x=645,y=75)

labelScore = Label(text = "Score : 0", bg ="lightgrey", fg = "black")
labelScore.place(x=650,y=100)

labelOrdi = Label(text = None, bg = "black", width = 20, height = 10)
labelOrdi.place(x=600,y=200)

buttonCommencer = Button(text = "Commencer", command = commencer)
buttonCommencer.place(x=635,y=400)

ez = Button(text="Facile", bg="green", activebackground="green", command= goEz)
ez.place(x=70,y=510)

normal = Button(text="Normal", bg="orange", activebackground="orange", command= goNormal)
normal.place(x=120,y=510)

hard = Button(text="Difficile", bg="red", activebackground="red", command= goHard)
hard.place(x=170,y=510)

SIMON.mainloop()

SIMON.after(speed,gestionTempo)