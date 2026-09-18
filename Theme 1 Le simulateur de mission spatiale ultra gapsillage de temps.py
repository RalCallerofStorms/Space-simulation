import time
import random
print("Pour utiliser la fonction Compteur_de_ressources, on a des valeurs pour oxygene, nourriture, eau, minimum_critique, distance_traj, taux de consommation d'oxygène, taux de consommation de nourriture, taux de consommation d'eau, carburant, consommation de carburant, thrust, poid de nourriture(1par défaut), poid d'eau(1 par défaut), poid d'oxygène(1 par défaut), volume du vaisseau, constante gravitationelle(9.80665 par défaut)")
def Compteur_de_ressources(oxygene, nourriture, eau, minimum_critique, distance_traj, tdc_ox, tdc_nr, tdc_H2O, carburant, cons_car, thrust, volume_vaiss, poidn=1, poide=1, poido=1, const_grav=9.80665):
    compteur=0
    vitesse=0
    accel=0
    poid_total= poidn+poide+poido
    mass=poid_total/const_grav
    density=mass/volume_vaiss
    force_app=thrust*mass
    if thrust<=0:
        print("thrust ne peut pas etre <0 ou 0, reseeyer")
        thrust=int(input())
    carburant=carburant * (mass/thrust)
    if carburant==0 or carburant <=0 or carburant >0 and carburant <=1:
        return "Le vaisseau ne pouvait meme pas decoller entierement."
    while oxygene>=0 and nourriture>=0 and eau>=0 or distance_traj==0:
        accel=force_app/mass
        carburant=carburant-cons_car
        



        distance_traj=distance_traj-vitesse
        vitesse=vitesse+accel
        
        oxygene=oxygene-tdc_ox
        nourriture=nourriture-tdc_nr
        eau=eau-tdc_H2O
        compteur=compteur+1
        if oxygene<0:
            oxygene=0
        if nourriture<0:
            nourriture=0
        if eau<0:
            eau=0
        if distance_traj<0:
            distance_traj=0
        print("niveau carburant=", carburant)
        print("vitesse=", vitesse)
        print("niveau eau=", eau)
        print("niveau nourriture=", nourriture)
        print("niveau oxygene=", oxygene)
        print("distance restante=", distance_traj)
        print("niveau carburant=", carburant)
        time.sleep(0)
        if oxygene<=minimum_critique:
            print("Niveau d'oxygene bas")
            time.sleep(2)
        if eau<=minimum_critique:
            print("Niveau d'eau bas")
            time.sleep(2)
        if nourriture<=minimum_critique:
            print("Niveau de nourriture bas")
        if carburant<=minimum<critique:
            print("Niveau de carburant bas")
            time.sleep(2)
        print("Jour ", compteur)
        print()
        if oxygene==0 or nourriture==0 or eau==0:
            return ("L'equipage est mort jour", compteur)      
        if distance_traj==0:
            return ("L'equipage est arrivee a leurs destination le jour", compteur)


def Compteur_de_ressources_instantanee(oxygene, nourriture, eau, minimum_critique, distance_traj, vitesse, tdc_ox, tdc_nr, tdc_H2O):
    compteur=0
    while oxygene>0 and nourriture>0 and eau>0 or distance_traj==0:
        distance_traj=distance_traj-vitesse
        oxygene=oxygene-tdc_ox
        nourriture=nourriture-tdc_nr
        eau=eau-tdc_H2O
        compteur=compteur+1
        if oxygene<0:
            oxygene=0
        if nourriture<0:
            nourriture=0
        if eau<0:
            eau=0
        if distance_traj<0:
            distance_traj=0
        if oxygene==0:
            return("Il y manquera de l'oxygene pour le trajet jour", compteur)
        if nourriture==0:
            return("Il y manquera de la nourriture pour le trajet jour", compteur)
        if eau==0:
            return("Il y manquera de l'eau pour le trajet jour", compteur)
        if distance_traj==0:
            return ("Le trajet sera complétée le jour", compteur)

