import os
import sqlite3
from tkinter import *
import datetime
from datetime import date
import requests


class Daten():


    def daten_holen(self, land):
        '''
        Die Funktion lädt die Daten von der Covid-API herunter.
        Überprüfst auch, ob die Datenbank für gestern bereits verfügbar ist. Falls nicht - das Programm verwendet die Daten ab einem Tag zuvor (vorgestern)
        :return: List
        '''

        ############################### API URL einbauen - START ##################################
        #Corona API handling
        # Beispiel fuer covid_url_complete = "https://api.covid19api.com/country/germany?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z"
        covid_url = "https://api.covid19api.com/country/"   # try/except

        def raw_daten_holen(start_day, end_day):
            '''
            Die Funktion lädt die Daten von der Covid-API herunter.
            :param start_day:
            :param end_day:
            :return: List --> Aufteilung: Datum, AnzahlAktiverfälle, AnzahlbestätigeFälle, Anzahlgenesene,  Anzahlverstorbene
            '''


            # aktuelles datum
            aktuellesDatum = date.today()

            # ziehe vom aktuellen datum 1 tag und 7 tage ab:
            gesterndatum = aktuellesDatum - datetime.timedelta(days=start_day)
            siebentageminusdatum = aktuellesDatum - datetime.timedelta(days=end_day)

            # Umwandlung in String + passendes Format
            string_gesterndatum = gesterndatum.strftime("%Y-%m-%dT%H:%M:%SZ")
            string_siebentageminusdatum = siebentageminusdatum.strftime("%Y-%m-%dT%H:%M:%SZ")

            # Aufteilung in einzelnen Einheiten
            date_from = string_siebentageminusdatum
            date_today = string_gesterndatum
            api_url = covid_url + land + "?from=" + date_from + "&to=" + date_today

            ############################### API URL einbauen - ENDE ##################################

            # Daten holen
            response = requests.get(api_url)
            data = response.json()


            # Aufteilung: Datum, AnzahlAktiverfälle, AnzahlbestätigeFälle, Anzahlgenesene,  Anzahlverstorbene

            daten_all = []
            for item in range(0, 7):
                daten_all.append(
                    [str(data[item]["Date"])[:10], data[item]["Active"], data[item]["Confirmed"],
                     data[item]["Recovered"], data[item]["Deaths"]])

            return daten_all


        # Überprüfung:
        try:
            #if die Datenbank für gestern bereits verfügbar ist
            daten_all = raw_daten_holen(1,7)

        except:
            # sonst benutzt die Daten ab einem Tag zuvor (vorgestern)
            daten_all = raw_daten_holen(2,8)

        return daten_all

# def country():
#     lande = ["germany", "spain", "italy"]
#     index = int(input("Welche Land moechten Sie?: 0: DE, 1: SP, 2: IT "))
#     land = lande[index]
#     print("Land:", land)
#     return land

# land = country()
# daten_all = Daten()
# daten_neu = daten_all.daten_holen(land)
# print(daten_neu)


class Datenbank(Button):
    '''

    '''
    def __init__(self):
        self.connection = sqlite3.connect("database.sqlite3")

        try:
            self.erzeugeTabelleInDatenbank()
        except:
            pass


    def erzeugeTabelleInDatenbank(self):
        '''
        Erstellt DB für CoronaDaten
         Aufteilung: Datum, AnzahlAktiverfälle, AnzahlbestätigeFälle, Anzahlgenesene,  Anzahlverstorbene
        '''



        cursor = self.connection.cursor()
        neue_tabelle = f'''
            CREATE TABLE coronadaten (
                nummer INTEGER PRIMARY KEY,
                land VARCHAR(200),
                datum VARCHAR(200),
                anzahlaktiverfälle VARCHAR(200),
                anzahlbestätigeFälle VARCHAR(200),
                anzahlgeneseneFälle VARCHAR(200),
                anzahlverstorbene VARCHAR(200));
        '''
        cursor.execute(neue_tabelle)
        self.connection.commit()


    def datenvonapizudatenbank(self, land, daten_neu):


        for item in range(0, 7):
            cursor = self.connection.cursor()
            einfuegen = f'''INSERT INTO coronadaten (nummer, land, datum, anzahlaktiverfälle, anzahlbestätigeFälle ,anzahlgeneseneFälle, anzahlverstorbene)
                             VALUES (NULL, "{land}","{daten_neu[item][0]}", "{daten_neu[item][1]}", "{daten_neu[item][2]}", "{daten_neu[item][3]}", "{daten_neu[item][4]}");   
            '''
            cursor.execute(einfuegen)
            self.connection.commit()
            #print(einfuegen)


        print("läuft")

    def holealleDatenausdatenbank(self):

        cursor = self.connection.cursor()
        abfrage = f'''SELECT * FROM coronadaten       '''
        cursor.execute(abfrage)
        daten = cursor.fetchall()
        self.connection.commit()
        return daten


    def loescheProdukte(self, nummer):
        cursor = self.connection.cursor()
        aendern = f'''DELETE FROM coronadaten WHERE datum="{nummer}";'''
        cursor.execute(aendern)
        self.connection.commit()

