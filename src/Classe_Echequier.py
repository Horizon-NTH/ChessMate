from Classe_Pieces import *


class Echequier:
    def __init__(self):
        # Création d'un tableau 8x8 vide
        self.Tableau = [["  " for _ in range(8)] for _ in range(8)]
        self.CaseSelec=[None,None]
        self.NumTour=1
        self.PlaceDesBlanc=0

    def getTableau(self):
        TableauDeRetour = []  # Création d'une liste vide pour le tableau de retour
        for ligne in range(8):
            TableauDeColonne = []  # Création d'une liste vide pour la colonne actuelle
            for colonne in range(8):
                # Vérification si l'objet est une instance de PieceGene ou d'une de ses sous-classes
                if isinstance(self.Tableau[ligne][colonne], PieceGene):
                    TableauDeColonne.append(self.Tableau[ligne][colonne].AffichageTerminal())  # Utilise .append pour ajouter l'affichage de la pièce
                else:
                    TableauDeColonne.append(None)  # Ajoute None si pas de pièce
            TableauDeRetour.append(TableauDeColonne)  # Ajoute la colonne complète au tableau de retour
        return TableauDeRetour

    def getCaseSelec(self):
        return self.CaseSelec

    def initialiserPlateau(self, PlaceBlanc:bool=0):
        self.PlaceDesBlanc=PlaceBlanc
        # Initialisation des pièces sur le plateau
        self.NumTour=1
        for ligne in range(8):
            for colonne in range(8):
                self.Tableau[ligne][colonne] = None
        if (self.PlaceDesBlanc)==0:
            mod=6
        else:
            mod=0
        for loop in range(8):
            self.Tableau[1][loop]= CreationPiece(6+mod)
            self.Tableau[6][loop]= CreationPiece(12-mod)
            if loop == 0 or loop == 7:
                self.Tableau[0][loop]= CreationPiece(5+mod)
                self.Tableau[7][loop]= CreationPiece(11-mod)
            if loop == 1 or loop == 6:
                self.Tableau[0][loop]= CreationPiece(4+mod)
                self.Tableau[7][loop]= CreationPiece(10-mod)  
            if loop == 2 or loop == 5:
                self.Tableau[0][loop]= CreationPiece(3+mod)
                self.Tableau[7][loop]= CreationPiece(9-mod)  
            if loop == 3:
                self.Tableau[0][loop]= CreationPiece(2+mod)
                self.Tableau[7][loop]= CreationPiece(7-mod)
            if loop == 4:
                self.Tableau[0][loop]= CreationPiece(1+mod)
                self.Tableau[7][loop]= CreationPiece(8-mod)

    def AfficherPlateauTerminal(self):
        #Permet d'afficher dans le terminal le contenu du tableau
        for ligne in range(8):
            for colonne in range(8):
                # Utilise isinstance pour vérifier si l'objet est une instance de PieceGene ou d'une de ses sous-classes
                if isinstance(self.Tableau[ligne][colonne], PieceGene):
                    print(self.Tableau[ligne][colonne].AffichageTerminal(), end=" ")
                else:
                    print("  ", end=" ")  # Assurez-vous d'ajouter end="" pour éviter les nouvelles lignes supplémentaires
            print()  # Ajout d'une nouvelle ligne après chaque ligne du plateau

    def GetListMovPossible(self, ligne:int, colone:int):
        #Prend les coordonée d'une case et renvoi une liste des cases ou la piece peut ce déplacer

        if isinstance(self.Tableau[ligne][colone], PieceGene):
            ListeCasePossible = [None]
            if ((self.Tableau[ligne][colone].couleur=="Black" and self.NumTour%2==0) or (self.Tableau[ligne][colone].couleur=="White" and self.NumTour%2==1)):
                ListeCasePossible = self.Tableau[ligne][colone].ListMovPossiblePiece(self.getTableau(),self.PlaceDesBlanc, ligne, colone)
            else:
                print("Ce n'est pas votre piece")
            return ListeCasePossible

        else:
            print("ERREUR: Aucune piece sur cette case")
            return None

    def Move(self, ligneDepart: int, colonneDepart: int, ligneArrivee: int, colonneArrivee: int):
        # On considère ici le déplacement a été approuvé
        self.NumTour += 1
        self.Tableau[ligneArrivee][colonneArrivee] = self.Tableau[ligneDepart][colonneDepart]
        self.Tableau[ligneDepart][colonneDepart] = None

    def SelectionPiece(self, ligne: int, colonne: int):
        # Basicement c'est le clic sur une case
        if isinstance(self.Tableau[ligne][colonne], PieceGene):  # cas où la case sélectionnée contient une pièce
            if self.CaseSelec == [None, None]:  # Cas où il n'y avait pas déjà une case sélectionnée
                self.CaseSelec = [ligne, colonne]
                return self.GetListMovPossible(ligne, colonne)
            else:  # Cas où une pièce était déjà sélectionnée
                if [ligne, colonne] in self.GetListMovPossible(self.CaseSelec[0], self.CaseSelec[1]):
                    self.Move(self.CaseSelec[0], self.CaseSelec[1], ligne, colonne)
                    self.CaseSelec = [None, None]
        else:  # Cas où il n'y a pas de pièce sur la case cliquée
            if self.CaseSelec != [None, None]:  # Cas où une case était déjà sélectionnée
                if [ligne, colonne] in self.GetListMovPossible(self.CaseSelec[0], self.CaseSelec[1]):  # Si le coup est valable
                    self.Move(self.CaseSelec[0], self.CaseSelec[1], ligne, colonne)
                    self.CaseSelec = [None, None]
                else:  # Si le coup n'est pas valable
                    self.CaseSelec = [None, None]

TestA = Echequier()
TestA.initialiserPlateau(1)
TestA.AfficherPlateauTerminal()

TestA.SelectionPiece(1,0)
TestA.SelectionPiece(3,0)
TestA.AfficherPlateauTerminal()

TestA.SelectionPiece(6,6)
TestA.SelectionPiece(4,6)
TestA.AfficherPlateauTerminal()

TestA.SelectionPiece(1,7)
TestA.SelectionPiece(3,7)
TestA.AfficherPlateauTerminal()

TestA.SelectionPiece(4,6)
TestA.SelectionPiece(3,7)
TestA.AfficherPlateauTerminal()
print("Debut du changement")

TestA.SelectionPiece(3,0)
TestA.SelectionPiece(4,0)
TestA.AfficherPlateauTerminal()

TestA.SelectionPiece(3,7)
TestA.SelectionPiece(2,7)
TestA.AfficherPlateauTerminal()

TestA.SelectionPiece(4,0)
TestA.SelectionPiece(5,0)
TestA.AfficherPlateauTerminal()

TestA.SelectionPiece(2,7)
TestA.SelectionPiece(1,7)
TestA.AfficherPlateauTerminal()

TestA.SelectionPiece(5,0)
TestA.SelectionPiece(6,0)
TestA.AfficherPlateauTerminal()

TestA.SelectionPiece(5,0)
TestA.SelectionPiece(6,1)
TestA.AfficherPlateauTerminal()

TestA.SelectionPiece(1,7)
TestA.SelectionPiece(0,6)
TestA.AfficherPlateauTerminal()

TestA.SelectionPiece(0,0)
TestA.SelectionPiece(6,0)
TestA.AfficherPlateauTerminal()

TestA.SelectionPiece(7,0)
TestA.SelectionPiece(7,1)
TestA.AfficherPlateauTerminal()

TestA.SelectionPiece(7,0)
TestA.SelectionPiece(6,0)
TestA.AfficherPlateauTerminal()