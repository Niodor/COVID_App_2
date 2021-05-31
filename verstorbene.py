from tkinter import *
from datenbank import *


class Verstorbene(Button):

    def uebersicht(self, daten_neu):

        class MeinButton(Button):

            def aktionabbrechen(self):
                '''
                schließe das Fenster
                '''
                fenster.destroy()


        fenster = Tk()
        fenster.geometry("500x400")
        fenster.title("Personen die an oder mit Corona gestorben sind")
        rahmen = Frame(fenster, relief="flat", borderwidth=5, bg="white")
        rahmen.pack(fill="both", expand=1)

        label = Label(rahmen, text="Verstorbene:")
        label.config(font=("Arial", 14, "bold"))
        label.pack(pady=10)


        rahmen_anzeige = Frame(rahmen, relief="flat", borderwidth=1)
        rahmen_anzeige.pack(pady = 10, padx = 10)


        label_1 = Label(fenster,
                        text=f'''|           Datum:        |    Verstorbene Fälle:  |''')
        label_1.config(font=("Arial", 10, "bold"), fg="Blue", bg="white")
        label_1.place(x=120, y=80)

        i = 0
        for item in range(0, 7):

            label_2 = Label(fenster, text=f'''|        "{daten_neu[item][0]}"         |              "{daten_neu[item][4]}"''')
            label_2.config(font=("Arial", 9), fg="Red", bg="white")
            label_2.place(x=120, y=(100 + i))
            i += 20

        abbrechbutton = MeinButton(rahmen, text="abbrechen")
        abbrechbutton["command"]= abbrechbutton.aktionabbrechen
        abbrechbutton.place(x=200, y=260)


        fenster.mainloop()

