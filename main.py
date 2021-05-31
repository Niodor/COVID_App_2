
import tkinter
import datetime
from datetime import date
from tkinter import *
from aktive import *
from bestaetigte import *
from verstorbene import *
from genesene import *
from datenbank import *

'''
Corona Anzeige Programm -
Aufgabenstellung: 
Speichern Sie die aktuellen Zahlen der letzten 7 Tage (täglich) der Corona Fälle, 
um Aussagen über die Verbreitung treffen zu können. In der Corona-API https://api.covid19api.com finden Sie 
eine Schnittstelle für JSON Daten, die via Requests abgerufen werden können. 
Weitere Information zu der API: https://covid19api.com/
Die Einwohnerzahl kann als Konstante angesehen werden. Deutschland (83 149 300 Einwohner)
         
         
         
## Userstory I (Prio 1)
Der Arzt Dr. Petersen möchte die Entwicklung von Deuschland im Blick behalten. Zeigen Sie ihm in einer 
Applikationsansicht die Zahlen der letzten 7 Tage für Deutschland an. 
(aktuell infiziert, bestätigte Fälle, Aktive Fälle, genesene Fälle, verstorbene Fälle)
Startfenster: 
Vier Buttons:
Buttons:

    
-	Bestätigte Fälle
    o	Zeige die Zahl der bestätigten Fälle an
    
-	Aktive Fälle
    o	Zeige die Zahl der aktiven Fälle an
    
-	Genesene Fälle
    o	Zeige die Zahl der genesene Fälle an
    
-   verstorbene Fälle
    o	Zeige die Zahl der verstorbenen Fälle an
    

         
'''

#Fenster
#############################
#             #             #
# Aktive      #  Bestätigte #
#             #             #
#############################
#             #             #
# verstorbene #  Genesene   #
#             #             #
#############################



#Fenster erzeugen
fenster = Tk()
fenster.geometry("800x550")
fenster.title("Corona Daten - Übersicht ")
rahmen = Frame(fenster, relief="flat", borderwidth=5, bg = "white")
rahmen.pack(fill="both", expand = 1)


imgfile = PhotoImage( file = (os.getcwd() + '\\unnamed.png') )
backgroundimg   = Label(rahmen, image = imgfile)
backgroundimg.image = imgfile
backgroundimg.place(x = 0, y = 0)

label = Label(rahmen, text="Corona API")
label.config(font=("Arial", 14, "bold"))
label.pack(pady=10)


# #button COUNTRY
def ok():

    global daten_neu
    global ausgewaehltesland
    ausgewaehltesland = variable.get()
    daten_all = Daten()
    daten_neu = daten_all.daten_holen(ausgewaehltesland)

    print(ausgewaehltesland)

daten_all = Daten()
daten_neu = daten_all.daten_holen("germany")

auswahllist = [
    "germany",
    "italy",
    "spain",
    ]

#Button Auswahl Land
button_auswahl = Button(rahmen, text="Bestätigung", width=10, height= 1)

#Anzeige Auswahl Länder
variable = StringVar(fenster)
variable.set(auswahllist[0])  # default value

w = OptionMenu(rahmen, variable, *auswahllist )
w.place(x=380, y=350)

#Anzeige aktuelles Land:
button_auswahl.config(font=("Arial", 10, "bold"))
button_auswahl['command'] = ok
button_auswahl.place(x=500, y=350)


#button aktive
button_aktive = Aktive(rahmen, text="Aktive Fälle", width=20, height= 5)
button_aktive.config(font=("Arial", 12, "bold"))
button_aktive['command'] = lambda: button_aktive.uebersicht(daten_neu)
button_aktive.place(x=50, y=50)

#button bestätigte
button_bestaetigte = Bestaetigte(rahmen, text="Bestaetigte Fälle", width=20, height= 5)
button_bestaetigte.config(font=("Arial", 12, "bold"))
button_bestaetigte['command'] = lambda: button_bestaetigte.uebersicht(daten_neu)
button_bestaetigte.place(x=430, y=50)

#button verstorbene
button_verstorbene = Verstorbene(rahmen, text="Verstorbene Fälle", width=20, height= 5)
button_verstorbene.config(font=("Arial", 12, "bold"))
button_verstorbene['command'] = lambda: button_verstorbene.uebersicht(daten_neu)
button_verstorbene.place(x=50, y=200)

#button genesene
button_genesene = Genesene(rahmen, text="Genesene Fälle", width=20, height= 5)
button_genesene.config(font=("Arial", 12, "bold"))
button_genesene['command'] = lambda: button_genesene.uebersicht(daten_neu)
button_genesene.place(x=430, y=200)

#button datenladen
button_datenladen = Button(rahmen, text="Daten aus API holen", width=15, height= 2)
button_datenladen.config(font=("Arial", 12, "bold"))
datenladen = Datenbank()
button_datenladen['command'] = lambda: datenladen.datenvonapizudatenbank(ausgewaehltesland, daten_neu)

button_datenladen.place(x=20, y=400)


mainloop()