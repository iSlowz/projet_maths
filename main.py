import time


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
    print("nombre d'addition:", nb_add)


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
    #print("Liste des combinaisons possibles:", combinations)
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


if __name__ == '__main__':
    question2()
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


