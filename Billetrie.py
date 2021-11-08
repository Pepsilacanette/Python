import math
import decimal

def billet():
    nbra = 0
    nbrtr = 0
    totaldest = 0
    départaff = 0
    départ = 0

    stations = {
        "0) Meinohama": 1.5,
        "1) Muromi": 0.8,
        "2) Fujisaki": 1.1,
        "3) Nishijin": 1.2,
        "4) Tojinmachi": 0.8,
        "5) Ohorikoen (Ohori Park)": 1.1,
        "6) Akasaka": 0.8,
        "7) Tenjin": 0.8,
        "8) Nakasu-Kawabata": 1.0,
        "9) Gion": 0.7,
        "10) Hakata": 1.2,
        "11) Higashi-Hie": 2.1,
        "12) Fukuokakuko (Airport)": 0.0,
    }

    nom_des_stations = list(stations.keys())
    distance_stations = list(stations.values())

    print("Bienvenue sur le terminal du métro de Fukuoka\n")

    chx1 = int(input("Désirez vous acheter des billets adultes ? 1)Oui 2)Non -->"))
     

    if chx1 == 1:
        nbra = int(input("\nCombien de tickets souhaitez vous acheter -->"))



    chx2 = int(input("\nDésirez vous acheter des billets à tarif réduit ? 1)Oui 2)Non -->"))


    if chx2 == 1:
        nbrtr = int(input("\nCombien de tickets souhaitez vous acheter ?"))





    print(nom_des_stations)

    départ = int(input("Où voulez vous partir -->"))

    print (nom_des_stations[départ])

    destination = int(input("Où voulez vous aller -->"))
     
    print (nom_des_stations[destination])

    if départ != destination :
        
        while not départ == destination :
            if départ < destination :
                totaldest += distance_stations[départ]
                départ = départ + 1
            if départ > destination :
                totaldest += distance_stations[départ]
                départ = départ - 1

        if totaldest < 3 :

            prixa = nbra * 210
            prixtr = nbrtr * 110

        if 3 < totaldest < 7 :

            prixa = nbra * 260
            prixtr = nbrtr * 130

        if 7 < totaldest < 11 :

            prixa = nbra * 300
            prixtr = nbrtr * 150

        if 11 < totaldest :

            prixa = nbra * 340
            prixtr = nbrtr * 170

        prixtotal = prixa + prixtr

        sens = ""

        if départaff < destination :
            sens = "voie 1"
        if départaff > destination :
            sens = "voie 2"

        print ("Vous avez achetez", nbra, "billet(s) adulte(s) et", nbrtr, "billet(s) à tarif réduit. Vous devez payer au total", prixtotal, "Vous partirez de", nom_des_stations[départaff], "pour aller à", nom_des_stations[destination], ". Vous devrez aller à la", sens, "pour prendre le métro")
    else :
        print("Erreur, veuillez relancer le programme")
        return billet()

    print (prixtotal)


    totaldest = decimal.Decimal(totaldest)
    print(round(totaldest,2))

billet()
