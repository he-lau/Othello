#!/usr/bin/python
# -*- coding: latin-1 -*-

#QUESTIONS


#Question 1

def indice_valide(plateau, indice):
    n = plateau["n"]
    if indice >= 0 and indice <= n-1 :
        return True
    return False

#Question 2

def case_valide(plateau, i, j):
    if indice_valide(plateau, i) and indice_valide(plateau, j):
        return True
    return False

#Question 3

def get_case(plateau, i, j):
    n = plateau["n"]
    assert case_valide(plateau, i, j), "Case invalide." # cLa fonction lèvera une erreur si (i,j) ne correspond pas à une case valide
    return plateau["cases"][i*n+j]  #i => lignes, j => colonnes


#Question 4

def set_case(plateau, i, j, val):
    n = plateau["n"]
    assert case_valide(plateau, i, j)== True and val ==0 or val==1 or val==2, "Case invalide/ valeurs invalide."
    plateau["cases"][i*n+j] = val


#Question 5
def creer_plateau(n):
    assert (n ==4 or n==6 or n==8), "La taille de plateau est invalide."
    cases = []
    i=0
    while i< n*n :         #n*n => nombre de cases totales
        cases.append(0)
        i+=1

                                                    #On cherche à mettre les pions de départ au centre du tableau(cases)
                                                    #On cherche l'indice du milieu du plateau avec la division //2 pour placer les valeurs dans le tableau
                                                    #L'indice maximum d'un plateau => n*n-1, 1ligne => indice max => n-1

    i_milieu_ligne = (n-1)//2
    j_milieu_col = (n-1)//2

    cases[n * i_milieu_ligne + j_milieu_col] = 2
    cases[n * i_milieu_ligne + j_milieu_col + 1] = 1
    cases[n * (i_milieu_ligne + 1) + j_milieu_col] = 1
    cases[n * (i_milieu_ligne + 1) + j_milieu_col + 1] = 2


    partie = {
              "n": n,
              "cases": cases,
             }
    return partie


#Question 6

#Simple

#def afficher_plateau(plateau) :
    # n => longueur d'une ligne
    n = plateau["n"]
    i = 0
    while i < n :
        ligne = ""
        j = 0
        while j < n :
            ligne += str(plateau["cases"][i*n+j]) + "  "
            j+=1
        print(ligne)
        i+=1

#Intermédiaire

def afficher_plateau(plateau) :
    n = plateau["n"]
    i = 0
    while i < n :
        ligne = "*"

        print("*"+"********"*n)
        print("*"+"       *"*n)
        j = 0
        while j < n :
            if plateau["cases"][i*n+j] == 1:
                ligne += '   N   *'
            elif plateau["cases"][i*n+j] == 2:
                ligne += '   B   *'
            else:
                ligne += '       *'
            j+=1
        print(ligne)
        print("*"+"       *"*n)
        i+=1
    print("*"+"********"*n)



#TEST


#Question 1
def test_indice_valide():
    p = creer_plateau(4)
    assert indice_valide(p,3)  # doit retourner True car 3 est valide
    assert not indice_valide(p,-1) # doit retourner False car -1 n'est pas valide
    assert not indice_valide(p,4)  # doit retourner False car 4 n'est pas valide (si 4 cases : 0, 1, 2, 3)
    p = creer_plateau(6)
    assert indice_valide(p,5) # doit retourner True car on a maintenant 6 cases
    assert not indice_valide(p,6)  # doit retourner False  car les indices valides vont de 0 à 5
    p = creer_plateau(8)
    assert indice_valide(p,7)  # doit retourner True car on a maintenant 6 cases
    assert not indice_valide(p,8)  # doit retourner False  car les indices valides vont de 0 à 7 (n-1)



#Question 2
def test_case_valide():
    p = creer_plateau(4)
    assert case_valide(p,0,2) # doit retourner True car (0,2) correspond a des indices valides
    assert not case_valide(p,3,4) # doit retourner False car 4 == len(p) et donc pas un indice valide (len(p)-1)
    assert not case_valide(p,-1,0) # doit retourner False car -1 n'est pas valide
    p = creer_plateau(6)
    assert case_valide(p,5,4)  # doit retourner True car (5,4) correspond a des indices valides
    assert case_valide(p,5,3) # doit retourner True car on a maintenant 6 cases
    assert not case_valide(p,3,6) # doit retourner False car 6 == len(p) et donc pas un indice valide (len(p)-1)
    p = creer_plateau(8)
    assert case_valide(p,7,7)  # doit retourner True car (7,7) correspond a des indices valides
    assert case_valide(p,5,6) # doit retourner True car on a maintenant 8 cases
    assert not case_valide(p,5,8) # doit retourner False car 8 == len(p) et donc pas un indice valide (len(p)-1)


#Question 3
def test_get_case():
    p = creer_plateau(4)
    assert get_case(p,0,0) == 0# retourne 0 (la case est vide) (plateau["cases"][j*n+i])
    assert get_case(p,1,1) == 2# retourne 2 (la case contient un pion blanc)
    assert get_case(p,1,2) == 1# retourne 1 (la case contient un pion noir)
    p = creer_plateau(6)
    assert get_case(p,0,0) == 0  # retourne 0 (la case est vide)
    assert get_case(p,2,2) == 2 # retourne 2 (la case contient un pion blanc)
    assert get_case(p,2,3) == 1 # retourne 1 (la case contient un pion noir)
    p = creer_plateau(8)
    assert get_case(p,0,0) == 0 # retourne 0 (la case est vide)
    assert get_case(p,3,3) == 2 # retourne 2 (la case contient un pion blanc)
    assert get_case(p,3,4) == 1# retourne 1 (la case contient un pion noir)


#Question 4
def test_set_case():
    p = creer_plateau(4)
    set_case(p,0,0,1)
    assert get_case(p,0,0) == 1 # met un pions noir (i.e., met la valeur 1) dans la case (0,0)
    set_case(p,1,2,0)
    assert get_case(p,1,2) == 0 # enlève le pion (i.e., met la valeur 0) dans la case (1,2)


#Question 5
def test_creer_plateau():
    assert creer_plateau(4) == {
                                                    "n": 4,
                                                    "cases": [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0] ,
                                        }
                                                                #retourne un dictionnaire contenant les entrées (couples clés/valeurs) :
                                                                # n : 4
                                                                # cases : [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]

    assert creer_plateau(6) == {

                                                    "n": 6,
                                                    "cases":  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1,
                                                            0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

                                        }

                                                                #retourne un dictionnaire contenant les entrées (couples clés/valeurs) :
                                                                # n : 6
                                                                # cases : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1,
                                                                # 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    assert creer_plateau(8) ==  {

                                                    "n": 8,
                                                    "cases":  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1,
                                                                2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                0, 0, 0, 0, 0, 0, 0, 0],

                                        }


                                                                #retourne un dictionnaire contenant les entrées (couples clés/valeurs) :
                                                                # n : 8
                                                                # cases : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                #0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1,
                                                                #2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                                #0, 0, 0, 0, 0, 0, 0, 0]



#Question 6
def test_afficher_plateau():
    p = creer_plateau(4)
    afficher_plateau(p)
    p = creer_plateau(6)
    afficher_plateau(p)
    p = creer_plateau(8)
    afficher_plateau(p)




#Permet d'executer les fonctions test que si partie1.py est lancer

if __name__ == '__main__':
    test_indice_valide()
    test_case_valide()
    test_get_case()
    test_set_case()
    test_creer_plateau()
    test_afficher_plateau()
