#!/usr/bin/python
# Importation des librairies necessaires
import operator


class Noeud:
    """def __init__(self):
        self.pere = None
        self.filsGauche = None
        self.filsDroit = None
        self.valeur = None"""

    def __init__(self, pere, filsG, filsD, valeur):
        self.pere = pere
        self.filsGauche = filsG
        self.filsDroit = filsD
        self.valeur = valeur

    def setPere(self, pere):
        self.pere = pere

    def setValeur(self, valeur):
        self.valeur = valeur

    def setFilsGauche(self, filsG):
        self.filsGauche = filsG

    def setFilsDroit(self, filsD):
        self.filsDroit = filsD

    def getPere(self):
        return self.pere

    def getFilsGauche(self):
        return self.filsGauche

    def getFilsDroit(self):
        return self.filsDroit

    def getValeur(self):
        return self.valeur

# ------------------------------------------------------------------------------
class Huffman:

    def __init__(self, fichier):
        with open(fichier, 'r') as file:
            self.contenu = file.readlines()


    def creerFile(self):
        """
        Fonction qui creer une file contenant les caracteres du texte avec leur
        frequence d'apparition a l'interieur de celui-ci
        """
        tmpDic = {}
        dictlist = []
        # Pour chaque ligne du texte
        for i in self.contenu:
            # Pour chaque caractere de la ligne
            for j in i:
                # Si le dictionnaire ne contient pas le caractere
                if(j not in tmpDic):
                    tmpDic[j] = 1
                else :
                    tmpDic[j] += 1
        # Trie du dictionnaire
        dicoTrie = sorted(tmpDic.items(), key=operator.itemgetter(1))
        #print(dicoTrie)
        return dicoTrie

    def creerArbre(self, dicoTrie):
        """
        Fonction qui creer un arbre a partir d'un dico trie
        """
        ##i est l'élément de la liste courant
        ##
        while(len(dicoTrie) > 1):
            premierElement = dicoTrie[0]
            secondElement = dicoTrie[1]
            if (type(premierElement)!="Noeud" and secondElement!="Noeud"):
                #premierElement = dicoTrie[0]
                #secondElement = dicoTrie[1]
                del dicoTrie[0]
                del dicoTrie[1]
                # Noeud(pere, filsG, filsD, valeur)
                somme = premierElement[1] + secondElement[1]
                noeud = Noeud(None, premierElement, secondElement, somme)
                dicoTrie.append(noeud)
            #    while()
            #else:
"""
    def ajouterArbreDansListe(self, liste, noeud):
        trouve = False
        i = 0
        while(trouve == False):
            if
            if(liste[i][1] > noeud.getValeur()):
                trouve = True
            else:
                i += 1
        liste.insert(i, noeud)
"""







test = Huffman("./leHorla.txt")
test.creerFile()
lol = Noeud(None, None, None, None)
print(isinstance(lol, Noeud(None,None,None,None)))


    #pyDic = {"a" : 52, "b" : 32, "c" : 11, "d" : 11, "z" : 42, "j" : 11}
    #newDic = sorted(pyDic.items(), key=operator.itemgetter(1)) #expliquer cette merde
    #print(newDic)
