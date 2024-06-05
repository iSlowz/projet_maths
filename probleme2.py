
def bin_packing_probleme_d1_offline(marchandises, capacite):
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

wagons = bin_packing_probleme_d1_offline(list_marchandises, 11.583)
print(wagons)
print("Nombre de wagons:", len(wagons))