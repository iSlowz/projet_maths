import time
import math
from probleme2 import *

def question2():
    sum = 0
    for i in range(0, 24):
        sum += 2 ** i
    print(sum)


def solve(objects, cap):
    # On parcourt le tableau d'objets et on calcule le rapport utilité/poids
    for key, value in objects.items():
        # utility=value[1]
        # weight=value[0]
        profitability = value[1] / value[0]

        objects[key] = (profitability, value[0], value[1])

    # On trie les objets par ordre décroissant de rapport utilité/poids

    sorted_objects = sorted(objects.items(), key=lambda x: x[1][0], reverse=True)

    sum_weight = 0
    sum_utility = 0
    list_objects = []
    # On ajoute les objets dans le sac à dos

    # print(sorted_objects)
    for i in sorted_objects:  # On parcourt les objets triés
        if sum_weight + i[1][1] <= cap:  # Si on peut ajouter l'objet dans le sac on l'ajoute
            sum_weight += i[1][1]
            sum_utility += i[1][2]
            list_objects.append(i[0])
    print("Liste des objets à prendre:", list_objects)
    print("Utilité totale:", sum_utility)
    print("Poids total:", sum_weight)


def solve2(objects, cap):
    sorted_objects = {}

    for key, value in objects.items():
        # si on a déjà une clé du poid de l'objet dans sorted_objects
        if value[0] in sorted_objects.keys():
            # ajoute le tuple (key,value[1]) à sorted_objects[value[0]], liste de tuples, triée dans l'ordre décroissant
            sorted_objects[value[0]].append((key, value[1]))
            sorted_objects[value[0]].sort(key=lambda x: x[1], reverse=True)
        else:
            # sinon on crée une nouvelle clé dans sorted_objects avec pour valeur une liste contenant le tuple (key,value[1])
            sorted_objects[value[0]] = [(key, value[1])]

    print("dico trié par poid", sorted_objects)

    # les clés de sorted_objects sont les poids des objets, avec pour valeur une liste de tuples d'objets (nom objet,utilité), triés dans l'order décroissant de l'utilité, je veux tester toutes les combinaisons possibles poids, qui additionnées ne dépassent pas cap, sachant qu'on peut en additionner autant d'objets qu'on veut, on peut additionner 2 fois la même clé mais dans ce cas là on prendra l'objets suivant dans la liste de values
    # on va donc parcourir sorted_objects et tester toutes les combinaisons possibles de poids, en additionnant les utilités des objets, et on garde la combinaison qui a le plus d'utilité
    weights = list(sorted_objects.keys())
    # print(weights)
    nb_objects_per_weight = {i: len(sorted_objects[i]) for i in weights}

    # print(nb_objects_per_weight)

    def generate_combinations(weights, nb_objects_per_weight, cap):
        combinations = []
        current_combination = []
        backtrack(weights, nb_objects_per_weight, cap, 0, current_combination, combinations)
        return combinations

    def backtrack(weights, nb_objects_per_weight, cap, current_weight, current_combination, combinations):
        if current_weight > cap:
            return

        if current_weight <= cap:
            combinations.append(list(current_combination))

        for weight in weights:
            if nb_objects_per_weight[weight] > 0:
                current_combination.append(weight)
                nb_objects_per_weight[weight] -= 1
                current_weight += weight
                backtrack(weights, nb_objects_per_weight, cap, current_weight, current_combination, combinations)
                current_combination.pop()
                nb_objects_per_weight[weight] += 1
                current_weight -= weight

    # on va tester toutes les combinaisons possibles de poids, en additionnant les utilités des objets, et on garde la combinaison qui a le plus d'utilité

    combinations = generate_combinations(weights, nb_objects_per_weight, cap)
    print("Liste des combinaisons possibles:", combinations)
    max_utility = 0
    max_weight = 0
    max_liste_objects = []

    for combi in combinations:
        current_liste_objects = []
        current_utility = 0
        current_weight = 0
        for i in combi:
            j = 0
            while sorted_objects[i][j][0] in current_liste_objects:
                j += 1
            current_liste_objects.append(sorted_objects[i][j][0])
            current_utility += sorted_objects[i][j][1]
            current_weight += i
            if current_utility > max_utility:
                max_utility = round(current_utility, 3)
                max_weight = round(current_weight, 3)
                max_liste_objects = current_liste_objects

    print("Liste des objets à prendre:", max_liste_objects)
    print("Utilité totale:", max_utility)
    print("Poids total:", max_weight)


def knapsack_branch_and_bound1(list_objects, cap):  # marche pas

    def callback(list_objects, cap, compteur=0, current_weight=0, current_utility=0, current_combination=[],
                 combinations=[], left=True):
        if current_weight > cap or compteur >= len(list_objects) - 1:
            return

        compteur += 1
        if left:
            current_combination.append(list_objects[compteur][0])
            current_weight += list_objects[compteur][1]
            current_utility += list_objects[compteur][2]

        callback(list_objects, cap, compteur, current_weight, current_utility, current_combination, combinations, True)
        if compteur != 0:
            current_combination.pop()
            current_weight -= list_objects[compteur][1]
            current_utility -= list_objects[compteur][2]
            combinations.append((current_combination, current_weight, current_utility))

        callback(list_objects, cap, compteur, current_weight, current_utility, current_combination, combinations, False)
        if compteur != 0:
            current_combination.pop()
            current_weight -= list_objects[compteur][1]
            current_utility -= list_objects[compteur][2]
            combinations.append((current_combination, current_weight, current_utility))
        compteur -= 1

    combinations = []
    callback(list_objects, cap, 0, 0, 0, [], combinations)
    print("Liste des combinaisons possibles:", combinations)
    print("Liste des objets à prendre:", max(combinations, key=lambda x: x[2]))


class Tree:
    def __init__(self, valeur, gauche=None, droite=None, parent=None, level=0):
        self.noeud = valeur
        self.gauche = gauche
        self.droite = droite
        self.parent = parent
        self.level = level

    def add_child(self, valeur, left=True):
        if left:
            self.gauche = Tree(valeur)
            self.gauche.parent = self
        else:
            self.droite = Tree(valeur)
            self.droite.parent = self

    def construire():
        pass


if __name__ == '__main__':
    # question2()
    objects = {
        "Pompe": (0.2, 1.5),
        "Démonte-pneus": (0.1, 1.5),
        "Gourde": (1, 2),
        "Chambre à air": (0.2, 0.5),
        "Clé de 15": (0.3, 1),
        "Multi-tool": (0.2, 1.7),
        "Pince multiprise": (0.4, 0.8),
        "Couteau suisse": (0.2, 1.5),
        "Compresses": (0.1, 0.4),
        "Désinfectant": (0.2, 0.6),
        "Veste de pluie": (0.4, 1),
        "Pantalon de pluie": (0.4, 0.75),
        "Crème solaire": (0.4, 1.75),
        "Carte IGN": (0.1, 0.2),
        "Batterie Portable": (0.5, 0.4),
        "Téléphone mobile": (0.4, 2),
        "Lampes": (0.3, 1.8),
        "Arrache Manivelle": (0.4, 0),
        "Bouchon valve chromé bleu": (0.01, 0.1),
        "Maillon rapide": (0.05, 1.4),
        "Barre de céréales": (0.4, 0.8),
        "Fruits": (0.6, 1.3),
        "Rustines": (0.05, 1.5)
    }
    cap = 0.6

    # deb = time.time()
    # solve(objects, cap)
    # fin = time.time()
    # print("Temps de la fonction :",fin - deb)

    deb = time.time()
    solve2(objects, cap)
    fin = time.time()
    print("Temps de la fonction :", fin - deb)

    # knapsack_branch_and_bound1(list_objects, cap)

    # wagons = bin_packing_probleme_d1_offline_best(list_marchandises, 11.583)
    # print(wagons)
    # print("Nombre de wagons:", len(wagons))
    # print(aa(marchandises=list_marchandises, capacite=11.583))

    list_marchandises = [
        ("Tubes acier", 10, 1, 0.5),
        ("Tubes acier", 9, 2, 0.7),
        ("Tubes acier", 7.5, 1.2, 0.4),
        ("Acide chlorhydrique", 1, 1, 1),
        ("Godet pelleteuse", 2, 2, 1),
        ("Rails", 11, 1, 0.2),
        ("Tubes PVC", 3, 2, 0.6),
        ("Echaffaudage", 3, 1.3, 1.8),
        ("Verre", 3, 2.1, 0.6),
        ("Ciment", 4, 1, 0.5),
        ("Bois vrac", 5, 0.8, 1),
        ("Troncs chênes", 6, 1.9, 1),
        ("Troncs hêtres", 7, 1.6, 1.5),
        ("Pompe à chaleur", 5, 1.1, 2.3),
        ("Cuivre", 6, 2, 1.4),
        ("Zinc", 5, 0.8, 0.8),
        ("Papier", 4, 1.6, 0.6),
        ("Carton", 7, 1, 1.3),
        ("Verre blanc vrac", 9, 0.9, 2.2),
        ("Verre brun vrac", 3, 1.6, 0.9),
        ("Briques rouges", 5, 1.1, 2.4),
        ("Pièces métalliques", 6, 1.6, 1.4),
        ("Pièces métalliques", 7, 0.9, 1.2),
        ("Pièces métalliques", 3, 1.6, 1.9),
        ("Ardoises", 1, 1.8, 1),
        ("Tuiles", 2, 1.2, 2.3),
        ("Vitraux", 4, 0.7, 1.2),
        ("Carrelage", 6, 1.2, 2.5),
        ("Tôles", 7, 0.6, 1.5),
        ("Tôles", 9, 1.7, 1),
        ("Tôles", 6, 1.9, 1.6),
        ("Tôles", 3, 2.2, 2.2),
        ("Tôles", 3, 0.5, 2.2),
        ("Mobilier urbain", 4, 0.7, 1.9),
        ("Lin", 5, 2.2, 0.7),
        ("Textiles à recycler", 6, 1.3, 2.5),
        ("Aluminium", 6, 1.3, 1.2),
        ("Batteries automobile", 7, 1.4, 2.5),
        ("Quincaillerie", 6, 1.1, 1),
        ("Treuil", 7, 0.9, 1.3),
        ("Treuil", 8, 0.5, 0.5),
        ("Acier", 8, 0.9, 1.7),
        ("Laine de bois", 8, 0.9, 1.8),
        ("Ouate de cellusose", 5, 1.7, 1.2),
        ("Chanvre isolation", 2.2, 1.6, 1.1),
        ("Moteur élecrique", 4.2, 1.5, 0.8),
        ("Semi conducteurs", 3.7, 0.9, 1.4),
        ("Semi conducteurs", 5.6, 0.5, 1.4),
        ("Semi conducteurs", 4.9, 0.9, 2.5),
        ("Semi conducteurs", 8.7, 1.3, 1.3),
        ("Semi conducteurs", 6.1, 2.2, 2.3),
        ("Semi conducteurs", 3.3, 1.8, 2.3),
        ("Semi conducteurs", 2.6, 1.6, 2.3),
        ("Semi conducteurs", 2.9, 1.6, 2),
        ("Aluminium", 2, 1.1, 0.6),
        ("Aluminium", 3, 0.6, 1.2),
        ("Aluminium", 6, 1, 0.8),
        ("Aluminium", 5, 1.3, 0.6),
        ("Aluminium", 4, 2.1, 2.1),
        ("Aluminium", 6, 1.5, 1.9),
        ("Aluminium", 4, 0.8, 2.1),
        ("Aluminium", 2, 2, 2.3),
        ("Aluminium", 4, 1, 1.1),
        ("Aluminium", 6, 1.8, 1.1),
        ("Lithium", 6, 1.9, 0.9),
        ("Lithium", 3, 2, 2.2),
        ("Lithium", 4, 1.5, 0.9),
        ("Lithium", 4, 2.1, 2.5),
        ("Lithium", 2, 1.2, 1.5),
        ("Lithium", 6, 1.3, 2),
        ("Lithium", 2, 0.8, 1.1),
        ("Contreplaqué", 4, 1.4, 2),
        ("Contreplaqué", 5, 0.6, 0.5),
        ("Contreplaqué", 5, 0.6, 1.8),
        ("Contreplaqué", 4, 0.7, 1.4),
        ("Contreplaqué", 6, 0.5, 0.7),
        ("Contreplaqué", 3, 1.5, 1.8),
        ("Contreplaqué", 3, 1.4, 2),
        ("Contreplaqué", 3, 2, 2.3),
        ("Contreplaqué", 5, 1.5, 0.7),
        ("Contreplaqué", 5, 2.2, 0.5),
        ("Contreplaqué", 6, 1.2, 1.2),
        ("Poutre", 5, 0.8, 0.7),
        ("Poutre", 3, 0.5, 1.9),
        ("Poutre", 5, 1.4, 0.7),
        ("Poutre", 6, 0.7, 0.7),
        ("Poutre", 6, 1.2, 2),
        ("Poutre", 3, 1.7, 1.1),
        ("Poutre", 5, 1.6, 2.1),
        ("Pneus", 3, 1.3, 1.7),
        ("Pneus", 4, 1.5, 1.7),
        ("Pneus", 3, 1.5, 1.9),
        ("Pneus", 3, 0.6, 1.9),
        ("Pneus", 5, 1.8, 0.5),
        ("Pneus", 3, 1.8, 0.7),
        ("Pneus", 4, 1.7, 1.4),
        ("Pneus", 4, 1.5, 0.5),
        ("Pneus", 2, 2.1, 1.8),
        ("Pneus", 2, 0.7, 1.1),
        ("Pneus", 6, 1.2, 1.3)
    ]

    train = bin_packing_probleme_d2_offline_first(list_marchandises, 11.583)
    print("nb wagons : ", len(train.wagons))
    # Call the function with your wagons and container dimensions
    show_wagons_2d(train.wagons, 11.583, 2.294)
    print_train(train)











