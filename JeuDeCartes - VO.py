#Question 5 - Devoir 4
# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random


def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
     
     donneur=[]
     autre=[]


     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     for joueur in range(len(p)):
         if joueur % 2==1:
             donneur.append(p[joueur])
         else:
             autre.append(p[joueur])
     
     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat=[]


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    v = []
    for y in l:
        f = y.strip(y[len(y)-1])
        v.append(f)
    verif = []
    for i in range(len(v)):
        nbCartes = v.count(v[i])
        if nbCartes%2==1 and (v[i] not in verif):
            resultat.append(l[i])
        if v[i] not in verif:
            verif.append(v[i])

    
    
    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    for carte in p:
        print(carte,end=' ')
    print()

    

def entrez_position_valide(n):
     '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
     '''

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     entier = 0
     while entier < 1 or entier > n:
         entier = int(input("SVP entrez un entier de 1 à "+str(n)+": "))

     return entier
     

def joue():
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     tour = 0
     while (len(donneur) != 0) and (len(humain) != 0):
         print("***********************************************************")
         if tour % 2==0:
             print("Votre tour.\nVotre main est:")
             affiche_cartes(humain)
             print("J'ai",len(donneur),"cartes. Si 1 est la position de ma première carte et\n",len(donneur),"la position de ma dernière carte, laquelle de mes cartes voulez-vous?")
             choixJ = entrez_position_valide(len(donneur))
             print("Vous avez demandé ma "+str(choixJ)+"e carte.")
             print("Le voilà. C'est un",donneur[choixJ-1])
             
             humain.append(donneur[choixJ-1])
             print("Avec",donneur[choixJ-1],"votre main est:")
             affiche_cartes(humain)
             
             donneur.remove(donneur[choixJ-1])
             humain=elimine_paires(humain)
             print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main est:")
             affiche_cartes(humain)
             attend_le_joueur()
         else:
             choixO = random.randint(1,len(humain))
             print("Mon tour.\nJ'ai pris votre "+str(choixO)+"e carte")
             donneur.append(humain[choixO-1])
             humain.remove(humain[choixO-1])
             donneur=elimine_paires(donneur)

             attend_le_joueur()
        
         tour += 1

     if len(donneur) == 0:
         print("J'ai terminé toutes les cartes.\nVous avez perdu! Moi, Robot, j'ai gagné.")
     else:
         print("J'ai terminé toutes les cartes.\nFélicitations! Vous, Humain, vous avez gagné.")
    

	 
# programme principale
joue()

