class Commande:
    def __init__(self, numero_de_commande, liste_de_plats_commandes):
        self.__numero_de_commande = numero_de_commande
        self.__liste_de_plats_commandes = liste_de_plats_commandes
        self.__statut = "en cours"

    def ajouter_plat(self, plat):
        self.__liste_de_plats_commandes.append(plat)
    
    def annuler_commande(self):
        self.__statut = "annulée"

    def terminer_commande(self):
        self.__statut = "terminée"

    def __calculer_total(self):
        total = 0
        for plat in self.__liste_de_plats_commandes:
            total += plat["prix"]
        return total
    
    def __calculer_total_tva(self):
        return self.__calculer_total() * 0.1
    
    def __calculer_total_ttc(self):
        return self.__calculer_total() + self.__calculer_total_tva()

    def afficher_commande(self):
        print(f"Commande n°{self.__numero_de_commande}")
        for plat in self.__liste_de_plats_commandes:
            print(f"Plat: {plat["nom"]} à {plat["prix"]}€")
        print(f"Total HT: {self.__calculer_total()}")
        print(f"TVA: {self.__calculer_total_tva()}")
        print(f"Total TTC: {self.__calculer_total_ttc()}")
        print(f"Statut: {self.__statut}")
        print(f"============================================")

liste_de_plats_1 = [
                    {"nom":"hamburger", "prix": 10},
                    {"nom":"frites", "prix": 3},
                    {"nom":"nuggets", "prix": 5}
                ]

liste_de_plats_2 = [
                    {"nom":"salade", "prix": 7},
                    {"nom":"wrap", "prix": 7},
                    {"nom":"coca", "prix": 2}
                ]

liste_de_plats_3 = [
                    {"nom":"ramen", "prix": 16},
                    {"nom":"takoyakis", "prix": 5}
                ]

commande_1 = Commande(1,liste_de_plats_1)

commande_1.ajouter_plat({"nom": "fanta", "prix": 2})
commande_1.afficher_commande()

commande_2 = Commande(2,liste_de_plats_2)
commande_2.annuler_commande()
commande_2.afficher_commande()

commande_3 = Commande(3, liste_de_plats_3)
commande_3.terminer_commande()
commande_3.afficher_commande()