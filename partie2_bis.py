#!/usr/bin/python
# -*- coding: latin-1 -*-

from partie1 import * # On importe toutes les fonctions du module partie1.py

# QUESTIONS


def pion_adverse(n):
    assert n == 1 or n == 2, 'le joueur est différent de 1 et 2.'
    if n == 1:
        return 2
    return 1


def prise_possible_direction(plateau, i, j, vertical, horizontal, joueur):
    if not case_valide(plateau, i, j) or get_case(plateau, i, j) != 0:
        return 0
    nb = 0
    while case_valide(plateau, i, j):  # si la case est valide
        i = i - vertical
        j = j + horizontal  # i, j de la case suivante
        if case_valide(plateau, i, j):  # si la case suivante est toujours valide
            if get_case(plateau, i, j) == pion_adverse(joueur):
                # la case suivante contient pion_adverse
                nb += 1
            else:
                if get_case(plateau, i, j) == joueur:
                    # la case suivante ne contient pas pion_adverse
                    return nb
                else:
                    return 0
                # True si c'est le joueur lui meme et on a trouve un pion adversaire dans cette direction
                # False si la case est libre ou on n'a pas trouve un pion adversaire
    return 0


def mouvement_valide(plateau, i, j, joueur):
    # test pour tous les 8 directions
    nb = 0
    nb += prise_possible_direction(plateau, i, j, 0, -1, joueur)
    nb += prise_possible_direction(plateau, i, j, 1, -1, joueur)
    nb += prise_possible_direction(plateau, i, j, 1, 0, joueur)
    nb += prise_possible_direction(plateau, i, j, 1, 1, joueur)
    nb += prise_possible_direction(plateau, i, j, 0, 1, joueur)
    nb += prise_possible_direction(plateau, i, j, -1, 1, joueur)
    nb += prise_possible_direction(plateau, i, j, -1, 0, joueur)
    nb += prise_possible_direction(plateau, i, j, -1, -1, joueur)
    return nb


def mouvement_direction(plateau, i, j, vertical, horizontal, joueur):
    if prise_possible_direction(plateau, i, j, vertical, horizontal, joueur) == 0:
        # cette direction n'est pas valide
        return
    i = i-vertical
    j = j+horizontal
    while case_valide(plateau, i, j):
        if get_case(plateau, i, j) == joueur:
            # le pion est joueur lui meme, on arrete la fonction
            return
        set_case(plateau, i, j, joueur)
        i = i-vertical
        j = j+horizontal


def mouvement(plateau, i, j, joueur):
    if mouvement_valide(plateau, i, j, joueur) > 0:
        mouvement_direction(plateau, i, j, 0, -1, joueur)
        mouvement_direction(plateau, i, j, 1, -1, joueur)
        mouvement_direction(plateau, i, j, 1, 0, joueur)
        mouvement_direction(plateau, i, j, 1, 1, joueur)
        mouvement_direction(plateau, i, j, 0, 1, joueur)
        mouvement_direction(plateau, i, j, -1, 1, joueur)
        mouvement_direction(plateau, i, j, -1, 0, joueur)
        mouvement_direction(plateau, i, j, -1, -1, joueur)
        set_case(plateau, i, j, joueur)


def joueur_peut_jouer(plateau, joueur):
    n = plateau["n"]
    tab_coord = []
    coord = {"coord": [],
             "nb": 0
             }
    i = 0
    while i < n:
        j = 0
        while j < n:
            nb = mouvement_valide(plateau, i, j, joueur)
            if nb > 0:
                coord["coord"] = [i, j]
                coord["nb"] = nb
                tab_coord.append(coord)
                coord = {"coord": [],
                         "nb": 0
                         }
            j += 1
        i += 1
    if not tab_coord:
        return 0
    return tab_coord


def fin_de_partie(plateau):
    return joueur_peut_jouer(plateau, 1) == 0 and joueur_peut_jouer(plateau, 2) == 0


def gagnant(plateau):
    dico = {
        0: 0,
        1: 0,
        2: 0
    }
    i = 0
    while i < len(plateau["cases"]):
        dico[plateau["cases"][i]] += 1
        i += 1
    if dico[1] > dico[2]:
        return 1
    elif dico[2] > dico[1]:
        return 2
    else:
        return 0



# TEST


# Question 7

def test_pion_adverse():
	assert pion_adverse(1) == 2 # retourne 2
	assert pion_adverse(2) == 1 # retourne 1
	assert not pion_adverse(1) == 1 # lève une erreur

# Question 8

def test_prise_possible_direction():
	p = creer_plateau(4)
	assert prise_possible_direction(p,1,3,0,-1,2) # retourne True
	assert not prise_possible_direction(p,1,3,0,-1,1) # retourne False
	assert not prise_possible_direction(p,1,3,-1,-1,2) # retourne False
	assert prise_possible_direction(p,1,0,0,1,1) # retourne True

# Question 9

def test_mouvement_valide():
	p = creer_plateau(4)
	assert mouvement_valide(p,1,3,2) # retourne True
	assert not mouvement_valide(p,0,0,1) # retourne False

# Question 10

def test_mouvement_direction():
	p = creer_plateau(4) # On créer un plateau de taille 4 initialisé
	mouvement_direction(p,0,3,-1,1,2) # ne modifie rien
	assert get_case(p,0,0) == 0 #On regarde pour chaque case que la valeur n'a pas changé
	assert get_case(p,0,1) == 0
	assert get_case(p,0,2) == 0
	assert get_case(p,0,3) == 0
	assert get_case(p,1,0) == 0
	assert get_case(p,1,1) == 2
	assert get_case(p,1,2) == 1
	assert get_case(p,1,3) == 0
	assert get_case(p,2,0) == 0
	assert get_case(p,2,1) == 1
	assert get_case(p,2,2) == 2
	assert get_case(p,2,3) == 0
	assert get_case(p,3,0) == 0
	assert get_case(p,3,1) == 0
	assert get_case(p,3,2) == 0
	assert get_case(p,3,3) == 0
	mouvement_direction(p,1,3,0,-1,2) # met la valeur 2 dans la case (1,2)
	assert get_case(p,1,2) == 2

# Question 11

def test_mouvement():
	p = creer_plateau(4)
	mouvement(p,1,3,2) 
	assert get_case(p,1,2) == 2
	assert get_case(p,1,1) == 2


# Question 12

def test_joueur_peut_jouer():
	p = creer_plateau(4)
	assert joueur_peut_jouer(p,1) # retourne True
	# On remplace les pions du joueur 2 par des pions du joueur 1
	set_case(p,1,1,1)
	set_case(p,2,2,1)
	assert not joueur_peut_jouer(p,1) # retourne False

# Question 13

def test_fin_de_partie():
	p = creer_plateau(4)
	assert not fin_de_partie(p) # retourne False
	# On remplace les pions du joueur 2 par des pions du joueur 1
	set_case(p,1,1,1)
	set_case(p,2,2,1)
	assert fin_de_partie(p) # retourne True


# Question 14

def test_gagnant():
	p = creer_plateau(4)
	# On remplace les pions du joueur 2 par des pions du joueur 1
	set_case(p,1,1,1)
	set_case(p,2,2,1)
	assert gagnant(p) == 1 # retourne 1



if __name__ == '__main__': #Permet d'executer les fonctions test que si partie1.py est lancer

	test_pion_adverse()
	test_prise_possible_direction()
	test_mouvement_valide()
	test_mouvement_direction()
	test_mouvement()
	test_joueur_peut_jouer()
	test_fin_de_partie()
	test_gagnant()
