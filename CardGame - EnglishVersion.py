
# Card game called "Pouilleux" 

# The computer is the card dealer.

# A card is a string of 2 characters. 
# The first character represents a value and the second a color.
# Values ​​are characters like '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Colors are characters like : ♠, ♡, ♣, et ♢.
# We use 4 Unicode symbols to represent the 4 suits: spades, hearts, clubs and diamonds.
# For cards of 10 we use 3 characters, because the value '10' uses two characters.

import random


def attend_le_joueur():
    '''()->None
    Pause the program until the user presses Enter
    '''
    try:
         input("Press Enter to continue. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Returns a list of strings representing all cards,
        except the black jack.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # eliminates the black jack (the jack of clubs)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Shuffles the list of character strings representing the deck of cards    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Return two lists that represent the two hands of the cards.
     The dealer gives one card to the other player, one to himself,
     and it continues until the end of packet p.
     '''
     
     donneur=[]
     autre=[]


     
     for joueur in range(len(p)):
         if joueur % 2==1:
             donneur.append(p[joueur])
         else:
             autre.append(p[joueur])
     
     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Returns a copy of list l with all pairs eliminated
     and mix the remaining elements.
     Test:
     (Note that the order of the elements in the result could be different)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat=[]


    
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
    Displays the elements of the list p separated by spaces
    '''


    
    for carte in p:
        print(carte,end=' ')
    print()

    

def entrez_position_valide(n):
     '''
     (int)->int
     Returns an integer from the keyboard, from 1 to n (1 and n included).
     Keep asking if the user enters an integer that is not in the range [1,n]
     
     Précondition: n>=1
     '''

     
     entier = 0
     while entier < 1 or entier > n:
         entier = int(input("Please enter an integer from 1 to "+str(n)+": "))

     return entier
     

def joue():
     '''()->None
     This function plays the game'''
    
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Hello. My name is Robot and I deal the cards.")
     print("Your hand is:")
     affiche_cartes(humain)
     print("Don't worry, I can't see your cards or their order.")
     print("Now discard all pairs from your hand. I will do it too.")
     attend_le_joueur()
     
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     tour = 0
     while (len(donneur) != 0) and (len(humain) != 0):
         print("***********************************************************")
         if tour % 2==0:
             print("Your turn.\nYour hand is:")
             affiche_cartes(humain)
             print("I have",len(donneur),"cards. If 1 is the position of my first card is\n",len(donneur),"the position of my last card, which of my cards do you want?")
             choixJ = entrez_position_valide(len(donneur))
             print("You asked for my "+str(choixJ)+" card.")
             print("Here it is. It is a",donneur[choixJ-1])
             
             humain.append(donneur[choixJ-1])
             print("With",donneur[choixJ-1],"your hand is:")
             affiche_cartes(humain)
             
             donneur.remove(donneur[choixJ-1])
             humain=elimine_paires(humain)
             print("After discarding all pairs and shuffling the cards, your hand is: ")
             affiche_cartes(humain)
             attend_le_joueur()
         else:
             choixO = random.randint(1,len(humain))
             print("Your turn.\nI took your "+str(choixO)+" card")
             donneur.append(humain[choixO-1])
             humain.remove(humain[choixO-1])
             donneur=elimine_paires(donneur)

             attend_le_joueur()
        
         tour += 1

     if len(donneur) == 0:
         print("I've completed all the maps.\nYou lose! Me, Robot, I won.")
     else:
         print("I have completed all the maps.\nCongratulations! You, Human, have won.")
    

	 
# programme principale
joue()

