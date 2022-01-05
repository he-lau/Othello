#!/usr/bin/python
# -*- coding: latin-1 -*-

from partie2_bis import * #on importe le module de la partie 2 et de la partie 1
from json import dumps, loads #on importe le module json
import os #on importe  le module pour permettre d'effacer le terminal


def creer_partie(n):
    plateau = creer_plateau(n)
    partie = {
        "joueur" : 1,
        "plateau" : plateau
}
    return partie

def saisie_valide(partie, s):
    if s == "m":
        return True
    s = s.lower()
    if not("a" <= s[0] <= "z" and s[1].isdigit()) and len(s) == 2:
        return False
    i = ord(s[0])-97  # ord("a") == 97, pour que ord(a) = 0 ??? --> ord (s[0]) - 97 = 0
    j = int(s[1])-1 # 1-x = 0 --> x =1
    if not mouvement_valide(partie["plateau"], i, j, partie["joueur"]): #tant que le movement n'est pas valide:
        print("Case non valide!")
        return False
    return True



def effacer_terminal():
    os.system("cls") #Windows
    #os.system("clear") #Linux

def tour_jeu(partie):
    if not joueur_peut_jouer(partie["plateau"], partie["joueur"]):   #si le joueur ne peut pas jouer:
        print("joueur", partie["joueur"], "n'a pas de case disponible pour jouer") #on avertit le joueur qu'il ne peut pas jouer
        partie["joueur"] = pion_adverse(partie["joueur"]) #on change de joueur pour faire avancer le jeu
        return True
    effacer_terminal() #sinon on efface le plateau
    afficher_plateau(partie["plateau"]) #puis on affiche le nouveau plateau
    if partie["joueur"] == 1: #joueur == 1 --> N, joueur == 2 --> B
        print("C'est a votre tour: j1 (N)")
    else:
        print("C'est a votre tour: j2 (B)")
    s = ""
    print("saisir un mouvement valide ou la lettre M pour acceder au menu principal")
    while s == "" or not(saisie_valide(partie, s)): #tant que le joueur ne saisie rien ou que la saisie est invalide:
        s = input() #on demande alors au joueur de saisir une case ou "M"
        s = s.lower()
    if s == "m":
        return False
    i = ord(s[0])-97 #on etablit i et j pour pouvoir effectuer un mouvement
    j = int(s[1])-1
    mouvement(partie["plateau"], i, j, partie["joueur"]) #on effectue alors le mouvement
    partie["joueur"] = pion_adverse(partie["joueur"]) #c'est a l'adversaire de jouer
    return True


def saisir_action(partie=None):
    if partie is None:
        print("saisir le numero d'action souhaite:")
        print("0: terminer le jeu")
        print("1: commencer une nouvelle partie")
        print("2: charger une partie")
        s = int(input())
        while s > 2 or s < 0:
            s = int(input("Veuillez saisir seulement le numero."))
    else:
        print("saisir le numero d'action souhaite:")
        print("0: terminer le jeu")
        print("1: commencer une nouvelle partie")
        print("2: charger une partie")
        print("3: sauvegarder la partie en cours")
        print("4: reprendre la partie en cours")
        s = int(input())
        while s > 4 or s < 0:
            s = int(input("Veuillez saisir un numero valide svp."))
    return s



def jouer(partie):
    while not fin_de_partie(partie["plateau"]): #tant que la partie n'est pas fini
        if not tour_jeu(partie): #si le joueur ne peut pas jouer:
            return False
    return True


def saisir_taille_plateau():
    print("saisir la taille de plateau : 4, 6, 8")
    n = int(input())
    while n != 4 and n != 6 and n != 8:
        n = int(input())
    return n


def sauvegarder_partie(partie):
    partie = dumps(partie) # la variable partie est une chaine de caracteres contenant les informations de partie
    f = open("sauvegarde_partie.json", "w") #on ouvre le fichier sauvegarde_partie.json en mode "write"
    f.write(partie)# On ecrit dans le fichier la chaine contenant toutes les informations
    f.close()# On ferme le fichier


def charger_partie():
    if os.path.exists("sauvegarde_partie.json"): #si le fichier "sauvegarde_partie.json" existe:

        f = open("sauvegarde_partie.json", "r") #on ouvre le fichier sauvegarde_partie.json en mode "read"
        partie = f.read()

        partie = loads(partie) #partie est une variable contenant les informations de partie.
    else: #sinon le fichier n'existe pas (pas de sauvegarde)
        print("pas de partie disponible, creer une nouvelle partie")
        n = saisir_taille_plateau()
        partie = creer_partie(n) 
    return partie


def othello():
    action = saisir_action() #action est une valeur correspondant au chiffre saisie par le joueur
    if action == 0: #si 0: on arrête la partie
        return
    elif action == 1: #si 1: on créer une nouvelle partie
        n = saisir_taille_plateau()
        partie = creer_partie(n)
    elif action == 2: #si 2: on charge une partie sauvegardée
        partie = charger_partie()

    while True: #tant que la partie n'est pas fini:
        a = jouer(partie) #la partie continue
        if not a: #tant que jouer(partie) ne renvoie pas False: (lejoueur souhaite acceder au menu)
            action = saisir_action(partie) #on demande au joueur de saisir une action
            if action == 0:
                return
            elif action == 1:
                n = saisir_taille_plateau()
                partie = creer_partie(n)
                continue
            elif action == 2:
                partie = charger_partie()
                continue
            elif action == 3:
                sauvegarder_partie(partie)
                return
            elif action == 4:
                continue

        else: #sinon la partie est finie:
            n = gagnant(partie["plateau"])
            if n == 1: #si gagnant retourne 1:
                print("joueur 1 (N) a gagné") #j1 win
            elif n == 2: #si gagnant retourne 2:
                print("joueur 2 (B) a gagné") #j2 win
            else: #sinon:
                print("match nul") #draw
            return #on arrête alors le jeu



def test_creer_partie():
    assert creer_partie(4) =={
                                    "joueur" : 1,
                                    "plateau" : {
                                                    "n": 4,
                                                    "cases": [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0] ,
                                                }
                                            }
    assert creer_partie(6) =={
                                    "joueur" : 1,
                                    "plateau" : {
                                                    "n": 6,
                                                    "cases":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1,
                                                            0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                }
                                            }
    assert creer_partie(8) =={
                                    "joueur" : 1,
                                    "plateau" : {
                                                    "n": 8,
                                                    "cases": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1,
                                                                 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                    0, 0, 0, 0, 0, 0, 0, 0],
                                                }
                                            }


def test_saisie_valide():

    p = creer_partie(4)
    assert saisie_valide(p,"m") # retourne True
    assert saisie_valide(p,"b1")  # retourne True
    assert not saisie_valide(p,"b4") # return False
    print("test_saisie_valide():  validé! (4)")

    p = creer_partie(6)
    assert saisie_valide(p, "m") # retourne True
    assert saisie_valide(p, "c2") # retourne True
    assert not saisie_valide(p, "f6")  # return False
    print("test_saisie_valide():  validé! (6)")

    p = creer_partie(8)
    assert saisie_valide(p, "m") # retourne True
    assert saisie_valide(p, "d3") # retourne True
    assert not saisie_valide(p, "h9") # return False
    print("test_saisie_valide():  validé! (8)")




def test_tour_jeu():
    partie = creer_partie(4)
    plateau = partie["plateau"]
    tour_jeu(partie) # Comme le joueur 1 (N) a joué le plateau a donc était modifié est ne correspond plus a: [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]
    assert not partie =={
                        "joueur" : 1,
                        "plateau" : {
                        "n" : 4,
                        "cases" : [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]
                                    }
                            }


def test_saisir_action():
    print("Ceci est un test:")
    n = saisir_action(None)
    assert n>0 or n<=2 #n est un entier compris entre 0 et 2 inclus.
    print("Ceci est un test:")
    partie = creer_partie(4)
    n = saisir_action(partie) #n est un entier compris entre 0 et 4 inclus.
    assert n>0 or n<=4

def test_jouer():
    p = creer_partie(4)
    plateau = p["plateau"]
    res = jouer(p)
    #Si res vaut True, alors les deux joueurs ont fait une partie entière d'Othello sur une grille 4 * 4.
    assert res

def test_saisir_taille_plateau():
    print("Ceci est un test:")
    n = saisir_taille_plateau()
    assert (n == 4 or n == 6 or n == 8)


def test_sauvegarder_partie():
    p = creer_partie(4)
    sauvegarder_partie(p)
    f = open("sauvegarde_partie.json", "r")
    partie = f.read()
    f.close()
    partie = loads(partie)
    assert partie =={"joueur": 1, "plateau": {"n": 4, "cases": [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0,
0, 0, 0, 0]}}


def test_charger_partie():
    p = charger_partie()

    f = open("sauvegarde_partie.json", "r")
    partie = f.read()
    f.close()
    partie = loads(partie)    # Si le fichier sauvegarde_partie.json contient :
    assert partie =={"joueur": 1, "plateau": {"n": 4, "cases": [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0,
0, 0, 0, 0]}}


def test_othello():
    othello()



if __name__ == '__main__':
    test_creer_partie()
    test_saisie_valide()
    test_tour_jeu()
    test_saisir_action()
    test_jouer()
    test_saisir_taille_plateau()
    test_sauvegarder_partie()
    test_charger_partie()
    test_othello()
