import json, http.client
from tkinter import*
from PIL import Image
import time
import webbrowser

temp = ""
placed = False
windDir = ""

def rick():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def iconWeatherPickUp():
    global iconImage,iconWeather
    connexion = http.client.HTTPSConnection('openweathermap.org')
    connexion.request("GET","/img/wn/"+iconWeather+".png")
    rep1 = connexion.getresponse()
    octets = rep1.read()
    f = open('Icon.png','wb')
    f.write(octets)
    f.close()
    iconImage = PhotoImage(file="Icon.png")
    return iconImage


def windNightmare(): #AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
    global windDir
    if (jsonDoc['wind']['deg'] > 348.75 and jsonDoc['wind']['deg'] < 360) and (jsonDoc['wind']['deg'] > 0 and jsonDoc['wind']['deg'] < 11.25) :
        windDir = "le Nord"
    if jsonDoc['wind']['deg'] > 11.25 and jsonDoc['wind']['deg'] < 33.75 :
        windDir = "le Nord/Nord-Est"
    if jsonDoc['wind']['deg'] > 33.75 and jsonDoc['wind']['deg'] < 56.25 :
        windDir ="le Nord-Est"
    if jsonDoc['wind']['deg'] > 56.25 and jsonDoc['wind']['deg'] < 78.75 :
        windDir ="l'Est/Nord-Est"
    if jsonDoc['wind']['deg'] > 78.75 and jsonDoc['wind']['deg'] < 101.25 :
        windDir ="l'Est"
    if jsonDoc['wind']['deg'] > 101.25 and jsonDoc['wind']['deg'] < 123.75 :
        windDir ="l'Est/Sud-Est"
    if jsonDoc['wind']['deg'] > 123.75 and jsonDoc['wind']['deg'] < 146.25 :
        windDir ="le Sud-Est"
    if jsonDoc['wind']['deg'] > 146.25 and jsonDoc['wind']['deg'] < 168.75 :
        windDir ="le Sud/Sud-Est"
    if jsonDoc['wind']['deg'] > 168.75 and jsonDoc['wind']['deg'] < 191.25 :
        windDir ="le Sud"
    if jsonDoc['wind']['deg'] > 191.25 and jsonDoc['wind']['deg'] < 213.75  :
        windDir ="le Sud/Sud-Ouest"
    if jsonDoc['wind']['deg'] > 213.75 and jsonDoc['wind']['deg'] < 236.25 :
        windDir ="le Sud-Ouest"
    if jsonDoc['wind']['deg'] > 236.25 and jsonDoc['wind']['deg'] < 258.75 :
        windDir ="l'Ouest/Sud-Ouest"
    if jsonDoc['wind']['deg'] > 258.75 and jsonDoc['wind']['deg'] < 281.25 :
        windDir ="l'Ouest"
    if jsonDoc['wind']['deg'] > 281.25 and jsonDoc['wind']['deg'] < 303.75 :
        windDir ="l'Ouest/Nord-Ouest"
    if jsonDoc['wind']['deg'] > 303.75 and jsonDoc['wind']['deg'] < 326.25 :
        windDir = "le Nord-Ouest"
    if jsonDoc['wind']['deg'] > 326.25 and jsonDoc['wind']['deg'] < 348.75 :
        windDir = "le Nord/Nord-Ouest"

def labelPlacing():
    global placed
    placed = True
    labelNom.place(x=620,y=40)
    labelTemp.place(x=620,y=70)
    labelCloud.place(x=620,y=100)
    labelWind.place(x=620,y=130)
    labelMain.place(x=620,y=160)
    labelRain.place(x=620,y=190)

def Coords(event):
    global latitude,longitude,placed, windDir, jsonDoc, iconWeather, icon
    print (event.y,event.x)
    if (event.y > 294 and event.y < 0) or (event.x < 0 and event.x > 312): # ??????????????????????????????????????????????????????????????
        print("help")
        return None
    latitude = 51.608952-(event.y*8.6/460)
    longitude = -5.3 + (event.x*12.43/509)
    connexion = http.client.HTTPSConnection('api.openweathermap.org')
    connexion.request("GET", "/data/2.5/weather?lat="+str(latitude)+"&lon="+str(longitude)+"&APPID=e2536f1435cb0d071187d54316b91823&lang=FR")
    rep = connexion.getresponse()
    rep_str=rep.read()
    jsonDoc = json.loads(rep_str.decode('utf-8'))
    iconWeather = jsonDoc["weather"][0]["icon"]
    print(jsonDoc)
    connexion.close()
    iconReturned = iconWeatherPickUp()
    windNightmare()
    labelNom.config(text="Ville : "+str(jsonDoc['name']))
    labelTemp.config(text="Température : "+str(str(int((jsonDoc['main']['temp'])))+"°K / "+str(int((jsonDoc['main']['temp'])-273.15-32/1.8))+"°F / "+str(int((jsonDoc['main']['temp'])-273.15))+"°C"))
    labelCloud.config(text="Nuages : "+str(jsonDoc['weather'][0]['description']))
    labelWind.config(text="Vitesse du vent : "+str(jsonDoc['wind']['speed'])+"m/s vers "+str(windDir))
    labelMain.config(text="Température ressentie : "+str(str(int((jsonDoc['main']['feels_like'])))+"°K / "+str(int((jsonDoc['main']['feels_like'])-273.15-32/1.8))+"°F / "+str(int((jsonDoc['main']['feels_like'])-273.15))+"°C"))
    labelRain.config(text="Pourcentage d'humidité : "+str(jsonDoc['main']['humidity'])+"%")
    ca.delete(icon)
    icon = ca.create_image(event.x,event.y, image=iconReturned)
    if placed == False:
        labelPlacing()


LaM = Tk()
LaM.title("La Météo de France")
LaM.geometry("1000x624")
LaM.config(bg="lightgreen")

imageMap = PhotoImage(file="Images Météo/CarteFrance.png")

ca = Canvas (width=10000,height=10000, bg="lightgreen")
ca.place(x=0,y=0)

boooooooo = Button(command = rick).place(x=585,y=-5)

icon = ca.create_image(620, 200, image=None)
map = ca.create_image(294, 312, image=imageMap)

labelInfos = Label(LaM, text="Informations :", fg="purple", bg="lightgreen",font=30).place(x=620,y=10)
labelNom = Label(LaM, text="", bg="lightgreen",font=30)
labelTemp = Label(LaM, text="", bg="lightgreen",font=30)
labelCloud = Label(LaM, text="", bg="lightgreen",font=30)
labelWind = Label(LaM, text="", bg="lightgreen",font=30)
labelMain = Label(LaM, text="", bg="lightgreen",font=30)
labelRain = Label(LaM, text="", bg="lightgreen",font=30)

LaM.bind("<Button-1>", Coords)
LaM.mainloop()