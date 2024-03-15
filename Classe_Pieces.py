


def CreationPiece (idPiece:int):
    #Crée une pièce en fonction de l'id rentré
    #Les id sont comme suit : (1: Roi, 2: Dame, 3: Fou, 4: Cavalier, 5: Tour, 6: Pion)
    #On rajoute 6 si il s'agit d'une piece noir
    if (idPiece <=6):
        couleurPiece = "White"
    else:
        couleurPiece = "Black"
        idPiece -=6
    if (idPiece ==1):
        return General(couleurPiece)
    if (idPiece ==2):
        return Queen(couleurPiece)
    if (idPiece ==3):
        return Fool(couleurPiece)
    if (idPiece ==4):
        return Knight(couleurPiece)
    if (idPiece ==5):
        return Rock(couleurPiece)
    if (idPiece ==6):
        return Pawn(couleurPiece)
    return None

class PieceGene:
    def __init__(self, couleur:str):
        self.couleur = couleur # 1 implique une piece noir et 0 une piece blanche
        self.PieceClass = "None"

    def getCouleur():
        return self.couleur

    def AffichageTerminal(self):
        return self.PieceClass[0]+ self.couleur[0]
class General(PieceGene):
    def __init__(self, couleur: str):
        super().__init__(couleur)
        self.PieceClass = "General"

    def ListMovPossiblePiece(self, Echequier, PlaceDesBlanc, ligne: int, colone: int):
        TableauDeRetour = []

        for loop in range(8):
            ArretAvance = 0
            nbCase = 1
            if loop == 0:
                multiligne = 1
                multicolone = 1
            elif loop == 1:
                multiligne = -1
                multicolone = -1
            elif loop == 2:
                multiligne = -1
                multicolone = 1
            elif loop == 3:
                multiligne = 1
                multicolone = -1
            elif loop == 4:
                multiligne = 1
                multicolone = 0
            elif loop == 5:
                multiligne = -1
                multicolone = 0
            elif loop == 6:
                multiligne = 0
                multicolone = 1
            elif loop == 7:
                multiligne = 0
                multicolone = -1

            if 0 <= ligne + multiligne < 8 and 0 <= colone + multicolone < 8:
                newPosition = Echequier[ligne + multiligne][colone + multicolone]
                if newPosition is None:  # If no piece encountered
                    TableauDeRetour.append([ligne + multiligne, colone + multicolone])
                elif newPosition[1] != self.couleur[0]:  # If an enemy piece is encountered
                    TableauDeRetour.append([ligne + multiligne, colone + multicolone])
            else:
                break  # Break the loop if outside the board

        return TableauDeRetour

class Queen (PieceGene):
    def __init__(self, couleur:str):
        super().__init__(couleur)
        self.PieceClass = "Queen"
    def ListMovPossiblePiece(self, Echequier, PlaceDesBlanc, ligne: int, colone: int):
        TableauDeRetour = []

        for loop in range(8):
            ArretAvance = 0
            nbCase = 1
            if loop == 0:
                multiligne = 1
                multicolone = 1
            elif loop == 1:
                multiligne = -1
                multicolone = -1
            elif loop == 2:
                multiligne = -1
                multicolone = 1
            elif loop == 3:
                multiligne = 1
                multicolone = -1
            elif loop == 4:
                multiligne = 1
                multicolone = 0
            elif loop == 5:
                multiligne = -1
                multicolone = 0
            elif loop == 6:
                multiligne = 0
                multicolone = 1
            elif loop == 7:
                multiligne = 0
                multicolone = -1

            while ArretAvance == 0:
                if 0 <= ligne + nbCase * multiligne < 8 and 0 <= colone + nbCase * multicolone < 8:
                    newPosition = Echequier[ligne + nbCase * multiligne][colone + nbCase * multicolone]
                    if newPosition is None:  # If no piece encountered
                        TableauDeRetour.append([ligne + nbCase * multiligne, colone + nbCase * multicolone])
                    elif newPosition[1] != self.couleur[0]:  # If an enemy piece is encountered
                        TableauDeRetour.append([ligne + nbCase * multiligne, colone + nbCase * multicolone])
                        ArretAvance = 1
                    else:  # If an ally piece is encountered
                        ArretAvance = 1
                else:
                    break  # Break the loop if outside the board
                nbCase += 1
        return TableauDeRetour

class Fool (PieceGene):
    def __init__(self, couleur:str):
        super().__init__(couleur)
        self.PieceClass = "Fool"
    def ListMovPossiblePiece(self, Echequier, PlaceDesBlanc, ligne: int, colone: int):
        TableauDeRetour = []

        for loop in range(4):
            ArretAvance = 0
            nbCase = 1
            if loop == 0:
                multiligne = 1
                multicolone = 1
            elif loop == 1:
                multiligne = -1
                multicolone = -1
            elif loop == 2:
                multiligne = -1
                multicolone = 1
            elif loop == 3:
                multiligne = 1
                multicolone = -1

            while ArretAvance == 0:
                if 0 <= ligne + nbCase * multiligne < 8 and 0 <= colone + nbCase * multicolone < 8:
                    newPosition = Echequier[ligne + nbCase * multiligne][colone + nbCase * multicolone]
                    if newPosition is None:  # If no piece encountered
                        TableauDeRetour.append([ligne + nbCase * multiligne, colone + nbCase * multicolone])
                    elif newPosition[1] != self.couleur[0]:  # If an enemy piece is encountered
                        TableauDeRetour.append([ligne + nbCase * multiligne, colone + nbCase * multicolone])
                        ArretAvance = 1
                    else:  # If an ally piece is encountered
                        ArretAvance = 1
                else:
                    break  # Break the loop if outside the board
                nbCase += 1
        return TableauDeRetour


class Knight (PieceGene):
    def __init__(self, couleur:str):
        super().__init__(couleur)
        self.PieceClass = "Knight"
    def ListMovPossiblePiece(self, Echequier, PlaceDesBlanc, ligne: int, colone: int):
        TableauDeRetour = []

        for loop in range(8):
            ArretAvance = 0
            nbCase = 1
            if loop == 0:
                multiligne = 2
                multicolone = 1
            elif loop == 1:
                multiligne = 2
                multicolone = -1
            elif loop == 2:
                multiligne = -2
                multicolone = 1
            elif loop == 3:
                multiligne = -2
                multicolone = -1
            elif loop == 4:
                multiligne = 1
                multicolone = 2
            elif loop == 5:
                multiligne = -1
                multicolone = 2
            elif loop == 6:
                multiligne = 1
                multicolone = -2
            elif loop == 7:
                multiligne = -1
                multicolone = -2

            if 0 <= ligne + multiligne < 8 and 0 <= colone + multicolone < 8:
                newPosition = Echequier[ligne + multiligne][colone + multicolone]
                if newPosition is None:  # If no piece encountered
                    TableauDeRetour.append([ligne + multiligne, colone + multicolone])
                elif newPosition[1] != self.couleur[0]:  # If an enemy piece is encountered
                    TableauDeRetour.append([ligne + multiligne, colone + multicolone])
            else:
                break  # Break the loop if outside the board

        return TableauDeRetour


class Rock(PieceGene):
    def __init__(self, couleur: str):
        super().__init__(couleur)
        self.PieceClass = "Rock"

    def ListMovPossiblePiece(self, Echequier, PlaceDesBlanc, ligne: int, colone: int):
        TableauDeRetour = []

        for loop in range(4):
            ArretAvance = 0
            nbCase = 1
            if loop == 0:
                multiligne = 1
                multicolone = 0
            elif loop == 1:
                multiligne = -1
                multicolone = 0
            elif loop == 2:
                multiligne = 0
                multicolone = 1
            elif loop == 3:
                multiligne = 0
                multicolone = -1

            while ArretAvance == 0:
                if 0 <= ligne + nbCase * multiligne < 8 and 0 <= colone + nbCase * multicolone < 8:
                    newPosition = Echequier[ligne + nbCase * multiligne][colone + nbCase * multicolone]
                    if newPosition is None:  # If no piece encountered
                        TableauDeRetour.append([ligne + nbCase * multiligne, colone + nbCase * multicolone])
                    elif newPosition[1] != self.couleur[0]:  # If an enemy piece is encountered
                        TableauDeRetour.append([ligne + nbCase * multiligne, colone + nbCase * multicolone])
                        ArretAvance = 1
                    else:  # If an ally piece is encountered
                        ArretAvance = 1
                else:
                    break  # Break the loop if outside the board
                nbCase += 1
        return TableauDeRetour


class Pawn(PieceGene):
    def __init__(self, couleur: str):
        super().__init__(couleur)
        self.PieceClass = "Pawn"

    def ListMovPossiblePiece(self, Echequier, PlaceDesBlanc, ligneP: int, coloneP: int):
        TableauDeRetour = []

        # Déterminer le sens de mouvement
        sens = -1 if self.couleur == "White" else 1
        if PlaceDesBlanc:
            sens = sens* -1
        # Mouvement vers l'avant
        if Echequier[ligneP + sens][coloneP] is None:
            TableauDeRetour.append([ligneP + sens, coloneP])
        # Mouvement initial de deux cases
        if (self.couleur == "White" and ((ligneP == 6 and PlaceDesBlanc == 0) or (ligneP == 1 and PlaceDesBlanc == 1))) or \
            (self.couleur == "Black" and ((ligneP == 1 and PlaceDesBlanc == 0) or (ligneP == 6 and PlaceDesBlanc == 1))):
                if Echequier[ligneP + 2 * sens][coloneP] is None:
                    TableauDeRetour.append([ligneP + 2 * sens, coloneP])

        # Prises diagonales
        for delta_colone in [-1, 1]:
            nouvelle_colone = coloneP + delta_colone
            if 0 <= nouvelle_colone < 8:  # Vérifier les limites de l'échiquier
                piece_diagonale = Echequier[ligneP + sens][nouvelle_colone]
                if piece_diagonale is None or piece_diagonale[1] == self.couleur[0]:
                    pass
                else:
                    TableauDeRetour.append([ligneP + sens, nouvelle_colone])

        return TableauDeRetour
