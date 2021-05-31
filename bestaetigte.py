from tkinter import *
from datenbank import *
import os


class Bestaetigte(Button):

    def uebersicht(self, daten_neu):

        class MeinButton(Button):

            def aktionabbrechen(self):
                '''
                schließe das Fenster
                '''
                fenster.destroy()

            def prozent(self):
                '''
                Ermittelt den Zuwachs der aktuellen Fälle in Prozent der jeweiligen Tage und füget diesen der Ansicht hinzu.
                :return: Liste mit Wert für jeden Tag
                '''
                wert = [0]
                for item in range(1,7):
                    wert.append(round(((daten_neu[item][2] - daten_neu[item-1][2]) / daten_neu[item-1][2])*100,2))

                return wert

        fenster = Tk()
        fenster.geometry("600x350")
        fenster.title("Bestätigte Fälle")
        fenster.config(background="white")
        rahmen = Frame(fenster, relief="flat", borderwidth=5, bg="white")
        rahmen.pack(fill="both", expand=1)

        label = Label(rahmen, text="Bestätigte Fälle:")
        label.config(font=("Arial", 14, "bold"))
        label.pack(pady=10)


        rahmen_anzeige = Frame(rahmen, relief="flat", borderwidth=1)
        rahmen_anzeige.pack(pady = 10, padx = 10)
        #scrollbar = Scrollbar(rahmen_anzeige)


        prozent = MeinButton().prozent()


        label_1 = Label(fenster,
                        text=f'''|           Datum:        |    Bestätigte Fälle:  |  Zuwachs der aktuellen Fälle in Prozent:  |\n''')
        label_1.config(font=("Arial", 10, "bold"), fg="Blue", bg="white")
        label_1.place(x=30, y=80)

        i = 0
        for item in range(0, 7):

            label_2 = Label(fenster, text=f'''|      "{daten_neu[item][0]}"           |           "{daten_neu[item][2]}"            |                      {prozent[item]}%           ''')
            label_2.config(font=("Arial", 9), fg="Green", bg="white")
            label_2.place(x=30, y=(100 + i))
            i += 20


        abbrechbutton = MeinButton(rahmen, text="abbrechen")
        abbrechbutton["command"]= abbrechbutton.aktionabbrechen
        abbrechbutton.place(x=260, y=280)


        fenster.mainloop()

