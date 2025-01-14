class Navire:
    def __init__(self, nom, taille):
        self.nom = nom
        self.positions = []  # [ case 1 : (x,y),  case 2 : (x,y), ... ] tuple permettant d'avoir tous les coordonées du navire
        self.touches = []  # pareil mais enregistre ceux qui ont été touchés
        self.envie = True

    def est_touche(self, x, y):
        #Vérifie si le navire est touché
        position = (x, y)
        if position in self.positions and position not in self.touches:
            self.touches.append(position)

    #def est_coule(self):
        #Vérifie si le navire est coulé


class Plateau:
    def __init__(self):
        self.taille = 10
        self.grille = [['~' for _ in range(10)] for _ in range(10)]
        self.navires = []  # Liste des navires placés sur le plateau

    def placer_navire(self, navire, x, y, orientation):
        # Placer un navire sur le plateau après avoir vérifier si ce n'est pas déjà occupéé
        if self.placer_navire_verif(navire, x, y, orientation):
            # Placer le navire sur la grille
            positions = []
            for i in range(navire.taille):
                if orientation == 'horizontal':
                    self.grille[y][x + i] = 'N'
                    positions.append((x + i, y))
                else:  # vertical
                    self.grille[y + i][x] = 'N'
                    positions.append((x, y + i))
            navire.positions = positions
            self.navires.append(navire)
            return True
        return False

    def placer_navire_verif(self, navire, x, y, orientation):
        if orientation == 'horizontal':
            if x + navire.taille > self.taille:
                return False
            # Vérifier si les cases sont libres
            return all(self.grille[y][x + i] == '~' for i in range(navire.taille))
        else:  # vertical
            if y + navire.taille > self.taille:
                return False
            # Vérifier si les cases sont libres
            return all(self.grille[y + i][x] == '~' for i in range(navire.taille))

    def recevoir_tir(self, x, y):
        #Reçoit un tir aux coordonnées données
        if self.grille[y][x] == 'N':
            for navire in self.navires:
                if (x, y) in navire.positions:
                    navire.est_touche(x, y)
                    self.grille[y][x] = 'X'
                    return True
        else:
            self.grille[y][x] = 'O'
        return False

    def all_navire_touche(self):
        return all(navire.est_coule() for navire in self.navires) # éxécute fonctions x nombre de fois


class Joueur:
    def __init__(self, nom, est_ordinateur=False):
        self.nom = nom
        self.est_ordinateur = est_ordinateur
        self.plateau = Plateau()
        self.navires_ = [
            Navire("Porte-avions", 5),
            Navire("Croiseur", 4),
            Navire("Destroyer", 3),
            Navire("Destroyer", 3),
            Navire("Sous-marin", 2),
            Navire("Sous-marin", 2)
        ]
        self.tirs = []

    def tirer(self, x, y):
        if (x, y) not in self.tirs:
            self.tirs.append((x, y))
            return True
        return False

    def a_perdu(self):
        return self.plateau.all_navire_touche()