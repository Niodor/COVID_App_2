from tkinter import *
from datenbank import *


class Genesene(Button):

    def uebersicht(self, daten_neu):

        class MeinButton(Button):

            def aktionabbrechen(self):
                '''
                schließe das Fenster
                '''
                fenster.destroy()

            def prozent_genesen(self):
                '''
                Gibt an wieviel Prozent der Bevölkerung des Landes zum aktuellen Zeitpunkt genesen sind
                :return: List
                '''
                wert = [0]
                for item in range(1, 7):
                    wert.append(round(daten_neu[item][3]/83149300,3))

                return wert

        fenster = Tk()
        fenster.geometry("600x350")
        fenster.title("Genesene Personen")
        rahmen = Frame(fenster, relief="flat", borderwidth=5, bg="white")
        rahmen.pack(fill="both", expand=1)

        label = Label(rahmen, text="Genesene Personen:")
        label.config(font=("Arial", 14, "bold"))
        label.pack(pady=10)


        rahmen_anzeige = Frame(rahmen, relief="flat", borderwidth=1)
        rahmen_anzeige.pack(pady = 10, padx = 10)


        prozent_gen = MeinButton().prozent_genesen()

        label_1 = Label(fenster,
                        text=f'''|           Datum:        |    Genesene Fälle:  |    Fälle in Prozent:  |\n''')
        label_1.config(font=("Arial", 10, "bold"), fg="Blue", bg="white")
        label_1.place(x=30, y=80)

        i = 0
        for item in range(0, 7):

            label_2 = Label(fenster, text=f'''|      "{daten_neu[item][0]}"           |           "{daten_neu[item][3]}"            |                      {prozent_gen[item]}''')

            label_2.config(font=("Arial", 9), fg="Green", bg="white")
            label_2.place(x=30, y=(100 + i))
            i += 20

        abbrechbutton = MeinButton(rahmen, text="abbrechen")
        abbrechbutton["command"]= abbrechbutton.aktionabbrechen
        abbrechbutton.place(x=260, y=260)


        fenster.mainloop()

