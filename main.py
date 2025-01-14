import tkinter as tk
from tkinter import Label


def creer_interface():
    #Crée l'interface utilisateur avec deux grilles et des contrôles.
    fenetre = tk.Tk()
    fenetre.title("Bataille Navale")
    fenetre.iconbitmap("img/logo.ico")
    fenetre.minsize(700,600)
    fenetre.maxsize(3000, 400)


    # Créer grille avec grid
    grille_joueur = tk.Frame(fenetre)
    grille_joueur.grid(row=0, column=0,padx=10,pady=10)
    grille_ordinateur = tk.Frame(fenetre)
    grille_ordinateur.grid(row=0, column=1, padx=10,pady=10)

    # Créer les grilles (boutons)
    taille = 10
    boutons_joueur = []
    boutons_ordinateur = []

    for i in range(taille):
        ligne_joueur = []
        ligne_ordinateur = []
        for j in range(taille):
            # Boutons pour la grille du joueur
            bouton_joueur = tk.Button(grille_joueur, text="", width=3, height=1, bg="red")
            bouton_joueur.grid(row=i, column=j, padx=1, pady=1)
            ligne_joueur.append(bouton_joueur)

            # Boutons pour la grille de l'ordinateur
            bouton_ordinateur = tk.Button(grille_ordinateur, text="", width=3, height=1, bg="blue")
            bouton_ordinateur.grid(row=i, column=j, padx=1, pady=1)
            ligne_ordinateur.append(bouton_ordinateur)

        boutons_joueur.append(ligne_joueur)
        boutons_ordinateur.append(ligne_ordinateur)

    # Panneau de contrôle
    panneau_controle = tk.Frame(fenetre)
    panneau_controle.grid(row=1, column=0, columnspan=2, pady=10)


    bouton_rejouer = tk.Button(panneau_controle, text="Rejouer", width=15)
    bouton_rejouer.pack(side=tk.LEFT, padx=5)

    fenetre.mainloop()

if __name__ == "__main__":
    creer_interface()
