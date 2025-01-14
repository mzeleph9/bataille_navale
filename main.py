import tkinter as tk
from tkinter import messagebox
import random


class Navire:
    def __init__(self, nom, taille):
        self.nom = nom
        self.taille = taille
        self.positions = []
        self.touches = []

    def est_touche(self, x, y):
        position = (x, y)
        if position in self.positions and position not in self.touches:
            self.touches.append(position)
            return True
        return False

    def est_coule(self):
        return len(self.touches) == len(self.positions)


class Plateau:
    def __init__(self):
        self.taille = 10
        self.grille = [['~' for _ in range(10)] for _ in range(10)]
        self.navires = []

    def placer_navire(self, navire, x, y, orientation):
        if self.placer_navire_verif(navire, x, y, orientation):
            positions = []
            for i in range(navire.taille):
                if orientation == 'horizontal':
                    self.grille[y][x + i] = 'N'
                    positions.append((x + i, y))
                else:
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
            return all(self.grille[y][x + i] == '~' for i in range(navire.taille))
        else:
            if y + navire.taille > self.taille:
                return False
            return all(self.grille[y + i][x] == '~' for i in range(navire.taille))

    def recevoir_tir(self, x, y):
        if 0 <= x < self.taille and 0 <= y < self.taille:
            if self.grille[y][x] == 'N':
                for navire in self.navires:
                    if (x, y) in navire.positions:
                        navire.est_touche(x, y)
                        self.grille[y][x] = 'X'
                        return True
            elif self.grille[y][x] == '~':
                self.grille[y][x] = 'O'
            return False
        return False

    def tous_navires_coules(self):
        return all(navire.est_coule() for navire in self.navires)


class JeuBatailleNavale:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Bataille Navale")
        self.fenetre.minsize(700, 600)

        self.plateau_joueur = Plateau()
        self.plateau_ordinateur = Plateau()
        self.initialiser_interface()
        self.placer_navires_ordinateur()
        self.placer_navires_joueur()

    def initialiser_interface(self):
        # Création des grilles
        self.grille_joueur = tk.Frame(self.fenetre)
        self.grille_joueur.grid(row=0, column=0, padx=10, pady=10)
        self.grille_ordinateur = tk.Frame(self.fenetre)
        self.grille_ordinateur.grid(row=0, column=1, padx=10, pady=10)

        # Labels
        tk.Label(self.grille_joueur, text="Votre flotte").grid(row=0, column=0, columnspan=10)
        tk.Label(self.grille_ordinateur, text="Flotte ennemie").grid(row=0, column=0, columnspan=10)

        # Création des boutons
        self.boutons_joueur = []
        self.boutons_ordinateur = []




        for i in range(10):
            ligne_joueur = []
            ligne_ordinateur = []
            for j in range(10):
                # Boutons joueur
                bouton = tk.Button(self.grille_joueur, width=3, height=1, bg='lightblue')
                bouton.grid(row=i + 1, column=j, padx=1, pady=1)
                ligne_joueur.append(bouton)

                # Boutons ordinateur
                bouton = tk.Button(self.grille_ordinateur, width=3, height=1, bg='lightblue',
                                   command=lambda x=j, y=i: self.clic_case_ordinateur(x, y))
                bouton.grid(row=i + 1, column=j, padx=1, pady=1)
                ligne_ordinateur.append(bouton)

            self.boutons_joueur.append(ligne_joueur)
            self.boutons_ordinateur.append(ligne_ordinateur)

        # Bouton Rejouer
        tk.Button(self.fenetre, text="Nouvelle Partie",
                  command=self.nouvelle_partie).grid(row=1, column=0, columnspan=2, pady=10)

    def placer_navires_ordinateur(self):
        navires = [
            Navire("Porte-avions", 5),
            Navire("Croiseur", 4),
            Navire("Destroyer", 3),
            Navire("Sous-marin", 2)
        ]

        for navire in navires:
            place = False
            while not place:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                orientation = random.choice(['horizontal', 'vertical'])
                place = self.plateau_ordinateur.placer_navire(navire, x, y, orientation)

    def placer_navires_joueur(self):
        navires = [
            Navire("Porte-avions", 5),
            Navire("Croiseur", 4),
            Navire("Destroyer", 3),
            Navire("Sous-marin", 2)
        ]

        for navire in navires:
            place = False
            while not place:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                orientation = random.choice(['horizontal', 'vertical'])
                place = self.plateau_joueur.placer_navire(navire, x, y, orientation)
                if place:
                    self.afficher_navire_joueur(navire)

    def afficher_navire_joueur(self, navire):
        for x, y in navire.positions:
            self.boutons_joueur[y][x].configure(bg='gray')

    def clic_case_ordinateur(self, x, y):
        if self.plateau_ordinateur.grille[y][x] not in ['O', 'X']:
            touche = self.plateau_ordinateur.recevoir_tir(x, y)
            if touche:
                self.boutons_ordinateur[y][x].configure(bg='red')
                if self.plateau_ordinateur.tous_navires_coules():
                    messagebox.showinfo("Victoire!", "Vous avez gagné!")
                    return
            else:
                self.boutons_ordinateur[y][x].configure(bg='white')

            # Tour de l'ordinateur
            self.tour_ordinateur()

    def tour_ordinateur(self):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        while self.plateau_joueur.grille[y][x] in ['O', 'X']:
            x = random.randint(0, 9)
            y = random.randint(0, 9)

        touche = self.plateau_joueur.recevoir_tir(x, y)
        if touche:
            self.boutons_joueur[y][x].configure(bg='red')
            if self.plateau_joueur.tous_navires_coules():
                messagebox.showinfo("Défaite!", "L'ordinateur a gagné!")
        else:
            self.boutons_joueur[y][x].configure(bg='white')

    def nouvelle_partie(self):
        self.plateau_joueur = Plateau()
        self.plateau_ordinateur = Plateau()

        # Réinitialiser les boutons
        for i in range(10):
            for j in range(10):
                self.boutons_joueur[i][j].configure(bg='lightblue')
                self.boutons_ordinateur[i][j].configure(bg='lightblue')

        # Replacer les navires
        self.placer_navires_ordinateur()
        self.placer_navires_joueur()

    def demarrer(self):
        self.fenetre.mainloop()


if __name__ == "__main__":
    jeu = JeuBatailleNavale()
    jeu.demarrer()