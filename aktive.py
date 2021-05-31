from tkinter import *
from datenbank import *
from tkinter import messagebox


class Aktive(Button):

    def uebersicht(self, daten_neu):

        class MeinButton(Button):

            def aktionabbrechen(self):
                '''
                schließe das Fenster
                '''
                fenster.destroy()

            def infiziertProzent(self):
                '''
                Kalkuliert Prozent des Landes aktuell infiziert sind
                :return: List
                '''
                wert = []
                for item in range(0, 7):
                    wert.append(round((daten_neu[item][1]/83149300)*100,2))
                return wert


        fenster = Tk()
        fenster.geometry("600x400")
        fenster.title("Aktive Fälle")
        rahmen = Frame(fenster, relief="flat", borderwidth=5, bg="white")
        rahmen.pack(fill="both", expand=1)

        label = Label(rahmen, text="Aktive Fälle:")
        label.config(font=("Arial", 14, "bold"))
        label.pack(pady=10)


        rahmen_anzeige = Frame(rahmen, relief="flat", borderwidth=1)
        rahmen_anzeige.pack(pady = 10, padx = 10)
        scrollbar = Scrollbar(rahmen_anzeige)


        prozent = MeinButton().infiziertProzent()

        label_1 = Label(fenster,
                        text=f'''|           Datum:        |    Aktive Fälle:  |  Aktuell infiziert % des Landes:  |\n''')
        label_1.config(font=("Arial", 10, "bold"), fg="Blue", bg="white")
        label_1.place(x=90, y=80)

        i = 0
        for item in range(0, 7):

            label_2 = Label(fenster, text=f'''|      "{daten_neu[item][0]}"         |           "{daten_neu[item][1]}"          |               "{prozent[item]}" ''')
            label_2.config(font=("Arial", 9), fg="Green", bg="white")
            label_2.place(x=90, y=(100 + i))
            i += 20

            if prozent[item] > 0.01:

                messagebox.showwarning(message=f'''!!! Hohes Infektionsrisiko fuer Tag: {daten_neu[item][0]} !!!''', title="Warnung")
            else:
                continue


        abbrechbutton = MeinButton(rahmen, text="abbrechen")
        abbrechbutton["command"]= abbrechbutton.aktionabbrechen
        abbrechbutton.place(x=260, y=260)

        fenster.mainloop()






