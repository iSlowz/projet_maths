import math
import random

import matplotlib.pyplot as plt


def bin_packing_probleme_d1_offline(marchandises, capacite):
    # on utilise first fit
    marchandises = [(marchandise[0], marchandise[1]) for marchandise in marchandises]
    marchandises.sort(key=lambda x: x[1], reverse=True)
    print(marchandises)

    wagons = []  # liste de wagons, avec chaque wagon qui contient une liste de marchandises
    wagons_poids = []  # liste de poids des wagons
    for marchandise in marchandises:
        if not wagons:
            wagons.append([marchandise])
            wagons_poids.append(marchandise[1])
        else:
            for i in range(len(wagons)):
                if wagons_poids[i] + marchandise[1] <= capacite:
                    wagons[i].append(marchandise)
                    wagons_poids[i] += marchandise[1]
                    break
            else:
                wagons.append([marchandise])
                wagons_poids.append(marchandise[1])
    return wagons


def bin_packing_probleme_d1_online(marchandises, capacite):
    # on utilise first fit
    marchandises = [(marchandise[0], marchandise[1]) for marchandise in marchandises]
    print(marchandises)

    wagons = []  # liste de wagons, avec chaque wagon qui contient une liste de marchandises
    wagons_poids = []  # liste de poids des wagons
    for marchandise in marchandises:
        if not wagons:
            wagons.append([marchandise])
            wagons_poids.append(marchandise[1])
        else:
            for i in range(len(wagons)):
                if wagons_poids[i] + marchandise[1] <= capacite:
                    wagons[i].append(marchandise)
                    wagons_poids[i] += marchandise[1]
                    break
            else:
                wagons.append([marchandise])
                wagons_poids.append(marchandise[1])
    return wagons


def bin_packing_probleme_d1_offline_best(marchandises, capacite):
    # on utilise best fit
    marchandises = [(marchandise[0], marchandise[1]) for marchandise in marchandises]
    marchandises.sort(key=lambda x: x[1], reverse=True)
    print(marchandises)

    wagons = []  # liste de wagons, avec chaque wagon qui contient une liste de marchandises
    wagons_poids = []  # liste de poids des wagons
    for marchandise in marchandises:
        wagons_poids_temp = wagons_poids.copy()
        if not wagons_poids_temp:
            wagons_poids_temp.append(capacite)
        for i in range(len(wagons)):
            wagons_poids_temp[i] -= marchandise[1]
        wagons_poids_sup = [(wagons_poids_temp[i], i) for i in range(len(wagons)) if wagons_poids_temp[i] > 0]
        if wagons_poids_sup:
            best_wagon = min(wagons_poids_sup, key=lambda x: x[0])
            wagons[best_wagon[1]].append(marchandise)
            wagons_poids[best_wagon[1]] -= marchandise[1]
        else:
            wagons.append([marchandise])
            wagons_poids.append(capacite - marchandise[1])

    return wagons


def bin_packing_probleme_d1_online_best(marchandises, capacite):
    # on utilise best fit
    marchandises = [(marchandise[0], marchandise[1]) for marchandise in marchandises]
    print(marchandises)

    wagons = []  # liste de wagons, avec chaque wagon qui contient une liste de marchandises
    wagons_poids = []  # liste de poids des wagons
    for marchandise in marchandises:
        wagons_poids_temp = wagons_poids.copy()
        if not wagons_poids_temp:
            wagons_poids_temp.append(capacite)
        for i in range(len(wagons)):
            wagons_poids_temp[i] -= marchandise[1]
        wagons_poids_sup = [(wagons_poids_temp[i], i) for i in range(len(wagons)) if wagons_poids_temp[i] > 0]
        if wagons_poids_sup:
            best_wagon = min(wagons_poids_sup, key=lambda x: x[0])
            wagons[best_wagon[1]].append(marchandise)
            wagons_poids[best_wagon[1]] -= marchandise[1]
        else:
            wagons.append([marchandise])
            wagons_poids.append(capacite - marchandise[1])

    return wagons


class Train:
    def __init__(self):
        self.wagons = []

    def add_wagon(self, wagon):
        self.wagons.append(wagon)


class Wagon:
    def __init__(self, capacite=(11.583, 2.294, 2.567)):
        self.max_length = capacite[0]
        self.max_width = capacite[1]
        self.max_height = capacite[2]
        self.actual_width = 0
        self.shelves = []

    def add_shelf(self, shelf):
        # shelf.max_width = self.width - self.actual_width
        self.shelves.append(shelf)
        self.get_actual_width()

    def get_actual_width(self):
        self.actual_width = sum([shelf.actual_width for shelf in self.shelves])

    def print(self):
        for i in self.shelves:
            i.print()


class Shelf:
    def __init__(self, capacite=11.583):
        self.max_length = capacite
        self.actual_length = 0
        self.actual_width = 0
        self.marchandises = []

    def add_marchandise(self, marchandise):
        self.marchandises.append(marchandise)
        self.actual_length += marchandise.length

    def print(self):
        for i in self.marchandises:
            i.print()

        print(self.marchandises)

    def __repr__(self) -> str:
        return str(self.marchandises)


class Marchandise:
    def __init__(self, name, length, width, height):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.aire = length * width

    def print(self):
        print("(", self.name, self.length, self.width, self.height, ")")


def bin_packing_probleme_d2_online_first(list_marchandises, capacite):
    # on utilise first fit
    marchandises = []
    for marchandise in list_marchandises:
        marchandises.append(Marchandise(marchandise[0], marchandise[1], marchandise[2], marchandise[3]))
    compt_sup_2 = 0
    compt_objet = 0
    for marchandise in marchandises:
        compt_objet += 1
        if marchandise.width > 1.9:
            compt_sup_2 += 1
        print(marchandise.name, marchandise.length, marchandise.width, marchandise.height)

    print('sup à 2 : ', compt_sup_2)
    print('compt objet : ', compt_objet)

    train = Train()
    print(len(marchandises))
    for marchandise in marchandises:
        if not train.wagons:
            print("a")
            wagon = Wagon()
            shelf = Shelf()
            shelf.add_marchandise(marchandise)
            shelf.actual_width = marchandise.width
            wagon.add_shelf(shelf)
            train.add_wagon(wagon)
            # print(shelf.actual_width)
            # print(marchandises[1].width)
        else:
            placed = False
            for i in range(len(train.wagons)):
                if train.wagons[i].shelves:
                    for shelf in train.wagons[i].shelves:
                        # print("test", shelf.actual_length, marchandise.length, shelf.max_length)
                        if shelf.actual_length + marchandise.length <= shelf.max_length:
                            if shelf.actual_width < marchandise.width:

                                if train.wagons[i].actual_width - shelf.actual_width + marchandise.width <= \
                                        train.wagons[i].max_width and not placed:
                                    # print("b")
                                    shelf.add_marchandise(marchandise)
                                    shelf.actual_width = marchandise.width
                                    train.wagons[i].get_actual_width()
                                    placed = True
                                    break

                            else:
                                if not placed:
                                    # print("c")
                                    shelf.add_marchandise(marchandise)
                                    placed = True
                                    break

                        else:
                            if train.wagons[i].actual_width + marchandise.width <= train.wagons[
                                i].max_width and not placed:
                                # print("d")
                                shelf = Shelf()
                                shelf.add_marchandise(marchandise)
                                shelf.actual_width = marchandise.width
                                train.wagons[i].add_shelf(shelf)
                                placed = True
                                break

                else:
                    if not placed:
                        # print("f")

                        shelf = Shelf()
                        shelf.add_marchandise(marchandise)
                        shelf.actual_width = marchandise.width
                        train.wagons[i].add_shelf(shelf)
                        placed = True
                        break
            else:
                if not placed:
                    wagon = Wagon()
                    shelf = Shelf()
                    shelf.add_marchandise(marchandise)
                    shelf.actual_width = marchandise.width
                    wagon.add_shelf(shelf)
                    train.add_wagon(wagon)

    return train


def bin_packing_probleme_d2_offline_first(list_marchandises, capacite):
    # on utilise first fit
    list_marchandises.sort(key=lambda x: x[2], reverse=True)
    marchandises = []
    for marchandise in list_marchandises:
        marchandises.append(Marchandise(marchandise[0], marchandise[1], marchandise[2], marchandise[3]))
    compt_sup_2 = 0
    compt_objet = 0
    for marchandise in marchandises:
        compt_objet += 1
        if marchandise.width > 1.9:
            compt_sup_2 += 1
        print(marchandise.name, marchandise.length, marchandise.width, marchandise.height)

    print('sup à 2 : ', compt_sup_2)
    print('compt objet : ', compt_objet)

    train = Train()
    print(len(marchandises))
    for marchandise in marchandises:
        if not train.wagons:
            print("a")
            wagon = Wagon()
            shelf = Shelf()
            shelf.add_marchandise(marchandise)
            shelf.actual_width = marchandise.width
            wagon.add_shelf(shelf)
            train.add_wagon(wagon)
            # print(shelf.actual_width)
            # print(marchandises[1].width)
        else:
            placed = False
            for i in range(len(train.wagons)):
                if train.wagons[i].shelves:
                    for shelf in train.wagons[i].shelves:
                        # print("test", shelf.actual_length, marchandise.length, shelf.max_length)
                        if shelf.actual_length + marchandise.length <= shelf.max_length:
                            if shelf.actual_width < marchandise.width:

                                if train.wagons[i].actual_width - shelf.actual_width + marchandise.width <= \
                                        train.wagons[i].max_width and not placed:
                                    # print("b")
                                    shelf.add_marchandise(marchandise)
                                    shelf.actual_width = marchandise.width
                                    train.wagons[i].get_actual_width()
                                    placed = True
                                    break

                            else:
                                if not placed:
                                    # print("c")
                                    shelf.add_marchandise(marchandise)
                                    placed = True
                                    break

                        else:
                            if train.wagons[i].actual_width + marchandise.width <= train.wagons[
                                i].max_width and not placed:
                                # print("d")
                                shelf = Shelf()
                                shelf.add_marchandise(marchandise)
                                shelf.actual_width = marchandise.width
                                train.wagons[i].add_shelf(shelf)
                                placed = True
                                break

                else:
                    if not placed:
                        # print("f")

                        shelf = Shelf()
                        shelf.add_marchandise(marchandise)
                        shelf.actual_width = marchandise.width
                        train.wagons[i].add_shelf(shelf)
                        placed = True
                        break
            else:
                if not placed:
                    wagon = Wagon()
                    shelf = Shelf()
                    shelf.add_marchandise(marchandise)
                    shelf.actual_width = marchandise.width
                    wagon.add_shelf(shelf)
                    train.add_wagon(wagon)

    return train


def show_wagons_2d(wagons: list, contenair_length: float, contenair_width: float) -> None:
    num_wagons = len(wagons)
    cols = math.ceil(math.sqrt(num_wagons))
    rows = math.ceil(num_wagons / cols)

    _, axes = plt.subplots(rows, cols, figsize=(15, 10))

    if rows > 1:
        axes = axes.flatten()
    else:
        axes = [axes]

    for i, (wagon, ax) in enumerate(zip(wagons, axes)):
        wagon_current_length = 0
        wagon_current_width = 0
        wagon_current_width_row = 0

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(0, contenair_length)
        ax.set_ylim(0, contenair_width)
        ax.set_aspect('equal')

        for shelf in wagon.shelves:
            color = random.choice(['r', 'g', 'b', 'c', 'm', 'y', 'k'])
            for marchandise in shelf.marchandises:
                if wagon_current_length + marchandise.length <= contenair_length:
                    ax.add_patch(plt.Rectangle((wagon_current_length, wagon_current_width), marchandise.length,
                                               marchandise.width, alpha=0.5, color=color))
                    wagon_current_length += marchandise.length
                    wagon_current_width_row = max(wagon_current_width_row, marchandise.width)
                else:
                    wagon_current_width += wagon_current_width_row
                    wagon_current_length = marchandise.length
                    wagon_current_width_row = marchandise.width
                    ax.add_patch(
                        plt.Rectangle((0, wagon_current_width), marchandise.length, marchandise.width, alpha=0.5,
                                      color=color))

    for j in range(i + 1, len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.show()


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



def print_train(train):
    compt_marchandise = 0
    compt_sup_2 = 0
    for i, wagon in enumerate(train.wagons):
        # print(f"Wagon {i+1}:")
        for j, shelf in enumerate(wagon.shelves):
            # print(f"\tShelf {j+1}:")
            for k, marchandise in enumerate(shelf.marchandises):
                if marchandise.width > 1.9:
                    compt_sup_2 += 1
                compt_marchandise += 1
                # print(f"\t\tMarchandise {k+1}: {marchandise.name} ({marchandise.length}, {marchandise.width}, {marchandise.height})")
    print('sup à 2 : ', compt_sup_2)
    print('compt objet : ', compt_marchandise)


